# Model Debugging
For some parameters, ICMR seems to complain. I need to understand the range of parameter values where ICMR does not throw errors so I can set appropriate bounds and be sure there are no bugs in its implementation. To do that, I'll probably reproduce much of the code in the Dual Store Prototype but focus examination and reflection on behavior at borderline parameters.


## Implementation
Obviously we start with a selected model implementation. We'll modify this cell as we discover stuff that can be improved.

```python
import math
import numpy as np
from scipy import spatial
from numpy.linalg import norm


class InstanceCMR(object):
    """The context maintenance and retrieval model re-imagined as an exemplar model.
    
    Attributes:
        memory: array where rows/columns correspond to accumulated memory traces and feature dims respectively
        context: vector reflecting a recency-weighted average of recently presented stimuli information
        item_count: number of unique items relevant to model simulation
        encoding_drift_rate: rate of context drift during item processing
        start_drift_rate: amount of start-list context retrieved at start of recall
        recall_drift_rate: rate of context drift during recall
        shared_support: uniform amount of support items initially have for one another in recall competition
        item_support: initial strength of the diagonal of Mcf
        learning_rate: contribution of experimental relative to pre-experimental associations
        primacy_scale: scaling of primacy gradient in learning rate on Mcf
        primacy_decay: rate of decay of primacy gradient
        semantic_scale: scaling of semantic association strengths
        stop_probability_scale: scaling of the stop probability over output position
        stop_probability_growth: rate of increase in stop probability
        choice_sensitivity: sensitivity parameter of the Luce choice rule
    """

    def __init__(self, item_count, encoding_drift_rate, start_drift_rate, recall_drift_rate, shared_support,
                 item_support, learning_rate, primacy_scale, primacy_decay, stop_probability_scale,
                 stop_probability_growth, choice_sensitivity):
        """Start exemplar model with an initial set of pre-experimental associations in memory
        
        Args:
            item_count: number of unique items relevant to model simulation
            encoding_drift_rate: rate of context drift during item processing
            start_drift_rate: amount of start-list context retrieved at start of recall
            recall_drift_rate: rate of context drift during recall
            shared_support: uniform support items initially have for one another in recall competition
            item_support: initial strength of the diagonal of Mcf
            learning_rate: contribution of experimental relative to pre-experimental associations
            primacy_scale: scaling of primacy gradient in learning rate on Mcf
            primacy_decay: rate of decay of primacy gradient
            semantic_scale: scaling of semantic association strengths
            stop_probability_scale: scaling of the stop probability over output position
            stop_probability_growth: rate of increase in stop probability
            choice_sensitivity: sensitivity parameter of the Luce choice rule
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
        # self.semantic_scale = semantic_scale
        self.stop_probability_scale = stop_probability_scale
        self.stop_probability_growth = stop_probability_growth
        self.choice_sensitivity = choice_sensitivity

        # at the start of the list context is initialized with a state
        # orthogonal to the pre-experimental context associated with the set of items
        self.context = np.eye(1, item_count + 1).flatten()
        self.preretrieval_context = self.context
        self.state = 'encoding'
        self.recall = []

        # initialize memory
        # we now conceptualize it as a pairing of two stores Mfc and Mcf
        # representing feature-to-context and context-to-feature associations, respectively
        mfc = np.eye(item_count, item_count + 1, 1) * (1 - self.learning_rate)
        mcf = np.eye(item_count) * self.item_support
        mcf[np.logical_not(np.eye(item_count, dtype=bool))] = self.shared_support
        mcf = np.hstack((np.zeros((item_count, 1)), mcf))
        self.memory = np.hstack((mfc, mcf))

        # an additional item store and KDTree organizes response selection based on retrieved F
        self.items = np.eye(self.item_count, self.item_count + 1, 1)
        self.item_decision_rule = spatial.KDTree(self.items)

    def experience(self, experiences):
        """"Adds new trace(s) to model memory based on an experienced vector of item features 
            and current context."""
        if len(np.shape(experiences)) == 1:
            experiences = [experiences]
        for experience in experiences:
            self.update_context(self.encoding_drift_rate, np.hstack((np.array(experience), np.zeros((self.item_count + 1)))))
            trace = np.hstack((experience, self.context))
            self.memory = np.vstack((self.memory, trace))

    def update_context(self, drift_rate, experience=None):
        """Updates contextual representation based on content of current experience or, 
        if no experience is presented, on the content of initial context."""

        # first pre-experimental or initial context is retrieved
        if experience is not None:
            context_input = self.echo(experience)[self.item_count + 1:]
            context_input = context_input / norm(context_input)  # normalized to have length 1
        else:
            context_input = np.eye(1, self.item_count + 1).flatten()

        # updated context is sum of context and input, modulated by rho to have len 1 and some drift_rate
        rho = np.sqrt(1 + (drift_rate ** 2) * (((self.context * context_input) ** 2) - 1)) - (
                drift_rate * (self.context * context_input))
        self.context = (rho * self.context) + (drift_rate * context_input)

    def echo(self, probe):
        """A probe activates all traces in memory in parallel. The sum of these traces weighted by their 
        activation is an `echo` summarizing the memory system's response to the probe."""
        return np.sum((self.memory.T * self.activations(probe)).T, axis=0)

    def compare_probes(self, first_probe, second_probe):
        """Compute the resemblance (cosine similarity) between the echoes associated with probes A and B."""
        echoes = self.echo(first_probe), self.echo(second_probe)
        return np.sum(echoes[0] * echoes[1]) / (norm(echoes[0]) * norm(echoes[1]))

    def activations(self, probe):
        """Presents a cue to memory system, activating all traces in memory in parallel. Each trace's 
        `activation` is a cubed function of its `similarity` to the probe, weighted based on item position and 
        whether probe contains contextual or item features."""
        # computes and cubes similarity value to find activation for each trace in memory
        activation = np.sum(self.memory * probe, axis=1) / (norm(self.memory, axis=1) * norm(probe))
        activation = activation ** self.choice_sensitivity

        # determining weighting based on whether probe contains item or contextual features
        # mfc weightings - scale by gamma for each experimental trace
        weighting = np.ones(len(self.memory))
        if np.sum(probe[:self.item_count + 1]) != 0:
            weighting[self.item_count:] = self.learning_rate

        # mcf weightings - scale by primacy/attention function based on position of experimental experiences
        if np.sum(probe[self.item_count + 1:]) != 0:
            weighting[self.item_count:] *= self.primacy_scale * np.exp(
                -self.primacy_decay * np.arange(len(self.memory) - self.item_count)) + 1

        # weights traces based on provided scalings
        activation *= weighting
        return activation

    def outcome_probabilities(self, activations=None, cues=None):
        """Computes recall probability of each item given current model state and optional activation pattern/cue."""

        # if no activations are provided, generate some from current context
        if activations is None:
            activations = self.activations(np.hstack((np.zeros(self.item_count + 1), self.context)))

        # temporarily update context to reflect cue(s)
        preretrieval_context = self.context
        if cues is not None:
            for cue in cues:
                self.update_context(cue, self.retrieval_drift_rate)

        outcome_probabilities = np.zeros((self.item_count + 1))
        outcome_probabilities[0] = min(self.stop_probability_scale * np.exp(
            len(self.recall) * self.stop_probability_growth), 1.0)

        if outcome_probabilities[0] < 1:
            for trace_index, trace in enumerate(self.memory.tolist()):
                j = self.item_decision_rule.query(trace[:self.item_count + 1])[1]
                if j in self.recall:
                    continue
                outcome_probabilities[j + 1] += activations[trace_index]
            outcome_probabilities[1:] *= (1 - outcome_probabilities[0]) / np.sum(outcome_probabilities[1:])

        self.context = preretrieval_context
        return outcome_probabilities

    def force_recall(self, choice):
        """Forces model to recall chosen item and update context regardless of current model state.

        Here, recall items are 1-indexed, with a choice of 0 indicating a choice to end retrieval
        and return to preretrieval context.
        """
        if self.state == 'encoding':
            self.recall = []
            self.preretrieval_context = self.context
            self.update_context(self.start_drift_rate)
            self.state = 'retrieving'
        if choice == 0:
            self.state = 'encoding'
            self.context = self.preretrieval_context
        else:
            self.recall.append(choice - 1)
            self.update_context(self.recall_drift_rate,
                                np.hstack((self.items[choice - 1], np.zeros(self.item_count + 1))))
        return self.recall

    def free_recall(self, steps=None):
        """Simulates performance on a free recall task based on experienced items.

        We initialize context similar to eq. 16 from Morton & Polyn (2016), simulating end-of-list distraction
        and some amount of pre-list context reinstatement. This context is used as a retrieval cue (probe) to 
        attempt retrieval of a studied item, generating an associated memory echo.

        At each recall attempt, we also calculate a probability of stopping recall as a function of output 
        position according to eq. 18 of Morton & Polyn (2016). The probability of recalling a given item 
        conditioned on not stopping recall is defined on the basis of the item's similarity to the current 
        contextual representation according to a formula similar to eq 19 of Morton and Polyn (2016).
        """
        # number of items to retrieve is infinite if steps is unspecified
        if steps is None:
            steps = math.inf
        steps = len(self.recall) + steps

        # some amount of the pre-list context is reinstated before initiating recall
        if self.state == 'encoding':
            self.recall = []
            self.preretrieval_context = self.context
            self.update_context(self.start_drift_rate)
            self.state = 'retrieving'

        # at each recall attempt
        while len(self.recall) < steps:

            # the current state of context is used as a retrieval cue to attempt recall of a studied item
            activations = self.activations(np.hstack((np.zeros(self.item_count + 1), self.context)))

            # compute outcome probabilities and make choice based on distribution
            outcome_probabilities = self.outcome_probabilities(activations)
            choice = np.random.choice(len(outcome_probabilities), p=outcome_probabilities)

            # resolve and maybe store outcome
            # we stop recall if no choice is made
            if not choice:
                self.state = 'encoding'
                self.context = self.preretrieval_context
                break
            self.recall.append(choice - 1)
            self.update_context(self.recall_drift_rate,
                                np.hstack((self.items[choice - 1], np.zeros(self.item_count + 1))))

        return self.recall
```

