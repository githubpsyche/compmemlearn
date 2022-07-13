# AUTOGENERATED! DO NOT EDIT! File to edit: library/datasets/PEERS.ipynb (unless otherwise specified).

__all__ = ['simulate_df', 'simulate_df_from_events', 'simulate_array', 'simulate_array_from_presentations',
           'find_first', 'events_metadata', 'generate_trial_mask', 'prepare_healkaha2014_data',
           'prepare_howakaha05_data', 'prepare_lohnas2014_data', 'prepare_murdock1962_data', 'prepare_murdock1970_data']

# Cell
import pandas as pd
from psifr import fr
import numpy as np
from numba import int32
from numba import njit

def simulate_df(model, experiment_count, first_recall_item=None):
    """
    Initialize a model with specified parameters and experience sequences and
    then populate a psifr-formatted dataframe with the outcomes of performing `free recall`.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - free_recall: function that freely recalls a given number of items or until recall stops
    """

    # encode items
    model.experience(model.items)

    # simulate retrieval for the specified number of times, tracking results in df
    data = []
    for experiment in range(experiment_count):
        data += [[experiment, 0, 'study', i + 1, i] for i in range(model.item_count)]
    for experiment in range(experiment_count):
        if first_recall_item is not None:
            model.force_recall(first_recall_item)
        data += [[experiment, 0, 'recall', i + 1, o] for i, o in enumerate(model.free_recall())]
        model.force_recall(0)
    data = pd.DataFrame(data, columns=['subject', 'list', 'trial_type', 'position', 'item'])
    merged = fr.merge_free_recall(data)

    return merged

# Cell

from psifr import fr
import pandas as pd
import numpy as np
from sentence_transformers import util

def simulate_df_from_events(
    model_class, parameters, events, trial_query, experiment_count, first_recall_item=None,
    string_embeddings=None):
    """
    Initialize a model with specified parameters and experience sequences and
    then populate a psifr-formatted dataframe with the outcomes of performing `free recall`.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - free_recall: function that freely recalls a given number of items or until recall stops
    - force_recall: function that forces recall of a given item
    """

    trial_mask = generate_trial_mask(events, trial_query)
    trials, list_lengths, presentations, string_ids = events_metadata(events)
    chose = [i for i in range(len(trial_mask)) if np.sum(trial_mask[i]) != 0]
    assert(len(chose) == 1)
    chose = chose[0]
    trial_mask = trial_mask[chose]
    trials = trials[chose][trial_mask]
    presentations = presentations[chose][trial_mask]
    string_ids = string_ids[chose][trial_mask]

    default_columns = ['subject', 'list', 'trial_type', 'item', 'input', 'output', 'study', 'recall', 'repeat', 'intrusion', 'first_input']
    extra_is_not_item_level = ['subject_id', 'older', 'session', 'session_list', 'task', 'list length', 'condition',]
    extra_columns = [each for each in events.columns if each not in default_columns]

    trial_labels = {}
    for column in extra_columns:
        if column not in extra_is_not_item_level:
            continue
        try:
            trial_labels[column] = (
                events.pivot_table(index=['subject', 'list'], dropna=False)[column].values)

            if 'list length' in events.columns:
                trial_details = events.pivot_table(
                    index=['subject', 'list'], dropna=False, aggfunc='first').reset_index()
                list_length_mask = trial_details.eval(trial_query).to_numpy(dtype='bool')
                trial_labels[column] = trial_labels[column][list_length_mask]
            else:
                trial_labels[column] = trial_labels[column][trial_mask]
        except KeyError:
            pass

    item_labels = {}
    for column in extra_columns:
        if column in extra_is_not_item_level:
            continue
        try:
            item_labels[column] = {}
            item_labels[column]['study'] = events.pivot_table(
                    index=['subject', 'list'], columns='input', values=column, aggfunc='first', dropna=False)
            item_labels[column]['recall'] = events.pivot_table(
                    index=['subject', 'list'], columns='output', values=column, aggfunc='first', dropna=False)
            item_labels[column]['study'] = item_labels[column]['study'].to_numpy()
            item_labels[column]['recall'] = item_labels[column]['recall'].to_numpy()

            if 'list length' in events.columns:
                trial_details = events.pivot_table(
                    index=['subject', 'list'], dropna=False, aggfunc='first').reset_index()
                list_length_mask = trial_details.eval(trial_query).to_numpy(dtype='bool')
                item_labels[column]['study'] = item_labels[column]['study'][list_length_mask]
                item_labels[column]['recall'] = item_labels[column]['recall'][list_length_mask]
            else:
                item_labels[column]['study'] = item_labels[column]['study'][trial_mask]
                item_labels[column]['recall'] = item_labels[column]['recall'][trial_mask]
        except KeyError:
            pass

    data = []
    for experiment in range(experiment_count):
        for trial_index in range(len(presentations)):

            # retrieve presentation sequence for this trial and measure number of unique items
            presentation = presentations[trial_index]
            item_count = np.max(presentation)+1

            # record presentation events
            for presentation_index, presentation_event in enumerate(presentation):
                data.append([
                    experiment, experiment*len(presentations)+trial_index,
                    'study', presentation_index+1, presentation_event,
                    find_first(presentation_event, presentation) + 1])
                for label in item_labels:
                    data[-1].append(item_labels[label]['study'][trial_index][presentation_index])
                for label in trial_labels:
                    data[-1].append(trial_labels[label][trial_index])

            # simulate recall and identify first study position of each recalled item
            if string_embeddings is None:
                model = model_class(item_count, len(presentation), parameters)
            else:
                trial_embeddings = string_embeddings[string_ids[trial_index]]
                similarities = util.pytorch_cos_sim(trial_embeddings, trial_embeddings).numpy() + 1
                np.fill_diagonal(similarities, 0)
                model = model_class(similarities, len(presentation), parameters)

            model.experience(model.items[presentation])
            if first_recall_item is not None:
                model.force_recall(first_recall_item)
            recalled = model.free_recall()
            trial = [find_first(recalled[i], presentation) + 1 for i in range(len(recalled))]

            # record recall events
            for recall_index, recall_event in enumerate(trial):
                if recall_event != 0:
                    data.append([
                        experiment, experiment*len(presentations)+trial_index,
                        'recall', recall_index+1,
                        presentation[recall_event-1], recall_event])
                    for label in item_labels:
                        data[-1].append(np.nan); #item_labels[label]['recall'][trial_index][recall_index])
                    for label in trial_labels:
                        data[-1].append(np.nan) #trial_labels[label][trial_index])

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'first_input'] + list(
            item_labels.keys()) + list(trial_labels.keys()))
    merged = fr.merge_free_recall(
        data, study_keys=['first_input'] + list(item_labels.keys()) + list(trial_labels.keys()))
    return merged

