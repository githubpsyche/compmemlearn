# AUTOGENERATED! DO NOT EDIT! File to edit: library/model_analysis/Contiguity_Tracing.ipynb (unless otherwise specified).

__all__ = ['matrix_heatmap', 'icmr_memory_heatmap', 'latent_mfc_mcf', 'mfc_heatmap', 'connectivity_by_lag']

# Cell

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def matrix_heatmap(matrix, title='', figsize=(15, 15), savefig=False, axis=None):
    """
    Plots an array of model states as a value-annotated heatmap with an arbitrary title.

    **Arguments**:
    - matrix: an array of model states, ideally with columns representing unique feature indices and rows
        representing unique update indices
    - title: a title for the generated plot, ideally conveying what array values represent at each entry
    - savefig: boolean deciding whether generated figure is saved (True if Yes)
    """
    plt.figure(figsize=figsize)
    sns.heatmap(matrix, annot=True, linewidths=.5, ax=axis)
    plt.title(title)
    plt.xlabel('Feature Index')
    plt.ylabel('Update Index')
    if savefig:
        plt.savefig('figures/{}.jpeg'.format(title).replace(' ', '_').lower(), bbox_inches='tight')
    plt.show()

def icmr_memory_heatmap(model, just_experimental=False, just_context=False):
    memory_shape = np.shape(model.memory)
    fig_size = list(reversed(memory_shape))
    plotted_memory = model.memory.copy()
    title = "Memory Traces"

    if just_context:
        fig_size[0] /= 2
        plotted_memory = plotted_memory[:, int(memory_shape[1]/2):]
        title = "Contextual " + title

    if just_experimental:
        fig_size[1] -= model.item_count
        plotted_memory = plotted_memory[int(memory_shape[0]/2):]
        title = "Experimental " + title

    matrix_heatmap(plotted_memory, title, figsize=fig_size)

# Cell

import numpy as np

def latent_mfc_mcf(model):

    """
    Generates the latent $M^{FC}$ and $M^{CF}$ in the specified ICMR instance.
    For exploring and demonstrating model equivalence, we can calculate for any state of ICMR's dual-store memory
    array $M$ a corresponding $M^{FC}$ (or $M^{CF}$) by computing for each orthogonal $f_i$ (or $c_i$) the model's
    corresponding echo representation.
    """

    # start by finding latent mfc: the contextual representation cued when each orthogonal $f_i$ is cued
    latent_mfc = np.zeros((model.item_count, model.item_count+2))
    for i in range(model.item_count):
        latent_mfc[i] = model.echo(model.items[i])[model.item_count + 2:]

    latent_mcf = np.zeros((model.item_count, model.item_count+2))
    context_units = np.hstack(
        (np.zeros((model.item_count, model.item_count+2)),
         np.eye(model.item_count, model.item_count + 2, 1))
         )
    for i in range(model.item_count):
        latent_mcf[i] = model.echo(context_units[i])[:model.item_count+2]

    return latent_mfc, latent_mcf

def mfc_heatmap(mfc):
    matrix_heatmap(mfc, title='', figsize=list(reversed(np.shape(mfc))))

# Cell

def connectivity_by_lag(item_connections, item_count):

    lag_range = item_count - 1
    total_connectivity = np.zeros(lag_range * 2 + 1)
    total_possible_lags = np.zeros(lag_range * 2 + 1)
    item_positions = np.arange(item_count, dtype=int)

    # tabulate bin totals for actual and possible lags
    # this time instead of looping through trials and recall indices, we only loop once through each item index
    for i in range(item_count):

        # lag of each item from current item is item position - i,
        # and will always be in range [-lag_range, lag_range] so we keep position by adding lag_range
        item_lags = item_positions - i + lag_range
        total_connectivity[item_lags] += item_connections[i]
        total_possible_lags[item_lags] += 1

    # divide by possible lags to get average connectivity
    connectivity = total_connectivity / total_possible_lags
    return connectivity