## Model Simulation
Next we need some code for simulating the model with arbitrary parameters. The following cell instantiates the model. Deciding what should be done re: recall trials is probably a separate matter. The whole while, let's track pertinent aspects of model state.


## Instantiation
Passing parameters into model, defining pre-experimental associations.

Pretty solid parameters:
```
parameters = {
    'item_count': 20,
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
```

```python
lb = np.finfo(np.float64).tiny
parameters = {
    'item_count': 20,
    'encoding_drift_rate': .8,
    'start_drift_rate': .7,
    'recall_drift_rate': .8,
    'shared_support': 0,
    'item_support': 1,
    'learning_rate': .99,
    'primacy_scale': 1.0,
    'primacy_decay': 1.0,
    'stop_probability_scale': .01,
    'stop_probability_growth': .3,
    'choice_sensitivity': 5
}

parameters = {'item_count': 20, 'encoding_drift_rate': 1.0, 
              'start_drift_rate': 0, 
              'recall_drift_rate': 0, 'shared_support': 0.1, 
              'item_support':0, 'learning_rate': 0.99, 'primacy_scale': 5.0, 
              'primacy_decay': 3, 'stop_probability_scale': 1.0, 
              'stop_probability_growth': 1.0, 'choice_sensitivity': 0}


first_recall_item = None
item_count = parameters['item_count']

model = InstanceCMR(**parameters)
```

