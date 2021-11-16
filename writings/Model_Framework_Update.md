# Model Framework Update

What's the smallest useful thing I can do?

Four components of likelihood function:

1. Model configuration. Initialize the model with relevant parameters.
2. Trial simulation. Simulate study events preceding behavior we want to evaluate.
3. Likelihood calculation. Calculate likelihood of recall events given the model.
4. Result aggregation. Aggregate the likelihoods of all trials.

It's the second one that differs between list lengths and lists with item repetitions, but that has consequences for the first one (how often can I get away with just configuring a model once?).

I can make a function that handles 3 and 4 while dataset-unique functions pass on relevant info from 1 and 2. Could I?

```python

model = Model(parameters)
model.experience(presentations)
likelihood = np.array()

for trial_index in prange(len(trials)):
    trial = trials[trial_index]

    for recall_index in range(len(trial) + 1):
        trial_likelihood = calculate_likelihood(model, trial[recall_index])
        aggregate_likelihood(likelihood, trial_likelihood)

return aggregate_likelihood
```

I could make a function that takes a recall sequence (trial) and a model and returns the sequence's likelihood. Wrapper function might remake the model across trials, or it might not. 

Potential downside: harder to use a common data structure to aggregate event likelihoods. Is there anything I can do about that? No, so there's little room to optimize there.

I can avoid having to define a unique function for every model variant that each has to be updated each time I alter the variant. To do that, have the likelihood function accept...

1. data_to_fit
2. presentation configuration
3. model parameter dictionary

What do I call it? 

Uh, the item_counts thing is murdock specific, so I won't bother with it.

murdock_data_likelihood(data_to_fit, item_counts, model_class, parameters)

I think I will need to update experience to not require specification of the exact representation. The current version assumes experience representations are the same across model variants. Bad idea.

#TODO: don't use int32 inside numba. Makes debugging without njit on harder.

It's almost good, but I can't directly pass a class to numba functions. Means I need some stupid pass-through function.

TODO: Next step is show this works with instance_cmr too. Done!

#TODO: I also need to make sure the objective function dispatcher works too.

Once I clarify all that, my codebase gets a lot simpler and I can make the next CMR variant without tripling its size.

Now what? Everything else is solved, just tedious. Except TraceCMR

What next then? Update compmemlearn to the point where I am regenerating the murdock fits. 