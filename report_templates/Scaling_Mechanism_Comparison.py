import papermill as pm
import numpy as np

section_introduction = """
## Comparison of Scaling Mechanims in Instance CMR
We start by comparing how our echo- and trace-scaling implementations of InstanceCMR account for behavior in a classic experiment where each item is presented just once per study phase. For these simulations, we used the dataset reported by @murdock1970interresponse. Each of 72 undergraduates performed 20 trials with study lists each consisting of 20 unique words visually presented at either 60 or 120 words per minute. Given a particular subject, words were unique both within and across trials, and randomly selected from the Toronto Word Pool [@friendly1982toronto], a widely-used collection of high frequency nouns, adjectives, and verbs. While the major focus of the original report by @murdock1970interresponse was to investigate inter-response times in single-trial free recall, here we focus consideration on the content of recorded recall sequences. 
"""

individual_fits_statement = """
First we evaluated each model variant based on their ability to predict the specific sequences of recalls exhibited by each participant. Considering all 20 trials performed by each participant in the dataset, we applied the differential evolution optimization technique to find for each model the parameter configuration that maximized the likelihood of recorded recall sequences. We obtained a unique optimal parameter configuration for each unique participant and each considered model variant. To measure the goodness-of-fit for each parameter configuration and corresponding model, [Figure @fig-{section_tag}Fits] plots the log-likelihood of each participant's recall sequences given each model variant's corresponding optimized parameter configuration.
"""

individual_fits_caption = """Distribution of log-likelihood scores of recall sequences exhibited by each subject under each considered model across list-lengths [@murdock1970interresponse]."""

benchmark_statistics_statement = """
As a follow-up, we also compared how readily each model could account for organizational summary statistics in the dataset. We found for each model variant the optimal parameter configuration maximizing the likelihood of the entire dataset rather than participant-by-participant. Using each fitted model variant, we simulated 1000 unique free recall trials and measured summary statistics from the result. [Figure @fig-{section_tag}Summary] plots for each model against the corresponding statistics collected over the dataset how recall probability varies as a function of serial position, how the probability of recalling an item first varies as a function of serial position, and how the conditional recall probabability of an item varies as a function of its serial lag from the previously recalled item.
"""

benchmark_statistics_caption = """Comparison of summary statistics between each model against observed data [@murdock1970interresponse]"""

section_tag = "MurdOka_Scaling_Mechanisms"

model_paths = ["compmemlearn.models.Instance_CMR", "compmemlearn.models.Instance_CMR"]

model_names = ["Trace Scaling", "Echo Scaling"]

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
        #    'choice_sensitivity',
        "context_sensitivity",
        #    'feature_sensitivity'
        "delay_drift_rate",
    ],
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
        #    'context_sensitivity',
        #    'feature_sensitivity'
        "delay_drift_rate",
    ],
]

lb = np.finfo(float).eps
ub = 1 - np.finfo(float).eps
bounds = [
    [
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, 100],
        [lb, 100],
        [lb, ub],
        [lb, 10],
        [lb, 10],
        [lb, ub],
    ],
    [
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, ub],
        [lb, 100],
        [lb, 100],
        [lb, ub],
        [lb, 10],
        [lb, 10],
        [lb, ub],
    ],
]

fixed_parameters = [
    {"choice_sensitivity": 1, "feature_sensitivity": 1},
    {"context_sensitivity": 1, "feature_sensitivity": 1},
]

pm.execute_notebook(
    "Baseline_Comparison_Template.ipynb",
    "Baseline_Comparison_{section_tag}.ipynb".format(section_tag=section_tag),
    parameters=dict(model_paths=model_paths, model_names=model_names, free_parameters=free_parameters, bounds=bounds, fixed_parameters=fixed_parameters),
)