## Encoding
Model states throughout encoding.

```python
experiences = np.eye(parameters['item_count'], parameters['item_count'] + 1, 1)
encoding_contexts, encoding_supports = model.context, []

# track model state across experiences
for i in range(len(experiences)):
    model.experience(experiences[i])

    # track model contexts and item supports
    encoding_contexts = np.vstack((encoding_contexts, model.context))
    activations = model.activations(np.hstack((np.zeros(model.item_count + 1), model.context)))

    if len(encoding_supports) > 0:
        encoding_supports = np.vstack((encoding_supports, model.outcome_probabilities(activations)))
    else:
        encoding_supports = model.outcome_probabilities(activations)
```

### Encoding Contexts
Plotting the model's `context` representation at each update (e.g. when something new is experienced/encoded).

```python
import matplotlib.pyplot as plt
import seaborn as sns

# visualize outcomes
# encoding contexts
plt.figure(figsize=(15, 15))
sns.heatmap(encoding_contexts, annot=True, linewidths=.5)
plt.title('Encoding Contexts')
plt.xlabel('Feature Index')
plt.ylabel('Update Index')
plt.show()
print(norm(encoding_contexts, axis=1))
```

### Encoding Supports
Plotting support in memory for recall of each item at each increment of encoding.

```python
# encoding supports
plt.figure(figsize=(15, 15))
sns.heatmap(encoding_supports, annot=True, linewidths=.5)
plt.title('Supports For Each Item At Each Increment of Encoding')
plt.xlabel('Amount of Support')
plt.ylabel('Update Index')
plt.show()
```

