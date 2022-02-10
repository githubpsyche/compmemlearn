# Expanded Model Analysis


While figures like the serial position curve, probability of first recall by item position curve, and conditional response probability curve offer useful insights into the temporal organization of model outputs, we may obtain further value by tracking aspects of model state during simulation.

We can track at each update the state of the model's context representation and that representation's support for recall of each relevant item. We can also directly observe the model's memory store. Finally, we can track the similarity of the model's item representations to one another by comparing echoes associated with presenting each item as a probe.

In the 10/16 meeting about the result of these analyses, Sean further proposed an additional model analysis: forcing the model to recall particular items to start retrieval and the measuring consequences of that for the rest of free recall. To support this experiment, we also add a function to ICMR called `force_recall` that forces the recall of at least one specified recall. An additional experiment parameter `first_recall_item` is supported. If it is not set to `None`, the model will recall the specified item first during its recall simulations.

We also add support for distinct drift parameters (encoding, starting, and retrieval) to enable more flexible model configuration as development proceeds.


## Parameters


### Model Parameters

Model parameters can be configured here to visualize consequences for model analysis outcomes. In the current prototype, six parameters determine the behavior of Instance-CMR during simulations of free recall.

`item_count` specifies the number of unique items presented during encoding. For the prototype, we assume items are orthonormal in their features and represent them as such with unique index vectors.

To represent pre-experimental memory, initial traces representing each item's feature vector are included and modified to have some parametrized amount of `shared_support` for all items. The parameter thus works similarly to to CMR's `alpha` as specified in Morton & Polyn, 2016. With the value 0, the initial traces are held orthogonal to each other, excluding any pre-experimental association.

`encoding_drift_rate` controls the rate of context drift during encoding, while `starting_drift_rate` and `retrieval_drift_rate` control the rate of context drift when retrieval starts and rate of context drift during retrieval, respectively. Higher values cause `context` to drift more quickly as new items are experienced or recalled, as well as in between tasks.

`learning_rate` - similar to CMR's `gamma` - controls the contribution of experimental memory relative to pre-experimental memory to activity patterns during echo retrieval. With the value 1, experimental memory is not additionally weighted. Higher values enhance experimental memory and diminish pre-experimental memory, while lower values do the opposite.

Finally, `stop_probability_scale` and `stop_probability_growth` respectively control the scaling and the rate of increase of the probability of stopping during free recall over output position, implementing the same stopping mechanism implemented in Morton and Polyn, 2016.


### Experimental Parameters
The parameters `experiment_count` and `item_count` determine aspects of the experiment rather than the model: they control how many simulations occur and how many items are encoded by the model per simulation.

In the 10/16 meeting about the result of these analyses, Sean further proposed an additional model analysis: forcing the model to recall particular items to start retrieval and the measuring consequences of that for the rest of free recall. To support this experiment, we also add a function to ICMR called `force_recall` that forces the recall of at least one specified recall. An additional experiment parameter `first_recall_item` is supported. If it is not set to `None`, the model will recall the specified item first during its recall simulations.

```python
experiment_count = 1000
item_count = 24
first_recall_item = None # items are 1-index; indicate 1 if you want the model to recall the first presented item. 0 to immediately end recall.
 
encoding_drift_rate = .8
starting_drift_rate = .4
retrieval_drift_rate = .8
shared_support = 0.01
learning_rate = .6
stop_probability_scale = 0.01
stop_probability_growth = 0.3
choice_sensitivity = 1.0
```

In Google Colaboratory, "Run All Cells" can be executed with the shortcut Ctrl + F9 or through the "Runtime" menu at the top toolbar.


## Enabling Model Analysis at Each Recall Step
So we can analyze model state at each step of free recall, we modify the model to support a "steps" parameter in its free recall function controlling how many recalls the model should perform before pausing. We also refactor the model's computation of outcome probabilities to a separate model function. This makes it easier to measure support for recall of each item in context at arbitrary model states. This `outcome_probabilities` function also supports cued recall, returning probabilities after temporarily integrating specified retrieval cue(s) into context.

