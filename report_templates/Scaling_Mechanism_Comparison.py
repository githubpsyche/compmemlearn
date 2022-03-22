import papermill as pm
import numpy as np
import os

section_tag = "Scaling_Mechanisms"

data_path = "data/Murdock1962.csv"
trial_query = "subject > -1"
results_path = "results/"

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
    {"choice_sensitivity": 1, "feature_sensitivity": 1, 'mfc_familiarity_scale': 0, 
         'mcf_familiarity_scale': 0, 'drift_familiarity_scale': 0},
    {"context_sensitivity": 1, "feature_sensitivity": 1, 'mfc_familiarity_scale': 0, 
         'mcf_familiarity_scale': 0, 'drift_familiarity_scale': 0},
]

print(os.environ['PYTHONPATH'].split(os.pathsep))

pm.execute_notebook(
    "Subjectwise_Model_Evaluation.ipynb",
    "reports/Subjectwise_Model_Evaluation_{section_tag}.ipynb".format(section_tag=section_tag),
    parameters=dict(model_paths=model_paths, model_names=model_names, free_parameters=free_parameters, bounds=bounds, fixed_parameters=fixed_parameters), request_save_on_cell_execute=True, engine_name=os.environ['PYTHONPATH'].split(os.pathsep)[0]
)