## Retrieval
Tracking model state across each step of retrieval. Since it's stochastic, these values change with each iteration (unless I set a particular random seed...)


### Re-initialize model

```python
# initialization
retrieval_contexts, retrieval_supports = model.context, model.outcome_probabilities()

# re-instantiate the model
model = InstanceCMR(**parameters)
experiences = np.eye(parameters['item_count'], parameters['item_count'] + 1, 1)
encoding_contexts, encoding_supports = model.context, []

# track model state across experiences
for i in range(len(experiences)):
    model.experience(experiences[i])

    # track model contexts and item supports
    encoding_contexts = np.vstack((encoding_contexts, model.context))
    activations = model.activations(np.hstack((np.zeros(model.item_count + 1), model.context)))

    if len(encoding_supports) > 0:
        encoding_supports = np.vstack((encoding_supports, model.outcome_probabilities(activations)))
    else:
        encoding_supports = model.outcome_probabilities(activations)
```

### Actual Retrieval
Includes pre-retrieval distraction and execution of optional forced first recall. Prints recall train associated with this particular simulation.

```python
# pre-retrieval distraction
model.free_recall(0)
retrieval_contexts = np.vstack((retrieval_contexts, model.context))
retrieval_supports = np.vstack((retrieval_supports, model.outcome_probabilities()))

# optional forced first item recall
if first_recall_item is not None:
    model.force_recall(first_recall_item)
    retrieval_contexts = np.vstack((retrieval_contexts, model.context))
    retrieval_supports = np.vstack((retrieval_supports, model.outcome_probabilities()))

# actual recall
while model.state != 'encoding':
    recall = model.free_recall(1)
    retrieval_contexts = np.vstack((retrieval_contexts, model.context))
    retrieval_supports = np.vstack((retrieval_supports, model.outcome_probabilities()))

# print recall train associated with this simulation
print(recall)
```

### Retrieval Contexts
Context representation over course of retrieval.

```python
# retrieval contexts
plt.figure(figsize=(15, 15))
sns.heatmap(retrieval_contexts, annot=True, linewidths=.5)
plt.title('Retrieval Contexts')
plt.xlabel('Feature Index')
plt.ylabel('Update Index')
plt.show()
print(norm(retrieval_contexts, axis=1))
```

### Retrieval Supports
Support for each item at each increment of retrieval.

```python
# retrieval supports
plt.figure(figsize=(15, 15))
sns.heatmap(retrieval_supports, annot=True, linewidths=.5)
plt.title('Supports For Each Item At Each Increment of Retrieval')
plt.xlabel('Choice Index')
plt.ylabel('Update Index')
plt.show()
```

### Outcome Probabilities At Selected Index

```python
support_index_to_plot = 1

plt.plot(np.arange(item_count + 1), retrieval_supports[support_index_to_plot])
plt.xlabel('Choice Index')
plt.ylabel('Outcome Probability')
# plt.title('Outcome Probabilities after Item {} Recalled First'.format(first_recall_item))
plt.title('Outcome Probabilities At Recall Index {}'.format(support_index_to_plot))
plt.show()
retrieval_supports[support_index_to_plot]
```

