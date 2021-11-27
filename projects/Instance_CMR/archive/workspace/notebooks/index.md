---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# InstanceCMR
> An Instance-Based Account of Context Maintenance and Retrieval


In retrieved context accounts of memory search such as the Context
Maintenance and Retrieval (CMR) model (Polyn et al., 2009),
representations of studied items in a free recall experiment are
associated with an internal representation of context that changes
slowly during the study period. These associations in turn account for
organizational effects in recall sequences, such as the tendency for
related items to be recalled successively.

Specifications of the model tend to characterize these dynamics in terms
of a simplified neural network, as building a single prototypical
pattern of associations between each item and context (and vice versa)
across experience. By contrast, models of categorization and other
memory phenomena have increasingly converged on instance-based accounts
(Hintzman, 1984) that conceptualize memory as a stack of trace vectors
that each represent discrete experiences and support recall through
parallel activation based on similarity to a probe.

To investigate the consequences of this distinction, we present an
instance-based specification of CMR that encodes associations between
studied items and context by instantiating memory traces corresponding
to each experience, and drives recall through context-based coactivation
of those traces. We analyze the model&rsquo;s ability to account for
traditional phenomena that have been used as support for the original
prototypical specification of CMR, evaluate conditions under which the
specifications might behave differently, and explore the model&rsquo;s
capacity for integration with existing instance-based models to
elucidate a broader collection of memory phenomena.


## Features


- Thoroughly optimized and documented implementations of CMR, InstanceCMR, and related models, including benchmarks and parameter bounds
- A small library of utilities supporting model analysis, including state visualization and parameter fitting
- Tutorial notebooks outlining typical workflows to use and extend this codebase in various contexts
- Various simulation experiments developing a detailed account of how an instance-based architecture shapes model predictions


## Getting Started


To learn about the model, corresponding analyses, and the accompanying library of helper functions, check out the [project docs](https://vucml.github.io/instance_cmr/) and peruse its sidebar. Pages contain links to their corresponding IPython notebooks, both within this repository as well as for use on Google Colaboratory, a free, cloud-based Jupyter environment with GPU capabilities.

While this repository mainly exists to organize and preserve analysis related to InstanceCMR, we include and maintain a library of functions and classes available for reuse in new contexts. This library is maintained in the `instance_cmr/` subdirectory. 

Currently, the best way to install the library is to perform an [editable install](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install): upon installation, library functions will be usable anywhere in the relevant environment. Perform this by cloning the repository and at its root using the command `pip install -e .`.
