# What's Going On? ICMR 3/8


## I am behind
Weeks ago I tried to outline a timeline for milestones on this project. 

| Week | Milestone |Description |
| ---- | --------- | ---------- 
| 1 | Match | Demonstrate (or not) equivalence to CMR across datasets.
| 2 | Distinguish (Theory) | Clarify latent theoretical distinctions between models, linking these with testable predictions and the literature. |
| 3 | Distinguish (Data) | Prove proposed distinctions are real (or not!) by relating models to relevant existing data sets.
| 4 | Update | Update model specification based on results, and re-analyze.
| 5+ | Relate | Connect ICMR to other instance-based models, e.g. ITS. | 
| Beyond | Convey | Develop paper, presentations, supplementary analyses. |

I thought by March I'd be focused on developing our paper/presentations/supplementary analyses, but over a week in, I'm still stuck on 1-4, which turn out to overlap way too much for meaningful segmentation into different weeks. These last few weeks haven't been totally unproductive; I've hit big milestones when it comes to tackling passageFR maturely and we've definitely substantially improved our understanding of how ICMR and CMR differ. But this project is definitely off timeline.


## So What's the Plan Now?
Considered seriously, it does seem that I'll need the rest of the month to flesh out a core group of analyses for inclusion in my April 21 presentation and in our paper. Since we now understand that comparing/contrasting/updating CMR/ICMR and reporting the outcomes of these results can't be cleanly separated into unique milestones, it's probably better to identify milestones in terms of how we'll carry out these comparisons.

First, we still need to establish that the models support fits to free recall data in the same way, at least when items are presented once. Second, there are principled reasons to suppose that the models differ with respect to the way they handle repetitions of the same item within and across contexts; we'll want to analyze those differences as well. Third, the models seem to differ greatly in how they encode semantic associations and/or non-orthogonal item representations. And finally, ICMR seems more supportive of integration with other modeling ideas rooted in instance-based frameworks, and that's worth demo-ing, too.

This week, we'll finish up our comparison between CMR and ICMR on the Murdoch dataset.

Next week, we'll finally focus in repetitions. We'll start with some toy examples to clarify our intuitions about how the models differ, and then we'll test these intuitions by testing fits to relevant datasets.

The following week, we'll try to characterize CMR's challenges encoding non-orthogonal item representations and leverage a combination of ITS and ICMR to overcome them.

No matter how far we actually get on these objectives, April needs to be devoted to pulling together a cohesive presentation for the cogsci seminar. I can add supplementary analyses only directly for that purpose, or if I have time after pulling a presentation together. 

I should probably do at least one practice presentation on April the 16th or 9th.

| Date | Milestone |Description |
| ---- | --------- | ---------- 
| 3/12 | Free Recall | Characterize performance on regular free recall task
| 3/19 | Repetition | Characterize capacity to account for effect of item repetitions
| 3/26 | Semantics | Prove proposed distinctions are real (or not!) by relating models to relevant existing data sets.
| 4/9 or 4/16 | Practice | Compile and present practice presentation to lab
| 4/21 | Present | Cogsci seminar presentation
| 5/2 | Draft | Paper draft ready for Sean's review + committee meeting


## This Week
Somewhere along my attempts to equate ICMR and CMR, my codebase got messy and my implementations of both models got worse: CMR and ICMR both run more slowly and fit worse to datasets I've considered so far. So I'm probably spending the bulk of this week retracing my steps, hopefully culminating by our meeting to a full comparison of model performance fitting to the entire Murdoch72 dataset.

If I have extra time, I can either add some other free recall dataset, or I can try for initial simulations of how CMR and ICMR handle item repetitions during encoding.


## Reminders For Later
- May want to re-enable control over 0 likelihood events (adding a constant to all likelihoods computed). Ask Sean how he dealed. It doesn't seem to impact fitting; scipy's optimize function handles these cases fine.
- Now that I know how to enforce that arrays are contiguous, I might be able to achieve new performance gains for ICMR. Speed improvements are maybe not the top priority for the moment, though.
- I'm still missing a clear report on the consequences of certain manipulations, and haven't updated my documentation for ICMR. It looks like the activations function currently used by `echo`, for example, doesn't do the nonlinear trace coactivation thing that I thought was important. Instead, that only happens when computing outcome_probabilities. I need to figure out just how consequential these decisions are, and why, outside the context of my previous goal to equate CMR and ICMR.
- Still need to confirm parameter configurations impact model behavior in corresponding ways