```python
import math
import numpy as np
from numpy.linalg import norm

class InstanceCMR(object):
    """The context maintenance and retrieval model re-imagined as an exemplar model.

    As typical of exemplar models, every `experience` is represented as a high-dimensional feature vector.
    A record of each experience - called a `trace` - is stored as a new, separate row in a m x n `memory` matrix
    where rows correspond to memory traces and columns correspond to feature dimensions.

    As in a retrieved context model, a contextual representation is also maintained. Compared to the representation of
    current experience, it changes slowly over time, reflecting a recency-weighted average of information related to
    recently presented stimuli. New memory traces associate studied items with the context active during presentation.
    This enables context-driven recall of items, and item-driven recall of context.

    To retrieve information from memory, a feature vector can be presented as a `probe`. The probe activates all traces
    in memory in parallel. Each trace's `activation` is a cubed function of its `similarity` to the probe. The sum of
    these traces weighted by their activation represents an `echo` summarizing the memory system's response to the
    probe. The content and intensity of this echo is the information that characterizes memory performance across tasks.

    Attributes:
        memory: a m x n array where rows correspond to accumulated memory traces and columns correspond to feature dims
        context: length-n vector reflecting a recency-weighted average of recently presented stimuli information
        item_count: number of unique items in experiment list identifying the relevant store of pre-experimental memory
        encoding_drift_rate: rate of context drift during encoding
        starting_drift_rate: rate of context drift when retrieval starts
        retrieval_drift_rate: rate of context drift during retrieval
        shared_support: uniform amount of support items initially have for one another in recall competition
        learning_rate: controls contribution of experimental associations relative to pre-experimental associations
        stop_probability_scale: scaling of the stop probability over output position
        stop_probability_growth: rate of increase in stop probability
        choice_sensitivity: sensitivity parameter of the Luce choice rule
    """

    def __init__(self, item_count, encoding_drift_rate, starting_drift_rate, retrieval_drift_rate, shared_support, 
                 learning_rate, stop_probability_scale, stop_probability_growth, choice_sensitivity):
        """Starts exemplar model with initial set of experiences in memory.

        For the prototype, we assume items are orthonormal in their features and use unique index vectors to represent
        them as such. To represent pre-experimental memory, a trace is initially laid for each item representing its
        vector representation modified to have some parametrized amount of shared_support for all items (similar to
        CMR's alpha) and another parameter learning_rate (similar to CMR's gamma) controlling the contribution of
        experimental memory relative to pre-experimental memory to echo representations.

        Args:
            item_count: number of unique experimental items identifying the relevant store of pre-experimental memory
            encoding_drift_rate: rate of context drift during encoding
            starting_drift_rate: rate of context drift when retrieval starts
            retrieval_drift_rate: rate of context drift during retrieval
            shared_support: uniform amount of support items initially have for one another in recall competition
            learning_rate: controls contribution of experimental memory relative to pre-experimental memory
            stop_probability_scale: scaling of the stop probability over output position
            stop_probability_growth: rate of increase in stop probability
        """
        # store initial parameters
        self.item_count = item_count
        self.encoding_drift_rate = encoding_drift_rate
        self.starting_drift_rate = starting_drift_rate
        self.retrieval_drift_rate = retrieval_drift_rate
        self.shared_support = shared_support
        self.learning_rate = learning_rate
        self.stop_probability_scale = stop_probability_scale
        self.stop_probability_growth = stop_probability_growth
        self.choice_sensitivity = choice_sensitivity

        # initialize memory and context
        self.context = np.eye(1, item_count + 1)
        self.memory = np.eye(item_count, item_count + 1, 1)
        self.memory[np.logical_not(np.eye(item_count, item_count + 1, 1, dtype=bool))] = self.shared_support

        # track model state during and outside of recall
        self.preretrieval_context = self.context
        self.state = 'encoding'
        self.recall = []

    def experience(self, experiences):
        """Adds new trace(s) to model memory, represented as new row(s) in the model's memory array. The stored
        experience is the context representation after it's been updated by the current experience.
        """
        if len(np.shape(experiences)) == 1:
            experiences = [experiences]
        for experience in experiences:
            self.update_context(np.array(experience), encoding_drift_rate)
            # self.update_context(np.array(experience), encoding_drift_rate)  # updating context first will bias CRP to left
            # trace = (self.context + experience) / norm(self.context + experience)
            # self.memory = np.vstack((self.memory, trace)) 
            self.memory = np.vstack((self.memory, self.context))

    def update_context(self, experience, drift_rate):
        """Updates contextual representation based on content of current experience."""
        # retrieves echo (memory information) associated w/ experience to serve as input to context
        # parallel operation to equation 10 from Morton & Polyn (2016)
        context_input = self.probe(experience)
        context_input = context_input / norm(context_input)  # normalized to have length 1

        # updated context is sum of current context and input modulated to have len 1 w/ rho and a specified drift_rate
        # parallel operation to equations 11-12 from Morton & Polyn (2016)
        rho = np.sqrt(1 + np.power(drift_rate, 2) * (np.power(self.context * context_input, 2) - 1)) - (
                drift_rate * (self.context * context_input))
        self.context = (rho * self.context) + (drift_rate * context_input)
        self.context = self.context/norm(self.context)  # can do this to enforce norm(context) = 1 when shared_support != 0

    def probe(self, probe):
        """Presents a cue to memory system, fetching an echo reflecting its pattern of activation across traces.

        The probe activates all traces in memory in parallel. Each trace's `activation` is a cubed function of its
        `similarity` to the probe. The sum of these traces weighted by their activation is an `echo` summarizing
        the memory system's response to the probe. The learning_rate parameter further weights the relative contribution
        of pre-experimental and experimental traces to activity patterns.
        """
        # computes and cubes similarity value to find activation for each trace in memory
        activation = np.power(np.sum(self.memory * probe, axis=1) / (norm(self.memory, axis=1) * norm(probe)), 3)

        # weights traces based on learning rate
        weighting = np.hstack((np.ones((self.item_count,)) / self.learning_rate, 
                               np.ones((len(self.memory) - self.item_count,)) * self.learning_rate))
        activation *= weighting

        # multiply each trace by its associated activation and take a column-wise sum to retrieve echo
        echo = np.sum((self.memory.T * activation).T, axis=0)
        return echo

    def compare_probes(self, first_probe, second_probe):
        """Compute the resemblance (cosine similarity) between the echoes associated with probes A and B."""
        echoes = self.probe(first_probe), self.probe(second_probe)
        return np.sum(echoes[0] * echoes[1]) / (norm(echoes[0]) * norm(echoes[1]))

    def outcome_probabilities(self, cues=None):
        """Computes the recall probability for each item given the current model state.
        An array of retrieval cues can be included for presentation before computing probabilities."""

        # temporarily update context to reflect cue(s)
        preretrieval_context = self.context
        if cues is not None:
            for cue in cues:
                self.update_context(cue, self.retrieval_drift_rate)

        # compute outcome probabilities
        items = np.eye(self.item_count, self.item_count + 1, 1)
        outcome_probabilities = np.zeros((self.item_count + 1))
        outcome_probabilities[0] = min(self.stop_probability_scale * np.exp(
            len(self.recall) * self.stop_probability_growth), 1.0)
        if outcome_probabilities[0] < 1:
            for j, item in enumerate(items):
                if j in self.recall:
                    continue
                outcome_probabilities[j + 1] = np.power(np.sum(self.context * items[j]) / (
                        norm(self.context) * norm(items[j])), self.choice_sensitivity)
            outcome_probabilities[1:] *= (1 - outcome_probabilities[0]) / np.sum(outcome_probabilities[1:])

        self.context = preretrieval_context
        return outcome_probabilities

    def force_recall(self, choice):
        """Forces model to recall chosen item and update context regardless of current model state.

        Here, recall items are 1-indexed, with a choice of 0 indicating a choice to end retrieval
        and return to preretrieval context.
        """
        items = np.eye(self.item_count, self.item_count + 1, 1)
        if self.state == 'encoding':
            self.recall = []
            self.preretrieval_context = self.context
            self.update_context(np.eye(1, self.item_count + 1), self.starting_drift_rate)
            self.state = 'retrieving'
        if not choice:
            self.state = 'encoding'
            self.context = self.preretrieval_context
        else:
            self.recall.append(choice - 1)
            self.update_context(self.probe(items[choice - 1]), retrieval_drift_rate)
        return self.recall

    def free_recall(self, steps=None):
        """Simulates performance on a free recall task based on experienced items.

        We initialize context similar to eq. 16 from Morton & Polyn (2016), simulating end-of-list distraction and
        some amount of pre-list context reinstatement. This context is used as a retrieval cue (probe) to attempt
        retrieval of a studied item, generating an associated memory echo.

        At each recall attempt, we also calculate a probability of stopping recall as a function of output position
        according to eq. 18 of Morton & Polyn (2016). The probability of recalling a given item conditioned on not
        stopping recall is defined on the basis of the item's similarity to the current contextual representation
        according to a formula similar to eq 19 of Morton and Polyn (2016).
        """

        # number of items to retrieve is infinite if steps is unspecified
        if steps is None:
            steps = math.inf
        steps = len(self.recall) + steps

        # drift context toward the pre-experimental context
        items = np.eye(self.item_count, self.item_count + 1, 1)
        if self.state == 'encoding':
            self.recall = []
            self.preretrieval_context = self.context
            self.update_context(np.eye(1, self.item_count + 1), self.starting_drift_rate)
            self.state = 'retrieving'

        # do recall for as many steps as specified or until stop triggered
        while len(self.recall) < steps:

            # compute outcome probabilities and make choice based on distribution
            outcome_probabilities = self.outcome_probabilities()
            choice = np.random.choice(len(outcome_probabilities), p=outcome_probabilities)

            # resolve and maybe store outcome
            # we stop recall if no choice is made
            if not choice:
                self.state = 'encoding'
                self.context = self.preretrieval_context
                break
            self.recall.append(choice - 1)
            self.update_context(self.probe(items[choice - 1]), self.retrieval_drift_rate)

        return self.recall
```