# Cell

@njit(fastmath=True, nogil=True)
def simulate_array(model, experiment_count, first_recall_item=None):

    # encode items
    model.experience(model.items)

    # simulate retrieval for the specified number of times, tracking results in array
    trials = np.zeros((experiment_count, len(model.items)), dtype=int32)

    for trial_index in range(len(trials)):

        recalled = model.free_recall()
        model.force_recall(0)
        trials[trial_index, :len(recalled)] = recalled + 1

    return trials

# Cell

@njit(nogil=True)
def simulate_array_from_presentations(model_class, parameters, presentations, experiment_count):

    # simulate retrieval for the specified number of times, tracking results in trials array
    trials = np.zeros((experiment_count * len(presentations), np.max(presentations)+1), dtype=int32)

    for experiment in range(experiment_count):
        for trial_index in range(len(presentations)):

            # retrieve presentation sequence for this trial and measure number of unique items
            presentation = presentations[trial_index]
            item_count = np.max(presentation)+1

            # simulate recall and identify first study position of each recalled item
            model = model_class(item_count, len(presentation), parameters)
            model.experience(model.items[presentation])
            recalled = model.free_recall()

            for i in range(len(recalled)):
                trials[experiment*len(presentations) + trial_index, i] = find_first(recalled[i], presentation) + 1

    return trials

@njit(nogil=True)
def find_first(item, vec):
    """return the index of the first occurence of item in vec"""
    for i in range(len(vec)):
        if item == vec[i]:
            return i
    return -1

# Cell

import numpy as np
import pandas as pd

