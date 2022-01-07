# AUTOGENERATED! DO NOT EDIT! File to edit: library/model_analysis/Fitting_by_Likelihood.ipynb (unless otherwise specified).

__all__ = ['murdock_data_likelihood', 'murdock_objective_function', 'lohnas_data_likelihood',
           'lohnas_objective_function', 'apply_and_concatenate', 'murdock_data_likelihood',
           'murdock_objective_function', 'lohnas_data_likelihood', 'lohnas_objective_function', 'apply_and_concatenate']

# Cell
# hide

import numpy as np
from numba import njit, prange
from numba.typed import Dict
from numba.core import types

@njit(fastmath=True, nogil=True, parallel=True)
def murdock_data_likelihood(data_to_fit, item_counts, model_class, parameters):

    result = 0.0
    for i in prange(len(item_counts)):
        item_count = item_counts[i]
        trials = data_to_fit[i]
        likelihood = np.ones((len(trials), item_count))

        model = model_class(item_count, item_count, parameters)
        model.experience(model.items)

        for trial_index in range(len(trials)):
            trial = trials[trial_index]

            model.force_recall()
            for recall_index in range(len(trial) + 1):

                # identify index of item recalled; if zero then recall is over
                if recall_index == len(trial) and len(trial) < item_count:
                    recall = 0
                else:
                    recall = trial[recall_index]

                # store probability of and simulate recall of indexed item
                likelihood[trial_index, recall_index] = \
                    model.outcome_probabilities()[recall] + 10e-7

                if recall == 0:
                    break
                model.force_recall(recall)

            # reset model to its pre-retrieval (but post-encoding) state
            model.force_recall(0)

        result -= np.sum(np.log(likelihood))

    return result

def murdock_objective_function(data_to_fit, item_counts, model_class, fixed_parameters, free_parameters):
    """
    Configures cmr_likelihood for search over specified free/fixed parameters.
    """

    parameters = Dict.empty(key_type=types.unicode_type, value_type=types.float64)
    for name, value in fixed_parameters.items():
        parameters[name] = value

    def objective_function(x):
        for i in range(len(free_parameters)):
            parameters[free_parameters[i]] = x[i]
        return murdock_data_likelihood(data_to_fit, item_counts, model_class, parameters)

    return objective_function

# Cell
# hide

import numpy as np
from numba import njit, prange
from .models import Classic_CMR


#@njit(fastmath=True, nogil=True, parallel=True)
@njit(nogil=True)
def lohnas_data_likelihood(trials, presentations, model_class, parameters):

    list_length = len(presentations[0])
    likelihood = np.ones((len(trials), list_length))

    for trial_index in prange(len(trials)):

        item_count = np.max(presentations[trial_index])+1
        trial = trials[trial_index]
        model = model_class(item_count, list_length, parameters)
        model.experience(model.items[presentations[trial_index]])

        model.force_recall()
        for recall_index in range(len(trial) + 1):

            # identify index of item recalled; if zero then recall is over
            if recall_index == len(trial) and len(trial) < item_count:
                recall = 0
            elif trial[recall_index] == 0:
                recall = 0
            else:
                recall = presentations[trial_index][trial[recall_index]-1] + 1

            # store probability of and simulate recalling item with this index
            likelihood[trial_index, recall_index] = \
                model.outcome_probabilities()[recall] + 10e-7

            if recall == 0:
                break
            model.force_recall(recall)

        # reset model to its pre-retrieval (but post-encoding) state
        model.force_recall(0)

    return -np.sum(np.log(likelihood))

def lohnas_objective_function(data_to_fit, presentations, model_class, fixed_parameters, free_parameters):

    """
    Generates and returns an objective function for input to support search
    through parameter space for model fit using an optimization function.

    Returns a function that accepts a vector x specifying arbitrary values for
    free parameters and returns evaluation of likelihood using the model
    class, all parameters, and provided data.
    """

    parameters = Dict.empty(key_type=types.unicode_type, value_type=types.float64)
    for name, value in fixed_parameters.items():
        parameters[name] = value

    def objective_function(x):
        for i in range(len(free_parameters)):
            parameters[free_parameters[i]] = x[i]
        return lohnas_data_likelihood(data_to_fit, presentations, model_class, parameters)

    return objective_function

# Cell
import pandas as pd