## Visualizing Model State Throughout Encoding

```python
import matplotlib.pyplot as plt
import seaborn as sns


# instantiate the model
model = InstanceCMR(item_count, encoding_drift_rate, starting_drift_rate, retrieval_drift_rate, 
                    shared_support, learning_rate, stop_probability_scale, stop_probability_growth, 
                    choice_sensitivity)
experiences = np.eye(item_count, item_count+1, 1)
encoding_contexts, encoding_supports = model.context, []

# track model state across experiences
for i in range(len(experiences)):
    model.experience(experiences[i])

    # track model contexts and item supports
    encoding_contexts = np.vstack((encoding_contexts, model.context))
    if len(encoding_supports) > 0:
        encoding_supports = np.vstack((encoding_supports, model.outcome_probabilities()))
    else:
        encoding_supports = model.outcome_probabilities()
```

```python
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

```python
# encoding supports
plt.figure(figsize=(15, 15))
sns.heatmap(encoding_supports, annot=True, linewidths=.5)
plt.title('Supports For Each Item At Each Increment of Encoding')
plt.xlabel('Amount of Support')
plt.ylabel('Update Index')
plt.show()
```

## Visualizing Model State Throughout Free Retrieval

```python
# initialization; using model instantiated in previous cell
retrieval_contexts, retrieval_supports = model.context, model.outcome_probabilities()

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