def events_metadata(events):
    """
    Return as numpy arrays and vectors key metadata about recall events dataframe structure

    Generates a metadata array for each list length, and returns a list of these arrays.
    """

    # list lengths for efficient presentation simulation
    if 'list length' in events.columns:
        list_lengths = [int(each) for each in pd.unique(events["list length"])]
        ll_specific_trial_query = '`list length` == {}'
    else:
        list_lengths = [int(np.max(events.input))]
        ll_specific_trial_query = 'subject != -1'

    # trials for efficient recall simulation
    trials = []
    presentations = []
    if 'item_string_index' in events.columns:
        item_string_indices = []
    else:
        item_string_indices = None

    trial_details = events.pivot_table(index=['subject', 'list'], dropna=False, aggfunc='first').reset_index()
    for list_length in list_lengths:

        # generate list_length mask
        list_length_mask = trial_details.eval(
            ll_specific_trial_query.format(list_length)).to_numpy(dtype='bool')

        df_value = 'first_input' if 'first_input' in events.columns else 'input'
        trials_df = events.pivot_table(index=['subject', 'list'], columns='output', values=df_value, dropna=False)

        trials_array = trials_df.to_numpy(na_value=0).astype('int32')[list_length_mask]
        trials.append(trials_array[:, :min(list_length, trials_array.shape[1])])

        presentations_df = events.pivot_table(index=['subject', 'list'], columns='input', values='item', dropna=False)
        presentations_array = presentations_df.to_numpy(na_value=0).astype('int32')[list_length_mask]
        presentations.append(presentations_array[:, :min(list_length, presentations_array.shape[1])])

        if item_string_indices is not None:
            item_string_indices_df =  events.pivot_table(
                index=['subject', 'list'], columns='input', values='item_string_index', dropna=False)
            item_string_indices_array = item_string_indices_df.to_numpy().astype('int32')[list_length_mask]
            item_string_indices.append(item_string_indices_array[:, :min(list_length, item_string_indices_array.shape[1])])

    return trials, list_lengths, presentations, item_string_indices

# Cell

def generate_trial_mask(events, trial_query):
    """
    Return mask vector(s) selecting trials that match a query based on elements in events dataframe.

    Generates a mask vector for each list length, and returns a list of masks for each list length.
    """

    # infer list length(s)
    if 'list length' in events.columns:
        list_lengths = [int(each) for each in pd.unique(events["list length"])]
        ll_specific_trial_query = '`list length` == {}'
    else:
        list_lengths = [int(np.max(events.input))]
        ll_specific_trial_query = 'subject != -1'

    # build trials argument, careful to filter out recalls and presentations rows with same query
    trial_details = events.pivot_table(index=['subject', 'list'], dropna=False, aggfunc='first').reset_index()

    trial_masks = []

    for list_length in list_lengths:

        # generate list_length mask
        list_length_mask = trial_details.eval(
            ll_specific_trial_query.format(list_length)).to_numpy(dtype='bool')

        # generate trial mask and mask with list_length mask
        trial_mask = trial_details.eval(trial_query).to_numpy(dtype='bool')
        trial_masks.append(trial_mask[list_length_mask])

    return trial_masks

# Cell

import scipy.io as sio
import numpy as np
import pandas as pd
from psifr import fr

def prepare_healkaha2014_data(path):
    """
    Prepares data formatted like `data/MurdData_clean.mat` for fitting.

    Loads data from `path` with same format as `data/MurdData_clean.mat` and
    returns a selected dataset as an array of unique recall trials and a
    dataframe of unique study and recall events organized according to `psifr`
    specifications.

    **Arguments**:
    - path: source of data file
    - dataset_index: index of the dataset to be extracted from the file

    **Returns**:
    - trials: int64-array where rows identify a unique trial of responses and
        columns corresponds to a unique recall index.
    - merged: as a long format table where each row describes one study or
        recall event.
    - list_length: length of lists studied in the considered dataset
    """

    # load all the data
    mat_file = sio.loadmat(path, squeeze_me=True)
    mat_data = [mat_file['data'].item()[i] for i in range(10)]
    subjects = mat_data[0].astype('int64')
    session = mat_data[1].astype('int64')
    pres_item_strings = mat_data[2]
    pres_item_numbers = mat_data[3].astype('int64')
    rec_item_strings = mat_data[4]
    rec_item_numbers = mat_data[5].astype('int64')
    trials = mat_data[6].astype('int64')
    intrusions = mat_data[7]
    list_length = mat_data[8]
    list_type = mat_data[9]

    # build dataframe in psifr format
    data_columns = [
        'subject', 'list', 'trial_type', 'position', 'item', 'item_string_index',
        'item_string', 'session', 'session_list', 'task']
    data = []
    for trial_index, trial in enumerate(trials):

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            list_index = 0
        list_index += 1

        # every time the session changes, reset session_list_index
        if not data or data[-1][1] != session[trial_index]:
            session_list_index = 0
        session_list_index += 1

        # add study events
        for i in range(list_length):
            data += [[np.abs(subjects[trial_index]),
                      list_index, 'study', i+1, i, pres_item_numbers[trial_index][i], pres_item_strings[trial_index][i],
                      session[trial_index], session_list_index, list_type[trial_index]]]

        # add recall events
        output_position = 1
        for recall_index, recall_event in enumerate(trial):
            if recall_event > 0 and recall_event not in trial.tolist()[:recall_index]:
                data += [[np.abs(subjects[trial_index]), list_index,
                          'recall', output_position, recall_event-1, rec_item_numbers[trial_index][recall_index], rec_item_strings[trial_index][recall_index], session[trial_index], session_list_index, list_type[trial_index]]]
                output_position += 1

    data = pd.DataFrame(data, columns=data_columns)
    merged = fr.merge_free_recall(data, list_keys=data_columns[5:])
    return merged, list_length

