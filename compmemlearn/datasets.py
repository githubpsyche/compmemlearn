# AUTOGENERATED! DO NOT EDIT! File to edit: library/datasets/PEERS.ipynb (unless otherwise specified).

__all__ = ['prepare_clairexpt6_data', 'simulate_df', 'simulate_data', 'simulate_array',
           'simulate_array_from_presentations', 'find_first', 'events_metadata', 'prepare_healkaha2014_data',
           'prepare_howakaha05_data', 'prepare_lohnas2014_data', 'prepare_murdock1962_data', 'prepare_murdock1970_data']

# Cell

def prepare_clairexpt6_data(main_path, rp_itemnos_path):

    # load all the data
    matfile = sio.loadmat(main_path, squeeze_me=True)['data'].item()
    trials = matfile[4].astype('int64') # cleaner version, wo intrusions
    subjects = matfile[1].astype('int64')
    condition = matfile[2].astype('int64')
    cond_rp = matfile[5] # identifies rp condition variables
    cond_control = matfile[6] # identifies control condition variables
    list_length = matfile[3]

    # item sequences for rp condition
    rp_sequences = sio.loadmat(rp_itemnos_path, squeeze_me=True)['rp_itemnos'].astype('int64')

    data = []
    for trial_index, trial in enumerate(trials):

        # skip further processing if subject is coded as negative number
        if subjects[trial_index] < 0:
            continue

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            list_index = 0
        list_index += 1

        # add normal study events
        for i in range(list_length):
            data += [[subjects[trial_index], list_index, 'study', i+1, i+1, condition[trial_index]]]

        # if applicable, add rp events
        if condition[trial_index]:
            for i in range(3):
                if rp_sequences[trial_index, i]:
                    data += [[subjects[trial_index], list_index, 'study', rp_sequences[trial_index, i], rp_sequences[trial_index, i], condition[trial_index]]]

        # and recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, recall_event, condition[trial_index]]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'condition'])

    merged = fr.merge_free_recall(data, list_keys=['condition'])
    rp_sequences[rp_sequences <= 0] = 0
    presentations = np.hstack((np.matlib.repmat(np.arange(list_length)+1, len(rp_sequences), 1), rp_sequences))

    return trials, merged, list_length, presentations, condition, data, subjects[subjects>0], cond_rp, cond_control

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

simulate_data = simulate_df

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

def events_metadata(events, trial_query='subject > -1'):

    # build list lengths argument, careful to avoid including filtered-out list lengths
    if 'list length' in events.columns:
        list_lengths = [int(each) for each in pd.unique(events.query(trial_query)["list length"])]
        ll_specific_trial_query = trial_query + ' & `list length` == {list_length}'
    else:
        ll_specific_trial_query = trial_query
        list_lengths = [int(np.max(events.query(trial_query).input))]

    # build trials argument, careful to filter out recalls and presentations rows with same query
    trials = []
    presentations = []
    trial_details = events.pivot_table(index=['subject', 'list'], dropna=False).reset_index()
    for list_length in list_lengths:
        trial_filter = trial_details.eval(ll_specific_trial_query.format(list_length=list_length))
        trials_df = events.pivot_table(index=['subject', 'list'], columns='output', values='item', dropna=False)
        trials_array = trials_df.to_numpy(na_value=0).astype('int32')[trial_filter]
        #trials_array = np.hstack((trials_array, np.zeros((trials_array.shape[0], 1), dtype=np.int32)))
        trials.append(trials_array)

        presentations_df = events.pivot_table(index=['subject', 'list'], columns='input', values='item', dropna=False)
        presentations_array = presentations_df.to_numpy(na_value=0).astype('int32')[trial_filter]
        presentations.append(presentations_array)

    # dont make trials or lists_lengths or presentations lists if they are only one element
    if len(trials) == 1:
        trials = trials[0]
    if len(list_lengths) == 1:
        list_lengths = list_lengths[0]
    if len(presentations) == 1:
        presentations = presentations[0]

    return trials, list_lengths, presentations, trial_details[trial_details.eval(trial_query)]

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
    subjects = mat_data[0]
    session = mat_data[1]
    pres_item_strings = mat_data[2]
    pres_item_numbers = mat_data[3]
    rec_item_strings = mat_data[4]
    rec_item_numbers = mat_data[5]
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
            data += [[subjects[trial_index],
                      list_index, 'study', i+1, i+1, pres_item_numbers[trial_index][i], pres_item_strings[trial_index][i],
                      session[trial_index], session_list_index, list_type[trial_index]]]

        # add recall events
        output_position = 1
        for recall_index, recall_event in enumerate(trial):
            if recall_event > 0 and recall_event not in trial.tolist()[:recall_index]:
                data += [[subjects[trial_index], list_index,
                          'recall', output_position, recall_event, rec_item_numbers[trial_index][recall_index], rec_item_strings[trial_index][recall_index], session[trial_index], session_list_index, list_type[trial_index]]]
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
    for trial_index, trial in enumerate(trials):
        presentation = presentations[trial_index]

        # every time the subject changes, reset list_index
        if not data or data[-1][0] != subjects[trial_index]:
            list_index = 0
        list_index += 1

        # add study events
        for presentation_index, presentation_event in enumerate(presentation):
            data += [[subjects[trial_index],
                      list_index, 'study', presentation_index+1, presentation_event,  list_types[trial_index]
                     ]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, presentation[recall_event-1], list_types[trial_index]
                         ]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'condition'])
    merged = fr.merge_free_recall(data, list_keys=['condition'])

    return trials, merged, list_length, presentations, list_types, data, subjects

# Cell

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
                      list_index, 'study', presentation_index+1, presentation_event,  list_types[trial_index]
                     ]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, recall_event, list_types[trial_index]
                         ]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'condition'])
    merged = fr.merge_free_recall(data, list_keys=['condition'])

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
                      list_index + (dataset_index * 1000), 'study', i+1, i+1]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index + (dataset_index * 1000),
                          'recall', recall_index+1, recall_event]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item'])
    merged = fr.merge_free_recall(data)
    return trials, merged, list_length

# Cell

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
                      list_index, 'study', i+1, i+1]]

        # add recall events
        for recall_index, recall_event in enumerate(trial):
            if recall_event != 0:
                data += [[subjects[trial_index], list_index,
                          'recall', recall_index+1, recall_event]]

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item'])
    merged = fr.merge_free_recall(data)
    return trials, merged, list_length