## Temporal Organization Analyses
Upon completion,  the `psifr` toolbox is used to generate three plots corresponding to the contents of Figure 4 in Morton & Polyn, 2016:
1. Recall probability as a function of serial position
2. Probability of starting recall with each serial position
3. Conditional response probability as a function of lag

Whereas previous visualizations were based on an arbitrary model simulation, the current figures are based on averages over a simulation of the model some specified amount of times.

A bug found in the Initial ICMR Prototype's coding of the SPC calculation can be fixed here. We previously accidentally swapped each item's position coding with its identity coding, resulting in a scaling of recall probability with item position. The model's average SPC looks substantially more realistic now.

```python
import matplotlib.pyplot as plt
import pandas as pd

try:
    from psifr import fr
except ModuleNotFoundError:
    !pip install -q psifr
    from psifr import fr

experiment_count = 100
model = InstanceCMR(**parameters)


# instantiate the model
encoding_contexts, encoding_supports = model.context, []

# track model state across experiences
for i in range(len(experiences)):
    model.experience(experiences[i])

# encoding phase
data = []
for experiment in range(experiment_count):
    data += [[experiment, 0, 'study', i + 1, i] for i in range(item_count)]
for experiment in range(experiment_count):
    if first_recall_item is not None:
        model.force_recall(first_recall_item)
    data += [[experiment, 0, 'recall', i + 1, o] for i, o in enumerate(model.free_recall())]
data = pd.DataFrame(data, columns=['subject', 'list', 'trial_type', 'position', 'item'])
merged = fr.merge_free_recall(data)

# visualizations
# spc
recall = fr.spc(merged)
g = fr.plot_spc(recall)
plt.title('Serial Position Curve')
plt.show()

# P(Start Recall) For Each Serial Position
prob = fr.pnr(merged)
pfr = prob.query('output <= 1')
g = fr.plot_spc(pfr).add_legend()
plt.title('Probability of Starting Recall With Each Serial Position')
plt.show()

# Conditional response probability as a function of lag
crp = fr.lag_crp(merged)
g = fr.plot_lag_crp(crp)
plt.title('Conditional Response Probability')
plt.show()
```

## Notes


### Drift Rate


#### Bounds
They can't be over 1.0, because for drift rates over 1, the `rho` quantity that enforces the length of `context` to 1.0 is `nan`. Can't be under 0 for the same reasons. Maybe be careful to keep bounds above 0, since scipy's bounds construct is inclusive.

#### Potential Problems
`rho` doesn't seem to reliably enforce `context` to a length of 1. Instead, `context` slowly grows in length over the course of the experiment. I have noticed this before, but so far it seems unaddressed. This is probably a result of `context_input` having too high a magnitude? No; I normalize `context_input`. The explanation has to lie in how I compute rho. My guess is that it's a matter of number precision; nothing I can do, and unlikely to impact performance.


### Shared Support
uniform amount of support items initially have for one another in recall competition


Curve seems unilaterally flat at shared support > .1. I'll range from 0 to .1.


### Item Support
item_support: initial strength of the diagonal of Mcf. 


Seems it can be arbitrary? Let's range it up to 5.0 or hold it at some arbitrary value. Seems to manipulate how steep the SPC is? Also controls direction of the CRP's lopsidedness. Super high is lopsided left. But it's not really a big difference at very low or very high values. So 0 to 5. Must be above 0.


### Learning Rate
Contribution of experimental relative to pre-experimental associations. Throws an error at 1.0. Why? No error at 0.
Even though it makes sense that learning rate shouldn't go beyond 1.0, I need to understand the error better.


### Primacy Scale/Decay
Can be any positive value, it seems, and has meaningful impact on shape too.


### Stop Probability Scale/Growth
As for scale, max this out at 1.0. Fitting seems impossible at 0. Growth seems unbounded. Might as well keep near 1 as well.


### Choice Sensitivity
Seems open-ended. Ugh.

```python

```
