# %%
#| code-summary: code -- load dependencies and data and select parameters
#| echo: false
#| output: false

# TODO: ctrl f "list_length", "list length", "ll" for details to manipulate for variation

from compmemlearn.fitting import generate_objective_function
from compmemlearn.datasets import events_metadata, generate_trial_mask, find_first
from scipy.optimize import differential_evolution
from numba.typed import List, Dict
from numba.core import types
from numba import njit
from psifr import fr
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import importlib
import os

lb = np.finfo(float).eps
ub = 1 - np.finfo(float).eps

title = "VARIABLE_LIST_LENGTHS"
section_tag = "HealyKahana2014"
trial_query = "subject > -1"
results_path = "reports/subjectwise_model_evaluation/results/"

model_names = ["PrototypeCMR"]
model_paths = [
    "compmemlearn.models.Semantic_CMR",
]

free_parameters = [
    [
        "encoding_drift_rate",
        "start_drift_rate",
        "recall_drift_rate",
        "shared_support",
        "item_support",
        "learning_rate",
        "primacy_scale",
        "primacy_decay",
        "stop_probability_scale",
        "stop_probability_growth",
        "choice_sensitivity",
        "delay_drift_rate",
    ],
]

fixed_parameters = [
    {'semantic_scale': 0},
]

analysis_names = ['spc', 'crp', 'pfr']
analysis_paths = [
    'compmemlearn.analyses.plot_flex_spc', 
    'compmemlearn.analyses.plot_flex_crp', 
    'compmemlearn.analyses.plot_flex_pfr'
]

experiment_count = 10

list_lengths = [15, 30, 45, 60, 75, 90]

# %% 
#| code-summary: code -- retrieve specified models and analyses and individual fits
#| echo: false
#| output: false

# import models from specified source
models = []
for i in range(len(model_paths)):
    module_name, model_name = model_paths[i].rsplit('.',1)
    module = importlib.import_module(module_name)
    models.append(getattr(module, model_name))

# import analyses from specified source
analyses = []
for i in range(len(analysis_paths)):
    module_name, analysis_name = analysis_paths[i].rsplit('.',1)
    module = importlib.import_module(module_name)
    analyses.append(getattr(module, analysis_name))

# build individual fits df concatenating results from each model
individual_fits = []
for model_index, model_class in enumerate(models):
    individual_fits.append(
        pd.read_csv(results_path + '{}_{}_individual.csv'.format(section_tag, model_names[model_index])))
individual_fits = pd.concat(individual_fits, ignore_index=True)

# %%
#| code-summary: code -- specify simulation function for demonstrations
#| echo: false
#| output: false

def simulate_df_from_presentations(model_class, parameters, presentations, experiment_count):

    data = []
    for experiment in range(experiment_count):
        for trial_index in range(len(presentations)):
        
            # retrieve presentation sequence for this trial and measure number of unique items
            presentation = presentations[trial_index]
            #item_count = np.max(presentation)+1
            item_count = np.eye(np.max(presentation)+1)

            # record presentation events
            for presentation_index, presentation_event in enumerate(presentation):
                data.append([
                    experiment, experiment*len(presentations)+trial_index, 
                    'study', presentation_index+1, presentation_event, presentation_index+1])

            # simulate recall and identify first study position of each recalled item
            model = model_class(item_count, len(presentation), parameters)
            model.experience(model.items[presentation])
            recalled = model.free_recall()
            trial = [find_first(recalled[i], presentation) + 1 for i in range(len(recalled))]

            # record recall events
            for recall_index, recall_event in enumerate(trial):
                if recall_event != 0:
                    data.append([
                        experiment, experiment*len(presentations)+trial_index, 
                        'recall', recall_index+1, presentation[recall_event-1], recall_event])

    data = pd.DataFrame(data, columns=[
        'subject', 'list', 'trial_type', 'position', 'item', 'first_input'])
    merged = fr.merge_free_recall(data, list_keys=['first_input'])
    return merged

# %%
#| code-summary: code -- specify simulation function for demonstrations
#| echo: false
#| output: false

sns.set(style='darkgrid')

# for each unique model
for model_index, model_class in enumerate(models):

    sim_dfs = []
    for ll_index, list_length in enumerate(list_lengths):

        # load sim_df from csv if it exists
        sim_df_path = results_path + '{}_{}_{}_ll{}_sim_df.csv'.format(
            title, section_tag, model_names[model_index], list_length)
        if False: #os.path.isfile(sim_df_path):
            sim_df = pd.read_csv(sim_df_path)
            print('{} sim_df for {} with list_length {} and tag {} already exists'.format(
                title, model_names[model_index], list_length, section_tag))

        # otherwise, generate it
        else:

            # specify presentation sequence for this list length
            presentations = np.expand_dims(np.arange(list_length, dtype=int), axis=0)

            # specify model initializer with just in time compilation
            @njit(fastmath=True, nogil=True)
            def init_model(item_count, presentation_count, parameters):
                return model_class(item_count, presentation_count, parameters)

            # for each unique matching entry in individual df
            subject_specific_sim_dfs = []
            for subject in pd.unique(individual_fits.subject):
                
                fit_result = individual_fits.query(f'subject == {subject} & model == "{model_names[model_index]}"')

                # configure model based on specified parameters
                fitted_parameters = Dict.empty(
                    key_type=types.unicode_type, value_type=types.float64
                )
                for i in range(len(free_parameters[model_index])):
                    fitted_parameters[free_parameters[model_index][i]] = fit_result[free_parameters[model_index][i]].values[0]
                for key in fixed_parameters[model_index]:
                    fitted_parameters[key] = fixed_parameters[model_index][key]

                # simulate df based on specified model and presentation sequence(s)
                subject_specific_sim_dfs.append(simulate_df_from_presentations(
                    init_model, fitted_parameters, presentations, experiment_count))
                subject_specific_sim_dfs[-1]['subject'] = subject
                subject_specific_sim_dfs[-1]['list_length'] = list_length

            # concatenate simulations into one dataframe
            if len(subject_specific_sim_dfs) == 0:
                sim_df = None
            else:
                # save sim_df to csv
                sim_df = pd.concat(subject_specific_sim_dfs)
                sim_df.to_csv(sim_df_path, index=False)

        if sim_df is not None:
            sim_dfs.append(sim_df)

    # plot result of analysis applied to sim_df
    for analysis_index, analysis_function in enumerate(analyses):

        analysis_name = analysis_names[analysis_index]

        axis = analysis_function(
            sim_dfs, 'subject > -1', contrast_name="list length", labels=list_lengths)

        # list_length variation: customize crp axis to curb whitespace
        if analysis_name == 'crp':
            axis.set_ylim((0, .5))
        
        plt.savefig(results_path+'{}_{}_{}_ll{}_{}.pdf'.format(title, section_tag, model_names[model_index], list_length, analysis_name), bbox_inches="tight")
        plt.show()
# %%
