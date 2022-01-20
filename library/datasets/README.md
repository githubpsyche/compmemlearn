# Preparing Free Recall Data
Whether working with simulated free recall data or the real deal, it has to be represented in a standardized way to enable interchangeable use of library functions.

For most of our analyses of free recall data, we'll follow the lead of the [Psifr library](https://psifr.readthedocs.io/en/latest/index.html) and represent most of our data in a long table format (encoded using `pandas`), with each row corresponding to a study or recall event and tracking for each event a subject index, a trial index, an input or output position, and item id. To identify items, we'll use a unique index or text string depending on the features of the item we're interested in.

Here we'll demonstrate the format using a few well-known datasets I'm using for research. Data preprocessing code is assigned to the `datasets` submodule of the `compmemlearn` package.