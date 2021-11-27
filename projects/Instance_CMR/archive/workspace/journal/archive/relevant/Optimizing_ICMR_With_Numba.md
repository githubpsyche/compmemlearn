# Optimizing ICMR With Numba


To hopefully make fitting faster, we'll use `numba` to make an even faster version of ICMR that supports
model fitting. 


## Initial Attempt
Since numba's class support is at an early stage, this will be tricky. To get around that problem, we'll
convert each step of `data_likelihood` to avoid using ICMR as a class, instead realizing ICMR as a function.
It's hardly maintainable code, however, and needs to be refactored into a set of functions and even ideally
an optimized ICMR class. But to start, we'll at least ensure the function is correct (returns the same costs
as our original `data_likelihood` function for the same inputs) and fast enough to justify the effort.

```python
from numba import jit, njit, float64, int32, int64
import numpy as np

@njit(float64(int64[:,:], int32, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64), nogil=True, fastmath=True)
def data_likelihood(trials, item_count, encoding_drift_rate, start_drift_rate, 
                    recall_drift_rate, shared_support, item_support, 
                    learning_rate, primacy_scale, primacy_decay, 
                    stop_probability_scale, stop_probability_growth, 
                    choice_sensitivity):
    
    ### model initialization
    # at the start of the list context is initialized with a state orthogonal to the pre-experimental context
    # associated with the set of items
    context = np.zeros(item_count + 1)
    context[0] = 1
    preretrieval_context = context
    recall = np.zeros(item_count) # recalls has at most `item_count` entries
    state = 'encoding'
    recall_total = 0

    # predefine activation weighting vectors
    item_weighting, context_weighting = np.ones(item_count*2), np.ones(item_count*2)
    item_weighting[item_count:] = learning_rate
    context_weighting[item_count:] = \
        primacy_scale * np.exp(-primacy_decay * np.arange(item_count)) + 1
    all_weighting = item_weighting * context_weighting

    # preallocate for outcome_probabilities
    probabilities = np.zeros((item_count + 1))

    # initialize memory
    # we now conceptualize it as a pairing of two stores Mfc and Mcf representing feature-to-context and
    # context-to-feature associations, respectively
    mfc = np.eye(item_count, item_count + 1, 1) * (1 - learning_rate)
    mcf = np.ones((item_count, item_count)) * shared_support
    for i in range(item_count):
        mcf[i, i] = item_support
    mcf = np.hstack((np.zeros((item_count, 1)), mcf))
    memory = np.zeros((item_count * 2, item_count * 2 + 2))
    memory[:item_count,] = np.hstack((mfc, mcf))
    encoding_index = item_count
    items = np.eye(item_count, item_count + 1, 1)
    
    ###
    
    ### experiencing items
    experiences = np.eye(N=item_count, M=item_count+1, k=1)
    
    for i in range(len(experiences)):
        memory[encoding_index, :item_count+1] = experiences[i]
        
        ##### updating context
        experience = memory[encoding_index]
        drift_rate = encoding_drift_rate

        ####### generating an echo
        probe = experience

        ######### computing activations
        # computes and cubes similarity value to find activation for each trace in memory
        activation = np.sum(memory[:encoding_index] * probe, axis=1) / (
            np.sqrt(np.sum(np.square(memory[:encoding_index]), axis=1)) * np.sqrt(np.sum(np.square(probe))))
        activation = np.power(activation, choice_sensitivity)

        # weight activations based on whether probe contains item or contextual features or both
        if np.any(probe[:item_count + 1]):
                if np.any(probe[item_count + 1:]):
                    # both mfc and mcf weightings, see below
                    activation *= all_weighting[:encoding_index]
                else:
                    # mfc weightings - scale by gamma for each experimental trace
                    activation *= item_weighting[:encoding_index]
        else:
            # mcf weightings - scale by primacy/attention function given position of experimental experiences
            activation *= context_weighting[:encoding_index]

        #########

        echo = np.sum((memory[:encoding_index].T * activation).T, axis=0)

        #######

        context_input = echo[item_count + 1:]
        context_input = context_input / np.sqrt(np.sum(np.square(context_input)))
        
        # updated context is sum of context and input, modulated by rho to have len 1 and some drift_rate
        rho = np.sqrt(1 + np.square(drift_rate) * (np.square(context * context_input) - 1)) - (
                drift_rate * (context * context_input))
        context = (rho * context) + (drift_rate * context_input)
        
        #####
        
        memory[encoding_index, item_count+1:] = context
        encoding_index += 1
        
    ###
        
    likelihood = np.ones(np.shape(trials))
    
    for trial_index in range(len(trials)):
        trial = trials[trial_index]
        
        ### force recall with no argument
        recall = np.zeros(item_count)
        recall_total = 0
        preretrieval_context = context

        ##### update context using start_drift_rate
        experience = None
        drift_rate = start_drift_rate
        
        context_input = np.zeros((item_count+1))
        context_input[0] = 1

        # updated context is sum of context and input, modulated by rho to have len 1 and some drift_rate
        rho = np.sqrt(1 + np.square(drift_rate) * (np.square(context * context_input) - 1)) - (
                drift_rate * (context * context_input))
        context = (rho * context) + (drift_rate * context_input)

        #####

        state = 'retrieving'
            
        ###
        
        for recall_index in range(len(trial)):
            _recall = trial[recall_index]
            
            ### outcome probabilities with no argument
            activations = None
            cues = None
            
            ##### computing activations
            probe = np.hstack((np.zeros(item_count + 1), context))

            # computes and cubes similarity value to find activation for each trace in memory
            activation = np.sum(memory[:encoding_index] * probe, axis=1) / (
                np.sqrt(np.sum(np.square(memory[:encoding_index]), axis=1)) * np.sqrt(np.sum(np.square(probe))))
            activation = np.power(activation, choice_sensitivity)

            # weight activations based on whether probe contains item or contextual features or both
            if np.any(probe[:item_count + 1]):
                    if np.any(probe[item_count + 1:]):
                        # both mfc and mcf weightings, see below
                        activation *= all_weighting[:encoding_index]
                    else:
                        # mfc weightings - scale by gamma for each experimental trace
                        activation *= item_weighting[:encoding_index]
            else:
                # mcf weightings - scale by primacy/attention function given position of experimental experiences
                activation *= context_weighting[:encoding_index]

            #####
            
            activations = activation
                
            probabilities = np.zeros((item_count + 1))
            probabilities[0] = min(stop_probability_scale * np.exp(
                recall_total * stop_probability_growth), 1.0)
            
            if probabilities[0] < 1:
                for trace_index in range(len(memory)):
                    matched_item = trace_index if trace_index < item_count else trace_index-item_count
                    if matched_item in recall[:recall_total]:
                        continue
                    probabilities[matched_item + 1] += activations[trace_index]
                probabilities[1:] *= (
                    1 - probabilities[0]) / np.sum(probabilities[1:])
                
            ###
            
            likelihood[trial_index, recall_index] = probabilities[_recall]
            
            ### force recall with argument _recall
            choice = _recall
                
            if choice == 0:
                state = 'encoding'
                context = preretrieval_context
            else:
                recall[recall_total] = choice - 1
                recall_total += 1
                
                ##### update context
                experience = np.hstack((items[choice - 1], np.zeros(item_count + 1)))
                drift_rate = recall_drift_rate
                
                ####### generating an echo
                probe = experience

                ######### computing activations
                # computes and cubes similarity value to find activation for each trace in memory
                activation = np.sum(memory[:encoding_index] * probe, axis=1) / (np.sqrt(
                    np.sum(np.square(memory[:encoding_index]), axis=1)) * np.sqrt(np.sum(np.square(probe))))
                activation = np.power(activation, choice_sensitivity)

                # weight activations based on whether probe contains item or contextual features or both
                if np.any(probe[:item_count + 1]):
                        if np.any(probe[item_count + 1:]):
                            # both mfc and mcf weightings, see below
                            activation *= all_weighting[:encoding_index]
                        else:
                            # mfc weightings - scale by gamma for each experimental trace
                            activation *= item_weighting[:encoding_index]
                else:
                    # mcf weightings - scale by primacy/attention function given position of experimental
                    # experiences
                    activation *= context_weighting[:encoding_index]

                #########

                echo = np.sum((memory[:encoding_index].T * activation).T, axis=0)

                #######

                context_input = echo[item_count + 1:]
                context_input = context_input / np.sqrt(np.sum(np.square(context_input)))

                # updated context is sum of context and input, modulated by rho to have len 1 and some drift_rate
                rho = np.sqrt(1 + np.square(drift_rate) * (np.square(context * context_input) - 1)) - (
                        drift_rate * (context * context_input))
                context = (rho * context) + (drift_rate * context_input)

                #####
            
            ###
                
            if _recall == 0:
                break
        
    return -np.sum(np.log(likelihood))
```