## CMR Bugs
Model arrays weren't contiguous, slowing down performance. This is resolved.

In Jit-compiled mode, kernel crashed during fitting instead of returning any error. This is found to be a behavior of numba; if it happens I should re-run code without jit compilation and will see useful error messages.

CMR didn't properly reset model state when a participant recalled the same number of items as the number of columns in the trials matrix. This is resolved.

CMR was assigning 0 likelihood to some events. This maybe requires consultation with Sean.


### 0 Likelihood Bug
```
> <ipython-input-3-bcf9f4aa7c0a>(50)cmr_likelihood()
     48                 breakpoint()
     49             likelihood[trial_index, recall_index] = \
---> 50                 model.outcome_probabilities(model.context)[recall]
     51             model.force_recall(recall)
     52 

ipdb>  model.outcome_probabilities(model.context)
array([1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0.])
ipdb>  trial
array([20, 19, 13, 18,  1,  9,  2, 17, 16,  0,  0,  0,  0,  0,  0],
      dtype=int64)
ipdb>  model.recall_total
1
ipdb>  model.recall
array([19.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
        0.,  0.,  0.,  0.,  0.,  0.,  0.])
ipdb>  item_count, encoding_drift_rate,                  start_drift_rate, recall_drift_rate, shared_support,                 item_support, learning_rate, primacy_scale,                  primacy_decay, stop_probability_scale,                  stop_probability_growth, choice_sensitivity
(20, 0.38942959881318856, 0.41252879236305146, 0.4300931311051954, 0.14274861840233005, 0.9781461659126326, 0.3372547059124553, 27.185671961036313, 27.58460709050587, 0.7499792332092385, 9.27414887022105, 6.6403421922173305)
```

Here, it looks like the model is only assigning any probability to the stop event. Is the stop probability parameter too high? If the model works for other parameter configurations, that might be it.

So the problem is that outcome probabilities of zero can be assigned to events as long as stop probability is over 1? That does seem to be a problem in principle, and does seem consistent with model simulations otherwise looking okay. But why did we never have this problem before?

In truth, it looks like the model should already avoid zero probability events.

In outcome probabilities, stop probability is always at most 1.0. Later, 1 - stop_probability constraints how high other probabilities can be; if stop probability is 1, they are all set to 0. It's tough to avoid this without deviating from the model specification. There are maybe special parameter bounds I can set? No, not really.

In Morton and Polyn (2016), P(stop, j) can scale over 1.0. 

```python
import numpy as np

# proof that stop probability scaling explains the bug I'm seeing
stop_probability_scale, stop_probability_growth = 0.7499792332092385, 9.27414887022105
for i in range(2):
    print(i)
    print(stop_probability_scale * np.exp(i * stop_probability_growth))
```

Automatically adding a minimum value to outcome probabilities is a stopgap, but I worry that it will hide bugs that I'm interested in. 0 likelihood events is usually a canary in the coalmine that I like to look out for. How can I know that the --


### Visualize Fit Bug
Even with zero likelihoods made impossible, there's a bug in visualize fits that prevents visualizing the discovereed parameter configuration.

```python
from instance_cmr.model_analysis import *
from instance_cmr.models import *
```

```python
temporal_organization_analyses(CMR(20, 3.79838528e-01, 2.22044605e-16, 6.49176081e-01, 2.01786897e-01,
       1.00000000e+00, 2.67706889e-01, 2.05590470e+00, 7.39730822e-01,
       2.22044605e-16, 2.22044605e-16, 9.86183814e+00), 100)
```

Even on the old version of the model, the kernel dies with these parameters. Must exit njit mode and debug.

This is actually the main bug that made me care about 0 likelihood events. It could be that differential evolution proceeds fine with some np.nan parameters.

Without njit, I get the following bug:

```
<ipython-input-2-74c5a6c2b4f3>:161: RuntimeWarning: invalid value encountered in true_divide
  self.probabilities[1:] = (1-self.probabilities[0]) * activation / np.sum(activation)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-6-2fdc12a2ff03> in <module>
----> 1 temporal_organization_analyses(CMR(20, 3.79838528e-01, 2.22044605e-16, 6.49176081e-01, 2.01786897e-01,
      2        1.00000000e+00, 2.67706889e-01, 2.05590470e+00, 7.39730822e-01,
      3        2.22044605e-16, 2.22044605e-16, 9.86183814e+00), 100)

c:\users\gunnj\google drive\instance_cmr\instance_cmr\model_analysis.py in temporal_organization_analyses(model, experiment_count, savefig, figsize, first_recall_item)
    243         if first_recall_item is not None:
    244             model.force_recall(first_recall_item)
--> 245         data += [[experiment, 0, 'recall', i + 1, o] for i, o in enumerate(model.free_recall())]
    246     data = pd.DataFrame(data, columns=['subject', 'list', 'trial_type', 'position', 'item'])
    247     merged = fr.merge_free_recall(data)

<ipython-input-2-74c5a6c2b4f3> in free_recall(self, steps)
    198                 self.context = self.preretrieval_context
    199                 break
--> 200             self.recall[self.recall_total] = choice - 1
    201             self.recall_total += 1
    202             self.update_context(self.recall_drift_rate, self.items[choice - 1])

IndexError: index 20 is out of bounds for axis 0 with size 20
```

But yeah this bug is prior to the zero probability bug I thought I had discovered.

Seems to be a result of the free recall function having no way to stop if stop_probability never scales to 1. Sure says a lot that fitting function would choose parameters with such low values; suggests that is broken, too.

For now, we add the relevant control. This makes clear that the main problem is that the fitting function is now bugged.


### Borked Fitting Function


Now the fitting function tends to find a fit where all items get recalled:

```python
visualize_fit(CMR, {**parameters, **{free_parameters[i]:result.x[i] for i in range(len(result.x))}}, 
        murd_events, 'subject == 1', experiment_count=1000, savefig=True)
```

 Interestingly, simulations of free recall seem to work okay, at least for our default parameters:

```python
temporal_organization_analyses(CMR(**hand_fit_parameters), 100)
```

What do I see?

The CRP is actually not bad. So the error function is appropriately punishing for something. 

I need to look at what happens when the data says something wasn't recalled - or, should I say, when the data says recalled stopped.

Yeah, that's the problem, and it actually goes a bit further than I first understood. Right now, my likelihood isn't updated when themodel says recall has stopped. 

Moving the break statement to after likelihood gets updated is one step to fixing this, but it misses the event where recall stops after recall of the 15th item. 

When len(trial) is less than item_count, and len(trial) equals the number of items recalled, we should also track the probability of stopping recall where recall_index == len(trial). 

This change shouldn't affect the single subject simulation; let's make sure this assumption holds.

Without the change, error is around 1082. With the change it's 1079. Not a big deal.

But this change should return an error because of the array size thing. Why don't I observe that for `cmr_likelihood(murd_trials, **hand_fit_parameters)`?

```
> <ipython-input-3-667e084147d5>(44)cmr_likelihood()
     42             if recall_index == len(trial) and len(trial) < item_count:
     43                 breakpoint()
---> 44                 recall = 0
     45             else:
     46                 recall = trial[recall_index]

ipdb>  n
> <ipython-input-3-667e084147d5>(50)cmr_likelihood()
     48             # store probability of and simulate recalling item with this index
     49             likelihood[trial_index, recall_index] = \
---> 50                 model.outcome_probabilities(model.context)[recall]
     51 
     52             if recall == 0:

ipdb>  trial
array([16, 17, 18, 19, 11, 12, 15, 13,  1,  2,  3,  8,  7,  9, 10],
      dtype=int64)
ipdb>  n
> <ipython-input-3-667e084147d5>(49)cmr_likelihood()
     47 
     48             # store probability of and simulate recalling item with this index
---> 49             likelihood[trial_index, recall_index] = \
     50                 model.outcome_probabilities(model.context)[recall]
     51 

ipdb>  n
IndexError: index 15 is out of bounds for axis 1 with size 15
> <ipython-input-3-667e084147d5>(49)cmr_likelihood()
     47 
     48             # store probability of and simulate recalling item with this index
---> 49             likelihood[trial_index, recall_index] = \
     50                 model.outcome_probabilities(model.context)[recall]
     51 

ipdb>  likelihood[trial_index, recall_index]
*** IndexError: index 15 is out of bounds for axis 1 with size 15
```

It looks like something in my jit_compilation ignores the error. Even though running the code without njit returns this error, nothing happens when I run in njit mode. Pretty concerning for debugging. Must always test without njit before moving to compilation.

Anyway, likelihood should always have as many columns as there are items that can be recalled. This is a somewhat larger array by default, but shouldn't be a huge hit to fitting speeds, right?


### ICMR Bugs
These can be resolved similarly to the CMR bugs.