# Cell

import numpy as np
import pandas as pd
from psifr import fr

def prepare_howakaha05_data(path):
    """
    Prepares data formatted like `../data/HowaKaha05.dat` for fitting.
    """

    with open(path) as f:
        howa_data = f.read()

    subject_count = 66
    trial_count = 15
    total_lines = 66 * 15 * 5
    list_length = 90

    lines = [each.split('\t') for each in howa_data.split('\n')]
    trial_info_inds = np.arange(1, total_lines, 5)
    presentation_info_inds = np.arange(2, total_lines, 5)
    recall_info_inds = np.arange(4, total_lines, 5)

    # build vectors/matrices tracking list types and presentation item numbers across trials
    list_types = np.array([int(lines[trial_info_inds[i]-1][2]) for i in range(subject_count * trial_count)])
    subjects = np.array([int(lines[trial_info_inds[i]-1][0]) for i in range(subject_count * trial_count)])

    pres_itemnos = np.array([[int(each) for each in lines[presentation_info_inds[i]-1][:-1]] for i in range(
        subject_count * trial_count)])

    # convert pres_itemnos into rows of unique indices for easier model encoding
    presentations = []
    for i in range(len(pres_itemnos)):
        seen = []
        presentations.append([])
        for p in pres_itemnos[i]:
            if p not in seen:
                seen.append(p)
            presentations[-1].append(seen.index(p))
    presentations = np.array(presentations)

    # track recalls, discarding intrusions
    trials = []
    for i in range(subject_count * trial_count):
        trials.append([])

        # if it can be cast as a positive integer and is not yet in the recall sequence, it's not an intrusion
        trial = lines[recall_info_inds[i]-1][:-1]
        for t in trial:
            try:
                t = int(t)
                if (t in pres_itemnos[i]):
                    #item = presentations[i][np.where(pres_itemnos[i] == t)[0][0]]+1
                    item = np.where(pres_itemnos[i] == t)[0][0] + 1
                    if item not in trials[-1]:
                        trials[-1].append(item)
            except ValueError:
                continue

        # pad with zeros to make sure the list is the right length
        while len(trials[-1]) < list_length:
            trials[-1].append(0)

    trials = np.array(trials)

    # encode dataset into psifr format
    data = []
    subject_counter = 0
    for trial_index, trial in enumerate(trials):
        presentation = presentations[trial_index]

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            subject_counter += 1
            list_index = 0
        list_index += 1

        # add study events
        for presentation_index, presentation_event in enumerate(presentation):
            data += [[subjects[trial_index],
                      list_index, 'study', presentation_index+1, presentation_event,  list_types[trial_index], find_first(presentation_event, presentation) + 1
                     ]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, presentation[recall_event-1], list_types[trial_index], recall_event
                         ]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'condition', 'first_input'])
    merged = fr.merge_free_recall(data, list_keys=['condition', 'first_input'])

    return trials, merged, list_length, presentations, list_types, data, subjects

# Cell

import scipy.io as sio
import numpy as np
import pandas as pd
from psifr import fr


