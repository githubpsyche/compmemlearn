# AUTOGENERATED! DO NOT EDIT! File to edit: projects/05_Model_Visualization.ipynb (unless otherwise specified).

__all__ = ['encoding_states', 'plot_states', 'encoding_visualizations', 'latent_mfc_mcf', 'retrieval_states',
           'outcome_probs_at_index', 'retrieval_visualizations', 'temporal_organization_analyses']

# Cell
#export
import numpy as np

def encoding_states(model):
    """
    Tracks state of context, and item supports across encoding. Model is also advanced to a state of fully encoded
    memories.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - activations: function returning item activations given a vector probe
    - outcome_probabilities: function returning item supports given a set of activations

    **Returns** array representations of context and support for retrieval of each item at each increment of item
    encoding. Each has shape model.item_count by model.item_count + 1.
    """

    experiences = np.eye(model.item_count, model.item_count + 1, 1)
    cmr_experiences = np.eye(model.item_count, model.item_count)
    encoding_contexts, encoding_supports = model.context, []

    # track model state across experiences
    for i in range(len(experiences)):
        try:
            model.experience(experiences[i].reshape((1, -1)))
        except ValueError:
            # special case for CMR
            model.experience(cmr_experiences[i].reshape((1, -1)))

        # track model contexts and item supports
        encoding_contexts = np.vstack((encoding_contexts, model.context))

        if model.__class__.__name__ == 'CMR':
            activation_cue = lambda model: model.context
        else:
            activation_cue = lambda model: np.hstack((np.zeros(model.item_count + 1), model.context))

        if len(encoding_supports) > 0:
            encoding_supports = np.vstack((encoding_supports, model.outcome_probabilities(activation_cue(model))))
        else:
            encoding_supports = model.outcome_probabilities(activation_cue(model))

    return encoding_contexts, encoding_supports

# Cell
# export
# collapse_input
import seaborn as sns
import matplotlib.pyplot as plt

def plot_states(matrix, title, figsize=(15, 15), savefig=False):
    """
    Plots an array of model states as a value-annotated heatmap with an arbitrary title.

    **Arguments**:
    - matrix: an array of model states, ideally with columns representing unique feature indices and rows
        representing unique update indices
    - title: a title for the generated plot, ideally conveying what array values represent at each entry
    - savefig: boolean deciding whether generated figure is saved (True if Yes)
    """
    plt.figure(figsize=figsize)
    sns.heatmap(matrix, annot=True, linewidths=.5)
    plt.title(title)
    plt.xlabel('Feature Index')
    plt.ylabel('Update Index')
    if savefig:
        plt.savefig('figures/{}.jpeg'.format(title).replace(' ', '_').lower(), bbox_inches='tight')
    plt.show()

# Cell
# export
def encoding_visualizations(model, savefig=True):
    """
    Plots encoding contexts, encoding supports as heatmaps.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - activations: function returning item activations given a vector probe
    - outcome_probabilities: function returning item supports given a set of activations
    - memory: a unitary representation of the current state of memory

    **Also** requires savefig:  boolean deciding if generated figure is saved
    """

    encoding_contexts, encoding_supports = encoding_states(model)
    plot_states(encoding_contexts, 'Encoding Contexts', savefig=savefig)
    plot_states(encoding_supports, 'Supports For Each Item At Each Increment of Encoding', savefig=savefig)

# Cell

def latent_mfc_mcf(model):

    """
    Generates the latent $M^{FC}$ and $M^{CF}$ in the specified ICMR instance.
    For exploring and demonstrating model equivalence, we can calculate for any state of ICMR's dual-store memory
    array $M$ a corresponding $M^{FC}$ (or $M^{CF}$) by computing for each orthogonal $f_i$ (or $c_i$) the model's
    corresponding echo representation.
    """

    encoding_states(model)

    # start by finding latent mfc: the contextual representation cued when each orthogonal $f_i$ is cued
    latent_mfc = np.zeros((model.item_count, model.item_count+1))
    cue = np.zeros(model.item_count*2 + 2)
    for i in range(model.item_count):
        cue *= 0
        cue[i+1] = 1
        latent_mfc[i] = model.echo(cue)[model.item_count + 1:]

    # now the latent mcf
    latent_mcf = np.zeros((model.item_count+1, model.item_count))
    for i in range(model.item_count+1):
        cue *= 0
        cue[model.item_count+1+i] = 1
        latent_mcf[i] = model.echo(cue)[1:model.item_count + 1] # start at 1 due to dummy column in F

    # plotting
    return latent_mfc, latent_mcf

# Cell
# hide
#collapse_input
import numpy as np