I need to remember to also take time to address that contiguous array problem. There are some performance/clarity issues associated with this that I'm sure I could give renewed attention to, but that's not the top priority for the moment. 

Right now, ICMR is about 6 times slower than CMR. It seems to obtain very similar fits, though. Single subject fits are very similar. (f is 1070.57 for CMR and 1066.62 for ICMR, and the "winner" seems to vary at each consideration.) And as for the full 20-item dataset? 21305 for ICMR vs 21224 for CMR. Hmm.




## ICMR Speed
ICMR still seems a lot slower than I remember, but maybe that was just a memory. 

Forcing arrays to be contiguous seems to speed up things a little. But moving the exponential to activations certainly slowed things down a bit (activations gets called a lot more often than outcome_probabilities!).

Let's try re-adding all the dot products I discarded. Doesn't actually seem to make a difference.

Magic number is: 22878.89038820426 for all subjects, 1186.8352381600062 for first

How much w/ dot product in echo? 9.66ms
Without? 9.49. Wow, really? Hmm.

When I swap out the first term in my activation function for a dot product, code gets to a clean 6.81ms. Clearly worth using numpy versions of functions where opportunity arises.
Without: 9.47
With: 7ms

What if I fit in a linalg.norm for the probe vector? 
With - 7.12
Without - 7

Linalg.norm doesn't seem worth it.

How about if I ditch np.power for something else?
Doesn't seem to be a huge difference. 

And if I go back to doing the exponential only in outcome_probabilities?
Down to 6.29 from what was 6.5-7.0. Half a millisecond basically. I'll go with the better fit.

Simulation would probably be faster if I didn't update context every time I started recall. Maybe I try to fix that later.

What about parallelization? It seems jitclass doesn't support the modifications I have in mind. But maybe my likelihood function does? Nah, somehow much slower.


## ICMR Alternative Implementations


Now I have to ask about the consequences of the various changes we discussed to the model.

First, let's see what happens if we put the exponential of activations inside the activation function instead of just inside outcome_probabilities.


### Our baseline fits are:
```
     fun: 1066.6198672539826
 message: 'Optimization terminated successfully.'
    nfev: 12411
     nit: 74
 success: True
       x: array([7.83057993e-01, 8.43579311e-03, 8.41344768e-01, 5.16132856e-03,
       9.28416235e-01, 1.90157671e-01, 1.00393775e+01, 3.25689988e+01,
       1.17197475e-02, 3.87954549e-01, 1.57952789e+00])
```
for one subject

```
     fun: 21305.459463112817
 message: 'Optimization terminated successfully.'
    nfev: 11256
     nit: 67
 success: True
       x: array([7.36326137e-01, 1.00379697e-01, 7.67841674e-01, 6.28420587e-03,
       6.64308038e-01, 1.13018109e-01, 4.42113403e+00, 5.71897928e+01,
       4.15564566e-02, 2.17469284e-01, 1.79295669e+00])
```
for all subjects


### If I move the exponential to affect encoding, too?

```
     fun: 1066.928495687557
 message: 'Optimization terminated successfully.'
    nfev: 17196
     nit: 103
 success: True
       x: array([8.36353524e-01, 8.13803889e-03, 7.85335816e-01, 3.90997688e-03,
       7.44171678e-01, 3.51124039e-01, 5.32479200e+00, 3.91069355e+01,
       1.85132603e-02, 3.35514090e-01, 1.45915070e+00])
```
for one subject

```
     fun: 21189.361909423762
     jac: array([  370.85883191,   395.01792365,  -284.3506067 , -4803.43042003,
          54.62388772,   182.5606888 ,   -16.67685875,     0.        ,
       -5460.87867314, -2637.80421076,   -19.46173154])
 message: 'Optimization terminated successfully.'
    nfev: 11199
     nit: 66
 success: True
       x: array([7.46510490e-01, 6.39097142e-02, 8.24181640e-01, 4.02289265e-03,
       5.34680153e-01, 2.72774711e-01, 4.47377578e+00, 4.97277656e+01,
       3.86851140e-02, 2.30541281e-01, 1.53490018e+00])
```
for all subjects

The fit is substantially better, even though the deviation from CMR is greater!


### Ditching Cosine Similarity
Any similarity function should do, right? No; cosine is special in clear ways. It's just the angle between two vectors, ignoring the magnitude. So this is the model? Except for the possibility of optimizing the likelihood function further or trying for a single-store representation, this is the model.

```python

```