def prepare_lohnas2014_data(path):
    """
    Prepares data formatted like `data/repFR.mat` for fitting.
    """

    # load all the data
    matfile = sio.loadmat(path, squeeze_me=True)['data'].item()
    subjects = matfile[0]
    pres_itemnos = matfile[4]
    recalls = matfile[6]
    list_types = matfile[7]
    list_length = matfile[12]

    # convert pres_itemnos into rows of unique indices for easier model encoding
    presentations = []
    for i in range(len(pres_itemnos)):
        seen = []
        presentations.append([])
        for p in pres_itemnos[i]:
            if p not in seen:
                seen.append(p)
            presentations[-1].append(seen.index(p))
    presentations = np.array(presentations)

    # discard intrusions from recalls
    trials = []
    for i in range(len(recalls)):
        trials.append([])

        trial = list(recalls[i])
        for t in trial:
            if (t > 0) and (t not in trials[-1]):
                trials[-1].append(t)

        while len(trials[-1]) < list_length:
            trials[-1].append(0)

    trials = np.array(trials)

    # encode dataset into psifr format
    data = []
    for trial_index, trial in enumerate(trials):
        presentation = presentations[trial_index]

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            list_index = 0
        list_index += 1

        # add study events
        for presentation_index, presentation_event in enumerate(presentation):
            data += [[subjects[trial_index],
                      list_index, 'study', presentation_index+1, presentation_event, list_types[trial_index],
                      find_first(presentation_event, presentation) + 1
                     ]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, presentation[recall_event-1], list_types[trial_index], recall_event
                         ]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'condition', 'first_input'])
    merged = fr.merge_free_recall(data, list_keys=['condition', 'first_input'])

    return trials, merged, list_length, presentations, list_types, data, subjects

# Cell

import scipy.io as sio
import numpy as np
import pandas as pd
from psifr import fr

def prepare_murdock1962_data(path, dataset_index=0):
    """
    Prepares data formatted like `data/MurdData_clean.mat` for fitting.

    Loads data from `path` with same format as `data/MurdData_clean.mat` and
    returns a selected dataset as an array of unique recall trials and a
    dataframe of unique study and recall events organized according to `psifr`
    specifications.

    **Arguments**:
    - path: source of data file
    - dataset_index: index of the dataset to be extracted from the file

    **Returns**:
    - trials: int64-array where rows identify a unique trial of responses and
        columns corresponds to a unique recall index.
    - merged: as a long format table where each row describes one study or
        recall event.
    - list_length: length of lists studied in the considered dataset
    """

    # load all the data
    matfile = sio.loadmat(path, squeeze_me=True)
    murd_data = [matfile['data'].item()[0][i].item() for i in range(3)]

    # encode dataset into psifr format
    trials, list_length, subjects = murd_data[dataset_index][:3]
    trials = trials.astype('int64')

    data = []
    for trial_index, trial in enumerate(trials):

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            list_index = 0
        list_index += 1

        # add study events
        for i in range(list_length):
            data += [[subjects[trial_index],
                      list_index + (dataset_index * 1000), 'study', i+1, i]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index + (dataset_index * 1000),
                          'recall', recall_index+1, recall_event-1]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item'])
    merged = fr.merge_free_recall(data)
    return trials, merged, list_length

# Cell
import numpy as np
import pandas as pd
from psifr import fr

def prepare_murdock1970_data(path):
    """
    Prepares data formatted like `data/MurdData_clean.mat` for fitting.

    Loads data from `path` with same format as `data/MurdData_clean.mat` and
    returns a selected dataset as an array of unique recall trials and a
    dataframe of unique study and recall events organized according to `psifr`
    specifications.

    **Arguments**:
    - path: source of data file
    - dataset_index: index of the dataset to be extracted from the file

    **Returns**:
    - trials: int64-array where rows identify a unique trial of responses and
        columns corresponds to a unique recall index.
    - merged: as a long format table where each row describes one study or
        recall event.
    - list_length: length of lists studied in the considered dataset
    """

    with open(path) as f:
        oka_data = f.read()

    counter = 0
    trials = []
    subjects = []
    list_length = 20

    for line in oka_data.split('\n'):

        if not line:
            continue

        # build subjects array
        if counter == 0:
            subjects.append(int(line.strip().split('    ')[1]))

        # build trials array
        if counter == 1:

            trial = [int(each) for each in line.strip().split('    ')]
            trial = [each for each in trial if each <= 20]
            already = []
            for each in trial:
                if each not in already:
                    already.append(each)
            trial = already

            while len(trial) < 13:
                trial.append(0)

            trials.append(trial)

        # keep track of which row we are on for the given trial
        counter += 1
        if counter == 3:
            counter = 0

    trials = np.array(trials).astype('int64')

    data = []
    for trial_index, trial in enumerate(trials):

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            list_index = 0
        list_index += 1

        # add study events
        for i in range(list_length):
            data += [[subjects[trial_index],
                      list_index, 'study', i+1, i]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, recall_event-1]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item'])
    merged = fr.merge_free_recall(data)
    return trials, merged, list_length