```python
# retrieval supports
plt.figure(figsize=(15, 15))
sns.heatmap(retrieval_supports, annot=True, linewidths=.5)
plt.title('Supports For Each Item At Each Increment of Retrieval')
plt.xlabel('Choice Index')
plt.ylabel('Update Index')
plt.show()
```

```python
support_index_to_plot = 2

plt.plot(np.arange(item_count+1), retrieval_supports[support_index_to_plot])
plt.xlabel('Choice Index')
plt.ylabel('Outcome Probability')
#plt.title('Outcome Probabilities after Item {} Recalled First'.format(first_recall_item))
plt.title('Outcome Probabilities At Recall Index {}'.format(support_index_to_plot))
plt.show()
retrieval_supports[support_index_to_plot]
```

## Model Memory
We add further visualizations exploring the content of the model's memory matrix, visualizing both the trace array and similarities between echo representations associated with each encoded item.

```python
# visualize model memory
plt.figure(figsize=(15, 20))
sns.heatmap(model.memory, annot=True, linewidths=.5)
plt.title('Model Memories')
plt.xlabel('Feature Index')
plt.ylabel('Trace Index')
plt.show()
```

```python
# item similarity matrix
similarities = np.zeros((item_count, item_count))
for x in range(item_count):
    for y in range(item_count):
        similarities[x, y] = model.compare_probes(experiences[x], experiences[y])

# visualize item similarities
plt.figure(figsize=(15, 15))
sns.heatmap(similarities, annot=True, linewidths=.5, mask=np.eye(item_count))
plt.title('Item Similarities')
plt.xlabel('Item Index')
plt.ylabel('Item Index')
plt.show()
```

