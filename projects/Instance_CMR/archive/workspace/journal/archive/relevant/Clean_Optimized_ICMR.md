Our initial successful implementation of ICMR with Numba is fast and correct and all, but its code is unmaintainable.
Here we try refactoring the implementation into a collection of functions and maybe even classes.

```python
from numba import jit, njit, float64, int32, int64, boolean
import numpy as np
from numba.experimental import jitclass
import math
```

```python
spec = [
    ('item_count', int32), 
    ('encoding_drift_rate', float64),
    ('start_drift_rate', float64),
    ('recall_drift_rate', float64),
    ('shared_support', float64),
    ('item_support', float64),
    ('learning_rate', float64),
    ('primacy_scale', float64),
    ('primacy_decay', float64),
    ('stop_probability_scale', float64),
    ('stop_probability_growth', float64),
    ('choice_sensitivity', float64),
    ('context', float64[:]),
    ('preretrieval_context', float64[:]),
    ('recall', float64[:]),
    ('retrieving', boolean),
    ('recall_total', int32),
    ('item_weighting', float64[:]),
    ('context_weighting', float64[:]),
    ('all_weighting', float64[:]),
    ('probabilities', float64[:]),
    ('memory', float64[:,:]),
    ('encoding_index', int32),
    ('items', float64[:,:])
]

@jitclass(spec)
class TestModel:
    
    """
    An instance-based implementation of the context maintenance and retrieval (CMR) model.

    InstanceCMR operates based on a combination of the context-based mechanisms of the CMR model (Morton and Polyn,
    2016) and the retrieval operations of the MINERVA 2 framework (Hintzman, 1984). In this framework, feature-based
    representations of studied items $F$ and a representation of current context $C$ interact over the course of a
    list-learning experiment. Item representations are feature vectors assumed to be orthonormal to each other: each
    index of $F$ corresponds to support for one particular item. Corresponding indices of the model's context
    representation $C$ similarly represent support for each item, but an additional index enables context to be set
    orthonormal to each relevant item representation as well.

    The two representations communicate with one another by being stored and retrieved together as memory traces in a
    global memory model, i.e. as a concatenated vector. When an item is presented during a list-learning experiment,
    it's assumed that the activated representation $r_i$ is a combination of the item's features $f_i$ and the temporal
    context of its presentation $c_i$. Memory for each experience is in turn encoded as a separate row in an $m$ by $n$
    memory matrix $M$ where rows correspond to memory traces (that is, experiences) and columns correspond to features, 

    $$M_i = r_i = (f_i, c_i)$$

    Attributes:  
    - memory: $M$, array of accumulated memory traces  
    - context: $C$, vector reflecting a recency-weighted average of encoded items  
    - retrieving: boolean switches between "encoding" and "retrieving" model state  
    - recall: vector whose nonzero entries track sequence of items recalled so far  
    - recall_total: integer count of items recalled so far  
    - item_count: $N$, integer count of unique items relevant to simulation  
    - encoding_drift_rate: ${\beta}_{enc}$, rate of context drift during item encoding  
    - start_drift_rate: ${\beta}_{start}$, amount of start-list context retrieved at start of recall
    - recall_drift_rate: ${\beta}_{rec}$, rate of context drift during recall
    - shared_support: ${\alpha}$, amount of support items initially have for one another
    - item_support: ${\delta}$, initial strength of the diagonal of pre-experimental contextual associations
    - learning_rate: ${\gamma}$, amount of experimental context retrieved by a recalled item
    - primacy_scale: ${\phi}_{s}$, scaling of primacy gradient on trace activations
    - primacy_decay: ${\phi}_{d}$, rate of decay of primacy gradient
    - choice_sensitivity: ${\tau}$, exponential weighting of similarity-driven activation
    - stop_probability_scale: ${\theta}_{s}$, scaling of the stop probability over output position
    - stop_probability_growth: ${\theta}_{r}$, rate of increase in stop probability over output position
    """
    
    def __init__(self, item_count, encoding_drift_rate, start_drift_rate, recall_drift_rate, shared_support,
                 item_support, learning_rate, primacy_scale, primacy_decay, stop_probability_scale,
                 stop_probability_growth, choice_sensitivity):
        """
        Initializes model instance with the specified parameter configuration.

        The content of memory traces are instantiated differently depending on whether representations reflect
        pre-experimental associations created at model instantiation or new associations learned during encoding. To set
        pre-experimental associations, a trace is encoded into memory for each relevant item. Each entry $j$ for each
        pre-experimental feature vector $f_i$ is set to have the effect of connecting each index on $F$ to the
        corresponding index on $C$ during retrieval from a partial or mixed cue. The $\gamma$ parameter controls the
        strength of these pre-experimental associations relative to experimental associations.

        Similarly to control pre-experimental context-to-item associations, entries for each pre-experimental context
        vector $c_i$ are set based on $\delta$ and $\alpha$. Here, $\delta$ works like $\gamma$ to connect indices on
        $C$ to the corresponding index on $F$ during retrieval from a partial or mixed cue. The $\alpha$ parameter
        alternatively allows all the items to support one another in the recall competition in a uniform manner.

        Before list-learning, context $C$ is initialized with a state orthogonal to the pre-experimental context
        associated with the set of items via the extra index that the representation vector has relative to items'
        feature vectors.
        """

        # store initial parameters
        self.item_count = item_count
        self.encoding_drift_rate = encoding_drift_rate
        self.start_drift_rate = start_drift_rate
        self.recall_drift_rate = recall_drift_rate
        self.shared_support = shared_support
        self.item_support = item_support
        self.learning_rate = learning_rate
        self.primacy_scale = primacy_scale
        self.primacy_decay = primacy_decay
        self.stop_probability_scale = stop_probability_scale
        self.stop_probability_growth = stop_probability_growth
        self.choice_sensitivity = choice_sensitivity
        
        # at the start of the list context is initialized with a state orthogonal to the pre-experimental context
        # associated with the set of items
        self.context = np.zeros(item_count + 1)
        self.context[0] = 1
        self.preretrieval_context = self.context
        self.recall = np.zeros(item_count) # recalls has at most `item_count` entries
        self.retrieving = False
        self.recall_total = 0

        # predefine activation weighting vectors
        self.item_weighting, self.context_weighting = np.ones(item_count*2), np.ones(item_count*2)
        self.item_weighting[item_count:] = learning_rate
        self.context_weighting[item_count:] = \
            primacy_scale * np.exp(-primacy_decay * np.arange(item_count)) + 1
        self.all_weighting = self.item_weighting * self.context_weighting

        # preallocate for outcome_probabilities
        self.probabilities = np.zeros((item_count + 1))

        # initialize memory
        # we now conceptualize it as a pairing of two stores Mfc and Mcf representing feature-to-context and
        # context-to-feature associations, respectively
        mfc = np.eye(item_count, item_count + 1, 1) * (1 - learning_rate)
        mcf = np.ones((item_count, item_count)) * shared_support
        for i in range(item_count):
            mcf[i, i] = item_support
        mcf = np.hstack((np.zeros((item_count, 1)), mcf))
        self.memory = np.zeros((item_count * 2, item_count * 2 + 2))
        self.memory[:item_count,] = np.hstack((mfc, mcf))
        self.encoding_index = item_count
        self.items = np.eye(item_count, item_count + 1, 1)
        
    def experience(self, experiences):
        """Adds new traces to model memory for each experience based on model state."""

        for i in range(len(experiences)):
            self.memory[self.encoding_index, :self.item_count+1] = experiences[i]
            self.update_context(self.encoding_drift_rate, self.memory[self.encoding_index])
            self.memory[self.encoding_index, self.item_count+1:] = self.context
            self.encoding_index += 1
            
    def update_context(self, drift_rate, experience=None):
        """Updates context based on drift rate and either initial context or specified experience"""

        # first pre-experimental or initial context is retrieved
        if experience is not None:
            context_input = self.echo(experience)[self.item_count + 1:]
            context_input = context_input / np.sqrt(np.sum(np.square(context_input))) # norm to length 1
        else:
            context_input = np.zeros((self.item_count+1))
            context_input[0] = 1

        # updated context is sum of context and input, modulated by rho to have len 1 and some drift_rate
        rho = np.sqrt(1 + np.square(drift_rate) * (np.square(self.context * context_input) - 1)) - (
                drift_rate * (self.context * context_input))
        self.context = (rho * self.context) + (drift_rate * context_input)
        
    def echo(self, probe):
        """
        A probe activates all traces in memory in parallel. The sum of these traces weighted by their activation is an
        `echo` summarizing the memory system's response to the probe.
        """

        return np.sum((self.memory[:self.encoding_index].T * self.activations(probe)).T, axis=0)
    
    def activations(self, probe):
        """
        Presents a cue to memory system, activating all traces in memory in parallel. Each trace's `activation` is a
        cubed function of its `similarity` to the probe, weighted based on item position and whether probe contains
        contextual or item features.
        """

        # computes and cubes similarity value to find activation for each trace in memory
        activation = np.sum(self.memory[:self.encoding_index] * probe, axis=1) / (
            np.sqrt(np.sum(np.square(self.memory[:self.encoding_index]), axis=1)) * np.sqrt(
                np.sum(np.square(probe))))
        activation = np.power(activation, self.choice_sensitivity)

        # weight activations based on whether probe contains item or contextual features or both
        if np.any(probe[:self.item_count + 1]):
                if np.any(probe[self.item_count + 1:]):
                    # both mfc and mcf weightings, see below
                    activation *= self.all_weighting[:self.encoding_index]
                else:
                    # mfc weightings - scale by gamma for each experimental trace
                    activation *= self.item_weighting[:self.encoding_index]
        else:
            # mcf weightings - scale by primacy/attention function given position of experimental experiences
            activation *= self.context_weighting[:self.encoding_index]

        return activation
    
    def outcome_probabilities(self, activations=None, cues=None):
        """
        Computes current item recall probabilities given model state and any specified activation pattern/cue.
        """

        # if no activations are provided, generate some from current context
        if activations is None:
            activations = self.activations(np.hstack((np.zeros(self.item_count + 1), self.context)))

        # temporarily update context to reflect cue(s)
        preretrieval_context = self.context
        if cues is not None:
            for cue in cues:
                self.update_context(cue, self.retrieval_drift_rate)

        self.probabilities = np.zeros((self.item_count + 1))
        self.probabilities[0] = min(self.stop_probability_scale * np.exp(
            self.recall_total * self.stop_probability_growth), 1.0)

        if self.probabilities[0] < 1:
            for trace_index in range(len(self.memory)):
                matched_item = trace_index if trace_index < self.item_count else trace_index-self.item_count
                if matched_item in self.recall[:self.recall_total]:
                    continue
                self.probabilities[matched_item + 1] += activations[trace_index]
            self.probabilities[1:] *= (
                1 - self.probabilities[0]) / np.sum(self.probabilities[1:])

        self.context = preretrieval_context
        return self.probabilities
    
    def free_recall(self, steps=None):
        """Simulates free recall for the specified number of steps based on model state."""

        # some amount of the pre-list context is reinstated before initiating recall
        if not self.retrieving:
            self.recall = np.zeros(self.item_count)
            self.recall_total = 0
            self.preretrieval_context = self.context
            self.update_context(self.start_drift_rate)
            self.retrieving = True
            
        # number of items to retrieve is infinite if steps is unspecified
        if steps is None:
            #TODO
            steps = math.inf
        steps = len(self.recall) + steps

        # at each recall attempt
        while len(self.recall) < steps:

            # the current state of context is used as a retrieval cue to attempt recall of a studied item
            activations = self.activations(np.hstack((np.zeros(self.item_count + 1), self.context)))

            # compute outcome probabilities and make choice based on distribution
            outcome_probabilities = self.outcome_probabilities(activations)
            if np.any(outcome_probabilities[1:]):
                #TODO
                choice = np.random.choice(len(outcome_probabilities), p=outcome_probabilities)
            else:
                choice = 0

            # resolve and maybe store outcome
            # we stop recall if no choice is made (0)
            if choice == 0:
                self.retrieving = False
                self.context = self.preretrieval_context
                break
            self.recall[self.recall_total] = choice - 1
            self.recall_total += 1
            self.update_context(self.recall_drift_rate,
                                np.hstack((self.items[choice - 1], np.zeros(self.item_count + 1))))
        return self.recall[:self.recall_total]
    
    def force_recall(self, choice=None):
        """
        Forces model to recall chosen item and update context regardless of current model state.

        Here, recall items are 1-indexed, with a choice of 0 indicating a choice to end retrieval and return to
        preretrieval context.
        """
        if not self.retrieving:
            self.recall = np.zeros(self.item_count)
            self.recall_total = 0
            self.preretrieval_context = self.context
            self.update_context(self.start_drift_rate)
            self.retrieving = True

        if choice is None:
            pass
        elif choice == 0:
            self.retrieving = False
            self.context = self.preretrieval_context
        else:
            self.recall[self.recall_total] = choice - 1
            self.recall_total += 1
            self.update_context(self.recall_drift_rate,
                                np.hstack((self.items[choice - 1], np.zeros(self.item_count + 1))))
        return self.recall[:self.recall_total]
    
    def compare_probes(self, first_probe, second_probe):
        """
        Compute the resemblance (cosine similarity) between the echoes associated with first_probe and
        second_probe
        """
        echoes = self.echo(first_probe), self.echo(second_probe)
        return np.sum(echoes[0] * echoes[1]) / (np.sqrt(
                np.sum(np.square(echoes[0]))) * np.sqrt(
                np.sum(np.square(echoes[1]))))
```

