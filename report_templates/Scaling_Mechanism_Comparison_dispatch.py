
import papermill as pm
import numpy as np

section_introduction = """
## Comparison of Scaling Mechanims in Instance CMR
We start by comparing how our echo- and trace-scaling implementations of InstanceCMR account for behavior in a classic experiment where each item is presented just once per study phase. For these simulations, we used the dataset reported by @murdock1970interresponse. Each of 72 undergraduates performed 20 trials with study lists each consisting of 20 unique words visually presented at either 60 or 120 words per minute. Given a particular subject, words were unique both within and across trials, and randomly selected from the Toronto Word Pool [@friendly1982toronto], a widely-used collection of high frequency nouns, adjectives, and verbs. While the major focus of the original report by @murdock1970interresponse was to investigate inter-response times in single-trial free recall, here we focus consideration on the content of recorded recall sequences. 
"""
figure_caption = """Distribution of log-likelihood scores of recall sequences exhibited by each subject under each considered model across list-lengths [@murdock1970interresponse]."""

section_tag = "MurdOka"

data_path = "MurdockOkada1970.csv"

data_query = "subject > 0"

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
        #    'feature_sensitivity',
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
        'choice_sensitivity',
        #    "context_sensitivity",
        #    "feature_sensitivity",
        "delay_drift_rate",
    ]
]

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
    "Subjectwise_Model_Evaluation.ipynb",
    "Subjectwise_Model_Evaluation_{section_tag}.ipynb".format(section_tag=section_tag),
    parameters=dict(section_tag=section_tag, data_path=data_path, data_query=data_query, model_paths=model_paths, model_names=model_names, free_parameters=free_parameters, bounds=bounds, fixed_parameters=fixed_parameters),
)