```python
# we can also plot how item similarity varies as a function of proximity
plt.plot(np.arange(item_count), similarities[int(item_count/2)])
plt.title('Similarity of Each Echo to that of Middle Item')
plt.ylabel('Echo Similarity to That of Middle Item')
plt.xlabel('Item Index')
plt.show()
print('done')
```

## Temporal Organization Analyses
Upon completion,  the `psifr` toolbox is used to generate three plots corresponding to the contents of Figure 4 in Morton & Polyn, 2016:
1. Recall probability as a function of serial position
2. Probability of starting recall with each serial position
3. Conditional response probability as a function of lag

Whereas previous visualizations were based on an arbitrary model simulation, the current figures are based on averages over a simulation of the model some specified amount of times.

A bug found in the Initial ICMR Prototype's coding of the SPC calculation can be fixed here. We previously accidentally swapped each item's position coding with its identity coding, resulting in a scaling of recall probability with item position. The model's average SPC looks substantially more realistic now.

```python
import pandas as pd
try:
    from psifr import fr
except ModuleNotFoundError:
    !pip install -q psifr
    from psifr import fr

# encoding phase
data = []
for experiment in range(experiment_count):
    data += [[experiment, 0, 'study', i+1, i] for i in range(item_count)]
for experiment in range(experiment_count):
    if first_recall_item is not None:
        model.force_recall(first_recall_item)
    data += [[experiment, 0, 'recall', i+1, o] for i, o in enumerate(model.free_recall())]
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

## Observations


### Fixing Serial Position and Probability of First Recall Curves
This expansion of our pool of model analyses made obvious what was wrong with our Serial Position Curve visualizations, so we were able to fix them and obtain SPCs that more closely match our expectations.

Including an extra drift parameter controlling the contribution of initial encoding context to the content of initial retrieval context enables pretty flexible control of SPC and PFR shape. A high encoding drift rate but a low starting drift rate enforces a good shape for our PFR curve. Some shared support also results in reasonable SPCs, too. I haven't found a big use for `retrieval_drift_rate` yet, though. And of course none of these affect our CRP.


#### Relevant Parameters

```
experiment_count = 1000
item_count = 24
first_recall_item = None  # items are 1-index; indicate 1 if you want the model to recall the first presented item. 0 to immediately end recall.