def apply_and_concatenate(function, df1, df2, contrast_name='contrast', labels='AB'):
    """
    Concatenates the results of a function applied to two dataframes and creates a new column identifying the contrast.
    """
    return pd.concat([function(df1), function(df2)], keys=labels, names=[contrast_name]).reset_index()

# Cell
# hide

import numpy as np
from numba import njit, prange
from numba.typed import Dict
from numba.core import types

@njit(fastmath=True, nogil=True, parallel=True)
def murdock_data_likelihood(data_to_fit, item_counts, model_class, parameters):

    result = 0.0
    for i in prange(len(item_counts)):
        item_count = item_counts[i]
        trials = data_to_fit[i]
        likelihood = np.ones((len(trials), item_count))

        model = model_class(item_count, item_count, parameters)
        model.experience(model.items)

        for trial_index in range(len(trials)):
            trial = trials[trial_index]

            model.force_recall()
            for recall_index in range(len(trial) + 1):

                # identify index of item recalled; if zero then recall is over
                if recall_index == len(trial) and len(trial) < item_count:
                    recall = 0
                else:
                    recall = trial[recall_index]

                # store probability of and simulate recall of indexed item
                likelihood[trial_index, recall_index] = \
                    model.outcome_probabilities()[recall] + 10e-7

                if recall == 0:
                    break
                model.force_recall(recall)

            # reset model to its pre-retrieval (but post-encoding) state
            model.force_recall(0)

        result -= np.sum(np.log(likelihood))

    return result

def murdock_objective_function(data_to_fit, item_counts, model_class, fixed_parameters, free_parameters):
    """
    Configures cmr_likelihood for search over specified free/fixed parameters.
    """

    parameters = Dict.empty(key_type=types.unicode_type, value_type=types.float64)
    for name, value in fixed_parameters.items():
        parameters[name] = value

    def objective_function(x):
        for i in range(len(free_parameters)):
            parameters[free_parameters[i]] = x[i]
        return murdock_data_likelihood(data_to_fit, item_counts, model_class, parameters)

    return objective_function

# Cell
# hide

import numpy as np
from numba import njit, prange
from .models import Classic_CMR


#@njit(fastmath=True, nogil=True, parallel=True)
@njit(nogil=True)
def lohnas_data_likelihood(trials, presentations, model_class, parameters):

    list_length = len(presentations[0])
    likelihood = np.ones((len(trials), list_length))

    for trial_index in prange(len(trials)):

        item_count = np.max(presentations[trial_index])+1
        trial = trials[trial_index]
        model = model_class(item_count, list_length, parameters)
        model.experience(model.items[presentations[trial_index]])

        model.force_recall()
        for recall_index in range(len(trial) + 1):

            # identify index of item recalled; if zero then recall is over
            if recall_index == len(trial) and len(trial) < item_count:
                recall = 0
            elif trial[recall_index] == 0:
                recall = 0
            else:
                recall = presentations[trial_index][trial[recall_index]-1] + 1

            # store probability of and simulate recalling item with this index
            likelihood[trial_index, recall_index] = \
                model.outcome_probabilities()[recall] + 10e-7

            if recall == 0:
                break
            model.force_recall(recall)

        # reset model to its pre-retrieval (but post-encoding) state
        model.force_recall(0)

    return -np.sum(np.log(likelihood))

def lohnas_objective_function(data_to_fit, presentations, model_class, fixed_parameters, free_parameters):

    """
    Generates and returns an objective function for input to support search
    through parameter space for model fit using an optimization function.

    Returns a function that accepts a vector x specifying arbitrary values for
    free parameters and returns evaluation of likelihood using the model
    class, all parameters, and provided data.
    """

    parameters = Dict.empty(key_type=types.unicode_type, value_type=types.float64)
    for name, value in fixed_parameters.items():
        parameters[name] = value

    def objective_function(x):
        for i in range(len(free_parameters)):
            parameters[free_parameters[i]] = x[i]
        return lohnas_data_likelihood(data_to_fit, presentations, model_class, parameters)

    return objective_function

# Cell
import pandas as pd

def apply_and_concatenate(function, df1, df2, contrast_name='contrast', labels='AB'):
    """
    Concatenates the results of a function applied to two dataframes and creates a new column identifying the contrast.
    """
    return pd.concat([function(df1), function(df2)], keys=labels, names=[contrast_name]).reset_index()