Performance gains from `numba` are achieved through a just-in-time compilation, so the first execution will
take much longer than the others. Let's take the opportunity to confirm that the model returns the same cost
estimate for our typical parameters.

```python
from instance_cmr.model_analysis import prepare_murddata

murd_trials, murd_events, murd_length = prepare_murddata('data/MurdData_clean.mat', 0)

lb = np.finfo(float).eps
parameters = {
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

trials = murd_trials[:60]
data_likelihood(trials, **parameters)
```

Now let's time the usual runtime of the function.

```python
%timeit data_likelihood(trials, **parameters)
```

We return atiming of 9.43 ms +/- 165 $\mu$s per loop (mean +/- std. dev. of 7 runs, 100 loops each). 

Is that good or bad? To find out, we have to compare to our original function. First we'll show it returns
the same cost estimate as the implementation above:

```python
from instance_cmr.models import InstanceCMR
from instance_cmr.model_analysis import data_likelihood as classic_data_likelihood

classic_data_likelihood(InstanceCMR, parameters, trials)
```

Then we'll generate parallel timings:

```python
%timeit classic_data_likelihood(InstanceCMR, parameters, trials)
```

The result is `175 ms +/- 4.04 ms per loop (mean +/- std. dev. of 7 runs, 1 loop each)`.

This means our numba implementation is currently around 18 times faster than that associated with our
FastDualStore ICMR implementation.