def retrieval_states(model, first_recall_item=None):
    """
    Tracks state of context, and item supports across retrieval. Model is also advanced into a state of
    completed free recall.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - activations: function returning item activations given a vector probe
    - outcome_probabilities: function returning item supports given a set of activations
    - free_recall: function that freely recalls a given number of items or until recall stops
    - state: indicates whether model is encoding or engaged in recall with a string

    **Also** optionally uses first_recall_item: can specify an item for first recall

    **Returns** array representations of context and support for retrieval of each item at each increment of item
    retrieval. Also returns recall train associated with simulation.
    """

    if model.__class__.__name__ == 'CMR':
        activation_cue = lambda model: model.context
    else:
        activation_cue = lambda model: np.hstack((np.zeros(model.item_count + 1), model.context))

    # encoding items, presuming model is freshly initialized
    encoding_states(model)
    retrieval_contexts, retrieval_supports = model.context, model.outcome_probabilities(activation_cue(model))

    # pre-retrieval distraction
    model.free_recall(0)
    retrieval_contexts = np.vstack((retrieval_contexts, model.context))
    retrieval_supports = np.vstack((retrieval_supports, model.outcome_probabilities(activation_cue(model))))

    # optional forced first item recall
    if first_recall_item is not None:
        model.force_recall(first_recall_item)
        retrieval_contexts = np.vstack((retrieval_contexts, model.context))
        retrieval_supports = np.vstack((retrieval_supports, model.outcome_probabilities(activation_cue(model))))

    # actual recall
    while model.retrieving:
        model.free_recall(1)
        retrieval_contexts = np.vstack((retrieval_contexts, model.context))
        retrieval_supports = np.vstack((retrieval_supports, model.outcome_probabilities(activation_cue(model))))

    return retrieval_contexts, retrieval_supports, model.recall[:model.recall_total]

# Cell
#collapse_input
def outcome_probs_at_index(model, support_index_to_plot=1, savefig=True):
    """
    Plots outcome probability distribution at a specific index of free recall.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - activations: function returning item activations given a vector probe
    - outcome_probabilities: function returning item supports given a set of activations
    - free_recall: function that freely recalls a given number of items or until recall stops
    - state: indicates whether model is encoding or engaged in recall with a string

    **Other arguments**:
    - support_index_to_plot: index of retrieval to plot
    - savefig: whether to save or display the figure of interest

    **Generates** a plot of outcome probabilities as a line graph. Also returns vector representation of the
    generated probabilities.
    """

    retrieval_supports = retrieval_states(model)[1]
    plt.plot(np.arange(model.item_count + 1), retrieval_supports[support_index_to_plot])
    plt.xlabel('Choice Index')
    plt.ylabel('Outcome Probability')
    plt.title('Outcome Probabilities At Recall Index {}'.format(support_index_to_plot))
    plt.show()
    return retrieval_supports[support_index_to_plot]

# Cell
#collapse_input
def retrieval_visualizations(model, savefig=True):
    """
    Plots incremental retrieval contexts and supports, as heatmaps, and prints recalled items.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - activations: function returning item activations given a vector probe
    - outcome_probabilities: function returning item supports given a set of activations

    **Also** uses savefig: boolean deciding whether figures are saved (True) or displayed
    """

    retrieval_contexts, retrieval_supports, recall = retrieval_states(model)
    plot_states(retrieval_contexts, 'Retrieval Contexts', savefig=savefig)
    plot_states(retrieval_supports, 'Supports For Each Item At Each Increment of Retrieval',
                savefig=savefig)
    return recall

# Cell
#collapse_input
import pandas as pd
from psifr import fr

def temporal_organization_analyses(model, experiment_count, savefig=False, figsize=(15, 15), first_recall_item=None):
    """
    Visualization of the outcomes of a trio of organizational analyses of model performance on a free recall
    task.

    **Required model attributes**:
    - item_count: specifies number of items encoded into memory
    - context: vector representing an internal contextual state
    - experience: adding a new trace to the memory model
    - free_recall: function that freely recalls a given number of items or until recall stops

    **Other arguments**:
    - experiment_count: number of simulations to compute curves over
    - savefig: whether to save or display the figure of interest

    **Returns** three plots corresponding to the contents of Figure 4 in Morton & Polyn, 2016:
    1. Recall probability as a function of serial position
    2. Probability of starting recall with each serial position
    3. Conditional response probability as a function of lag
    """

    # encode items
    try:
        model.experience(np.eye(model.item_count, model.item_count + 1, 1))
    except ValueError:
        # so we can apply to CMR
        model.experience(np.eye(model.item_count, model.item_count))

    # simulate retrieval for the specified number of times, tracking results in df
    data = []
    for experiment in range(experiment_count):
        data += [[experiment, 0, 'study', i + 1, i] for i in range(model.item_count)]
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
    if savefig:
        plt.savefig('figures/spc.jpeg', bbox_inches='tight')
    else:
        plt.show()

    # P(Start Recall) For Each Serial Position
    prob = fr.pnr(merged)
    pfr = prob.query('output <= 1')
    g = fr.plot_spc(pfr).add_legend()
    plt.title('Probability of Starting Recall With Each Serial Position')
    if savefig:
        plt.savefig('figures/pfr.jpeg', bbox_inches='tight')
    else:
        plt.show()

    # Conditional response probability as a function of lag
    crp = fr.lag_crp(merged)
    g = fr.plot_lag_crp(crp)
    plt.title('Conditional Response Probability')
    if savefig:
        plt.savefig('figures/crp.jpeg', bbox_inches='tight')
    else:
        plt.show()