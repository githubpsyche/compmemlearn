 [
    'encoding_drift_rate',
    'delay_drift_rate',
    'start_drift_rate',
    'recall_drift_rate',
    'shared_support',
    'item_support',
    'learning_rate',
    'primacy_scale',
    'primacy_decay',
    'stop_probability_scale',
    'stop_probability_growth',
    'choice_sensitivity',
    'familiarity_scale']

True Fit Params:
[7.49829040e-01 9.40879905e-01 3.88458189e-01 9.18502901e-01
 7.36673074e-01 7.32671247e-01 7.10135255e-01 6.24997034e-01
 1.25823087e+01 2.36135876e-02 9.12404486e-02 9.52853899e+00
 7.59066815e+01]

CMR-DE Fit Params:
[8.02897453e-01 9.93387724e-01 2.28239870e-01 8.98772623e-01 
 4.43103475e-01 1.00000000e+00 3.86645895e-01 1.30164297e+00 
 7.83282934e+01 2.18380435e-02 1.21197226e-01 5.71602759e+00 
 6.17047148e+01]

 What is the difference between the two?
Drift rates are pretty close.

Shared support:
7.36673074e-01 vs 4.43103475e-01
Switching this in actually makes model worse than baseline, suppressing CRP.

Item support:
7.32670e-01 vs 1.00000000e+00
Doesn't seem to make a difference.

Learning rate:
7.10135255e-01 vs 3.86645895e-01
Increasing this seems to uplift the left side of the lag-CRP while simultaneously suppressing the right.

Primacy scale:
6.24997034e-01 vs 1.30164297e+00

Primacy decay:
1.25823087e+01 vs 7.83282934e+01

Choice sensitivity:
9.18502901e-01 vs 5.71602759e+00