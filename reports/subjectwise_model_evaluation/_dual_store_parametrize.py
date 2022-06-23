import papermill as pm
import numpy as np
import os
import sys

print('sys.argv:', sys.argv)

try:
  section_tag = sys.argv[3]
except:
  section_tag = "InstanceCMR_Evaluation"

try:
  data_path = sys.argv[1]
except:
  data_path = "data/HealyKahana2014.csv"

try:
  trial_query = sys.argv[2]
except:
  trial_query = "subject != -1"
  
results_path = "reports/subjectwise_model_evaluation/results"


model_paths = [
    "compmemlearn.models.Base_CMR",
    "compmemlearn.models.Dual_ICMR",
    "compmemlearn.models.Dual_ICMR",
    "compmemlearn.models.Dual_ICMR",
    "compmemlearn.models.Dual_ICMR",
]

model_names = [
    "PrototypeCMR",
    "ICMR_2_0_0",
    "ICMR_2_0_1",
    "ICMR_2_1_0",
    "ICMR_2_1_1"
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
        'choice_sensitivity',
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
        #"context_sensitivity",
        #"feature_sensitivity",
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
        #"context_sensitivity",
        #"feature_sensitivity",
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
        #"choice_sensitivity",
        "context_sensitivity",
        #"feature_sensitivity",
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
        #"choice_sensitivity",
        "context_sensitivity",
        #"feature_sensitivity",
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
    {}, 
    {"feature_sensitivity": 1, "context_sensitivity": 1, "learn_first": False},
    {"feature_sensitivity": 1, "context_sensitivity": 1, "learn_first": True},
    {"feature_sensitivity": 1, "choice_sensitivity": 1, "learn_first": False},
    {"feature_sensitivity": 1, "choice_sensitivity": 1,"learn_first": True},
]

pm.execute_notebook(
    "reports/subjectwise_model_evaluation/_Subjectwise_Model_Evaluation.ipynb",
    "reports/subjectwise_model_evaluation/Subjectwise_Model_Evaluation_Dual_Store_{section_tag}.ipynb".format(
        section_tag=section_tag
    ),
    parameters=dict(
        data_path=data_path,
        trial_query=trial_query,
        model_paths=model_paths,
        model_names=model_names,
        free_parameters=free_parameters,
        bounds=bounds,
        fixed_parameters=fixed_parameters,
        section_tag=section_tag,
    ),
    request_save_on_cell_execute=True,
)