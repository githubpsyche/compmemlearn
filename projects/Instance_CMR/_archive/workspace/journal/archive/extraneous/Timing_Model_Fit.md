(Here we just temporarily preserve code cells developed while trying to test optimization of ICMR with numba.
This code cannot actually run while outside its original context.)


## Timing Model Fit
Fitting the model to 60 trials with my previous model prototype took around 45 minutes. If the bulk of the
processing was running the cost function and this model is ~18 times faster, then now the fit should be
retrievable in under 3 minutes. Is that true? We'll need a new `generate_objective_function` that uses the
current data_likelihood:

```python
def generate_objective_function(model_class, fixed_parameters, free_parameters, data_to_fit):
    """
    Generates and returns an objective function for input to support search through parameter space for a model
    fit using an optimization function.

    Required model_class attributes:  
    - experience: adding a new trace to the memory model  
    - force_recall: forces recall of item, ignoring model state  
    - outcome_probabilities: returns item supports given activations

    Other arguments:  
    - fixed_parameters: dictionary mapping parameter names to values they'll be fixed to during search,
        overloaded by free_parameters if overlap
    - free_parameters: list of strings naming parameters for fit during search
    - data_to_fit: array where rows identify a unique trial of responses and columns corresponds to a unique
        recall index

    Returns a function that accepts a vector x specifying arbitrary values for free parameters and returns
    evaluation of data_likelihood using the model class, all parameters, and provided data.
    """
    
    return lambda x: data_likelihood(data_to_fit, **{**fixed_parameters, **{free_parameters[i]:x[i] for i in range(len(x))}})
```

```python
from scipy.optimize import differential_evolution

lb = np.finfo(float).eps
ub = 1-np.finfo(float).eps

full_parameters = {
    'item_count': murd_length,
    'encoding_drift_rate': .8,
    'start_drift_rate': .7,
    'recall_drift_rate': .8,
    'shared_support': 0.01,
    'item_support': 1.0,
    'learning_rate': .3,
    'primacy_scale': 1.0,
    'primacy_decay': 1.0,
    'stop_probability_scale': 0.01,
    'stop_probability_growth': 0.3,
    'choice_sensitivity': 2.0
}

full_bounds = [
    (lb, ub),
    (lb, ub),
    (lb, ub),
    (lb, ub),
    (lb, ub),
    (lb, ub),
    (lb, 100),
    (lb, 100),
    (lb, ub),
    (lb, 10),
    (lb, 10)
]

free_parameters = ['encoding_drift_rate', 'start_drift_rate', 
                   'recall_drift_rate', 'shared_support', 'item_support', 
                   'learning_rate', 'primacy_scale', 'primacy_decay', 
                   'stop_probability_scale', 'stop_probability_growth', 
                   'choice_sensitivity']

cost_function = generate_objective_function(InstanceCMR, full_parameters, free_parameters, murd_trials[:60])

result = differential_evolution(cost_function, full_bounds, disp=True)
result
```

```
     fun: 1069.3487317774889
 message: 'Optimization terminated successfully.'
    nfev: 17196
     nit: 101
 success: True
       x: array([7.73221500e-01, 9.96135200e-03, 6.61082573e-01, 2.08395877e-03,
       3.81620239e-01, 2.43211146e-01, 2.93099239e+01, 2.22813126e+00,
       4.52469176e-02, 2.38529048e-01, 1.60735389e+00])
```

```python
from instance_cmr.model_analysis import visualize_fit

x = np.array([7.73221500e-01, 9.96135200e-03, 6.61082573e-01, 2.08395877e-03,
       3.81620239e-01, 2.43211146e-01, 2.93099239e+01, 2.22813126e+00,
       4.52469176e-02, 2.38529048e-01, 1.60735389e+00])

visualize_fit(InstanceCMR, {**full_parameters, **{free_parameters[i]:x[i] for i in range(len(x))}}, murd_events, 'subject == 1', experiment_count=1000, savefig=True)
```

## Full Fit for LL=20
With numba, I've gotten model simulations super fast - about 15 times faster. At our last meeting, computing
a fit for one subject in murd_data (60 trials) previously took around 45 minutes, and now it's under 3! Since
murd_trials has a length of around 1200, we can expect a fit over the entire array to complete in under an
hour on my system.

```python
cost_function = generate_objective_function(InstanceCMR, full_parameters, free_parameters, murd_trials)
result = differential_evolution(cost_function, full_bounds, disp=True)
result
```

```python
x = [3.34623226e-01, 7.50756853e-02, 9.86031648e-01, 5.88729100e-04,
   6.22223981e-01, 3.13668541e-01, 8.88600044e+00, 7.00763795e+01,
   6.65320062e-02, 1.88495323e-01, 3.22197589e+00]

visualize_fit(InstanceCMR, {**full_parameters, **{free_parameters[i]:x[i] for i in range(len(x))}}, murd_events, 'subject >= 1', experiment_count=1000, savefig=True)
```
```python

```