# Testing
We need to confirm that it produces the same outputs as ICMR even across functions not covered by `data_likelihood`.
We also want to confirm that speed improvements from the functional implementation of our numba-based optimization of
ICMR are largely preserved.

Following previous conventions for timing JIT-compiled code, we'll do an example execution that should take longer to
run due to compilation, and then we'll execute our timing magic.

```python
from instance_cmr.model_analysis import prepare_murddata, data_likelihood

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

data_likelihood(TestModel, parameters, murd_trials[:60])
```

Returns 1154.6050515722663, consistent with our original cost function.

```python
%timeit data_likelihood(TestModel, parameters, murd_trials[:60])
```

Returns 13.5 ms +/- 169 $\mu$s per loop (mean +/- std. dev. of 7 runs, 100 loops each). That's faster than the
pre-numba implementation of the cost function, but about 3ms slower than our purely functional implementation of the
numba optimization. This is presumably because our `data_likelihood` function is not itself optimized. Let's try that
now.

```python
@njit(fastmath=True, nogil=True)
def test_data_likelihood(trials, item_count, encoding_drift_rate, 
                         start_drift_rate, recall_drift_rate, shared_support,
                         item_support, learning_rate, primacy_scale, 
                         primacy_decay, stop_probability_scale, 
                         stop_probability_growth, choice_sensitivity):
    
    model = TestModel(item_count, encoding_drift_rate, 
                      start_drift_rate, recall_drift_rate, shared_support,
                      item_support, learning_rate, primacy_scale, 
                      primacy_decay, stop_probability_scale, 
                      stop_probability_growth, choice_sensitivity)
    
    model.experience(np.eye(item_count, item_count + 1, 1))
    
    likelihood = np.ones(np.shape(trials))
    
    for trial_index in range(len(trials)):
        trial = trials[trial_index]
        
        model.force_recall()
        for recall_index in range(len(trial)):
            recall = trial[recall_index]
            likelihood[trial_index, recall_index] = \
                model.outcome_probabilities()[recall]
            model.force_recall(recall)
            if recall == 0:
                break
        
    return -np.sum(np.log(likelihood))
```

```python
test_data_likelihood(murd_trials[:60], **parameters)
```

```python
%timeit test_data_likelihood(murd_trials[:60], **parameters)
```

This returns 11.2 ms +/- 224 microseconds per loop, which is even more excellent.

We'll use this as our main implementation of InstanceCMR and data_likelihood, especially since the model is rarely
simulated just once.