encoding_drift_rate = .8
starting_drift_rate = .2
retrieval_drift_rate = .8
shared_support = 0.01
learning_rate = 1
stop_probability_scale = 0.01
stop_probability_growth = 0.3
choice_sensitivity = 1.0
```


### Creating memory traces before updating context as opposed to updating context first
In our 10/16 meeting, we explored the impact of this on CRP shape. We found that this made the CRP symmetrical rather than lopsided, and might be a part of the solution to our problem with the model's temporal organization.

This also seems to screw up our SPCs at the parameter configuration indicated above; the line just becomes linear. PFR is preserved, though. The reason why seems to be that shared support for/by other items is discarded without an initial update to context. Jacking up our `starting_drift_rate` parameter though reinstates the U-shape.


### Directly storing model context as our trace instead of generating a trace based on context
We found that had no impact on model performance beyond also making model CRP symmetric. Since it makes the model simpler and coheres with other practices in the multiple traces model literature, it may become a default feature of the model. A separate trace just might not be necessary.



### Increasing Context Magnitudes
`norm(self.context)` isn't 1 like `rho` is supposed to enforce when context is updated. Instead, it increases over time. Sean linked this to our shared support parameter. When shared_support is set to 0, `rho` controls context's magnitude appropriately. We should investigate the `shared_support` parameter in this context, exploring what it contributes to model performance and how its impact on `norm(context)` can be controlled.

Further analysis finds that context norms don't gradually increase; instead they stabilize to 1 + shared_support. Dividing context by its norm so that `norm(context)` becomes 1 does not substantially affect model performance. 

Sean suggests it's not a big deal and can be handled in hacky ways if relevant.


### Ineffective Gamma and our Lopsided CRP
I have a gamma parameter but it's only used for computing echoes apparently; it doesn't directly decide recall except perhaps when the retrieval context is adjusted before recalling the next item. Sean tied the gamma parameter as well as the content of the retrieval cue to the lopsidedness of the CRP curve. I have to investigate the issue to resolve this 'final' problem with our ICMR model.

In the CMR paper I've been basing this model on, `gamma` explained as controlling the "amount of experimental context retrieved by a recalled item". Gamma has two roles in the recent Morton and Polyn (2016) specification of the model. First, it controls the initial strength of feature-to-context associations in CMR. Input to context within CMR is defined by the function of Mfc with current item features; by default, Mfc is initially an identity matrix, so cIN is just equivalent to f when f is orthonormal. A high gamma can reduce the initial weighting of each feature vector within cIN. Later, Mfc is updated as experience occurs, with its change defined as a function of gamma, the current context representation, and the the current item being considered. This is supposed to associate the current item and the current state in memory through simple Hebbian learning. Gamma in this sense controls just big the alterations turn out to be. This is different from what our drift parameters are about, which is the change to context as a result of experience.

How does a Gamma parameter control the lopsidedness of a CRP curve? Concretely speaking, the shape of a CRP curve depends on whether item is more associated with items occurring before it or after it in experience. Context is a recency-weighted representation of past experience. During encoding, the model blends representation of each discrete experience with this recency-weighted representation of items occurring before it. During recall, a different matrix Mcf controls the activation of each item given current context; however, Mfc controls recall of successive items by way of determining the state of context after recall as a function of the recalled item.

So Mfc represents the current association between item features and context and controls how context is updated when an item is presented or remembered. It in turn is controlled by context, updating to increase association between item features and features of items that have been presented before it, weighting for recency. So when a previously experienced item is recalled, Mfc updates context not *just* to look more like the item's feature vector, but to look more like a blend of the item's feature vector *and* its contextual history.

During encoding, each item becomes associated with a recency-weighted representation of the items that came before it. Low positive-lag CRPs are supposed to higher than Low negative-lag CRPs because the context for item i+1 includes information about item i (since it's the most recent item) while the context for item i-1 does not. And of course item i's context includes information about item i. So if successive recall is determined by the similarity of candidate item representations to the current item representation, this shared contextual feature between item i and item i+1 should drive increased forward recall.

How does increasing gamma modulate this? During encoding, gamma controls how much an item representation becomes like its context. Again, this is separate from contextual drift, which determines how much context becomes like the current item representation. Low drift but high gamma maximally make an item's representation reflect item history while high drift and low gamma do the opposite: context already mostly consists of the current item representation and updates to memory are pretty minimal anyway. Ah, I'm still not getting how this controls lopsidedness. I'll have to do some experimentation.


### Increasing Context Magnitudes
`norm(self.context)` isn't 1 like `rho` is supposed to enforce when context is updated. Instead, it increases over time. Sean linked this to our shared support parameter. When shared_support is set to 0, `rho` controls context's magnitude appropriately. We should investigate the `shared_support` parameter in this context, exploring what it contributes to model performance and how its impact on `norm(context)` can be controlled.

Further analysis finds that context norms don't gradually increase; instead they stabilize to 1 + shared_support. Dividing context by its norm so that `norm(context)` becomes 1 does not substantially affect model performance. 

Sean suggests it's not a big deal and can be handled in hacky ways if relevant.


### 10/16 Meeting
We next explored some manipulations to the model to examine their consequences for analysis outcomes. In our 10/16 meeting we considered:
1. Creating memory traces before updating context as opposed to updating context first
2. Directly storing model context as our trace instead of generating a trace based on context
3. Updating context after retrieval toward that of the specific trace associated with the recalled item during encoding (rather than its echo)
4. Updating context after retrieval toward the item's feature representation itself (rather than its echo)

We found that (1) made the CRP symmetrical rather than lopsided, and might be a part of the solution to our problem with the model's temporal organization.

We found that (2) had no impact on model performance. Since it makes the model simpler and coheres with other practices in the multiple traces model literature, it may become a default feature of the model.

We found ambiguous consequences for (3) and (4) and are relatively uncertain about their importance for further model development.

Sean further proposed an additional model analysis: forcing the model to recall particular items first during retrieval and measuring consequences for the rest of free recall. I include support for an experimental parameter in this notebook that controls the first item recalled.

I should have some concrete record of the outcomes from our 10/16 manipulations.


### I may still want to separate contextual and item features in memory traces
And Sean has always preferred it. I'm not sure what this will do; it's worth checking. It's an approach I've seen in the MINERVA 2 and a recent Jones paper.

Quotation from the MINERVA 2 paper:
> Judgments of frequency are always relative to some "time window" or context over which frequency is to be integrated. This is demonstrated clearly by the ability of subjects to give largely independent judgments of frequency for the same word in two different lists (Hintzman & Block, 1971). Such list-specific frequency judgments can be simulated in MINERVA 2 by assuming first of all that certain trace features distinguish between lists. For example, let T(U) to T(i,4) be -1, +1,0, ° if trace i is from List 1, and 0, 0, -1, +1 if it is from List 2. The remainder of the features U= 5 '" N) represent the item itself. Now, probes can be constructed that activate features specific to the target list and inhibit those specific to the nontarget list (inhibition is produced by multiplying feature values by -1). Thus, in the present example, j =1 ... 4 in a probe targeting List 1 and inhibiting List 2 would be -1, +1, +1, -1, with the remaining features representing the test item. The frequency judgment is based on echo intensity, as before.

Quotation from my comment on Johns and Jones (2012):
> Mike's work here on an exemplar model that integrates lexical and perceptual memory seems to offer some lessons for how ICMR might integrate disparate sources of information (e.g item info and contextual info) too. While my work on ICMR has tried to blend the two, the model here works how you've been suggesting: through maintenance of separate perceptual and lexical content for each new memory trace vector. These results show that echoes extracted from a model like this can infer completed representations from partial probes. You can present a probe with just lexical content (and null values for perceptual information) and obtain an echo representation that also tracks associated perceptual regularities. And vice versa!

I suppose I thought that this kind of separation was "illegal", based on my work with the Jamieson et al (2018) semantic memory model. Word context was blended with word representation in that simulation, so I imagined I should be doing something parallel with context and item representation. We'll test the impact of drawing this distinction on model dynamics.

In the meeting, Sean concurred that this change likely would have little to do with the current issues we're currently working through. Since we now favor storing the context vector directly into model memory, the fate of this proposal is even more mysterious.

Guiding idea is that I want the model's memory matrix to play the role Mfc and Mcf plays in CMR. I should return to that thesis and assess the extent to which my model realizes it, as well as the extent to which model performance depends on consistency with it.
