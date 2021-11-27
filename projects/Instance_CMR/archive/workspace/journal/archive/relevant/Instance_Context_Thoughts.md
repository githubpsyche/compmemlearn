# ITS and Instance_CMR: Distinguishing Models of Context
A lot of the work on `instance_cmr` has been connected to Jamieson et al's (2018) instance theory of semantic memory (ITS). At the very least, the paper worked as a modern reference to help me grasp how multiple trace models of the MINERVA 2 tradition actually work, giving me a starting point to think about how CMR could be realized withini that tradition. The paper also makes tantalyzing references to episodic memory and context that might have prompted us to brainstorm how its ideas might connect to work in the free recall domain where these ideas are front and center. It might be worth reflecting on how the paper's integration of episodic context into its model of semantic memory relates to that of our current `instance_cmr` prototype.


## ITS and Context
Under ITS, experiences/episodes are a linear combination of word representations, a document context:

> Every letter string (i.e., word or nonword) is represented by a unique $n$ dimensional vector, $w$, where each dimension takes a randomly sampled value from a normal distribution with mean zero and variance $1/n$. Vectors constructed in this manner are orthonormal in expectation and are assumed to represent the physical form (orthography or phonology) of the word, as in BEAGLE.
> 
> Memory for an example of language is encoded as an instance context $c_i$, equal to the sum of the $j = 1…h$ word vectors in context $i$,
> 
> $c_i = \sum_{j=1}^{j=h} w_{ij}$
> 
> where $h$ is the number of words in context $i$, $w_j$ is word $j$ in the context, and $c_i$ is the sum of the words in context i. To illustrate, the context, "the dog bit the mailman" is stored as $w_{dog}$ + $w_{bit}$ + $w_{mailman}$ (consistent with standard practice, we excluded a list of stop words).
>
> The memory for each context, $c_i$, is stored as a separate row in an $m$ x $n$ memory matrix, $M$, where rows correspond to memory traces (i.e., **document contexts**) and columns correspond to features,
>
> $M_i = c_i = \sum_{j=1}^{j=h} w_{ij}$

So there is no distinction between some focal item and the temporal context of that item during creation of a memory trace as there is in ICMR. However, during retrieval, distinctions between particular words and the contexts in which they occur are critical. In the first simulation experiment exploring ITS, for instance, Jamieson et al showed that individual word vectors could be presented to the model to retrieve information about the contexts under which they occur. Maybe even more impressively, linear combinations of word representations could identify semantic distinctions between identically spelled words (homonyms) - e.g. between "break" as in "report (the news)" and "break" as in "smash (the dinnerware)".




Alternatively, depending on how `document contexts` are selected, this scheme might be characterized as actually context-free in the sense considered under ICMR: items are just sets of words, and the context under which items occur is not relevant.

<!-- #region -->
## InstanceCMR adds Real Context
If we consider



However experiential units and the context under which they occur are conceptualized under ITS, retrieved context models clearly takes a substantially different approach. Under this class of models, a feature-based representation of each studied item causes item-specific information to be integrated into a gradually changing representation of temporal context. In ICMR in particular, upon new experiences, the new trace stored as a row in $M$ contains both a representation of the experienced item and of the updated state of context. Later, when an item is recalled, the context associated with it is reactivated, providing a good cue for items studied nearby in the list and resulting in temporal organization. 

In our Dual Store prototype of ICMR, representations of experience and their temporal context have discrete stores in $M$: a subset of entries in a trace $t_i$ encode a vector representation of the experienced item while other entries ini $t_i$ encode a vector representation of the temporal context of the experienced item.

If we consider the model in the same setting as ITS, representations for new memory traces depends both on 
<!-- #endregion -->

```python

```

## Context as a Way To Fit Narrative Knowledge into a Model of Semantics?
I talked a lot earlier this week about how linguistic contextual representations serve word-sense disambiguation and temporal context representations might do the same thing for 

Have kinda found mysterious for a while the distinction between semantic memory and our memory for, like, stories and whatnot where a word's exact meaning and relations with other words might be extremely different from its overall meaning in a conceptual lexicon. But it seems like context mostly solves that. 

We can imagine an instance model of stories that starts with an overall model of semantics [e.g. like Jamieson et al's (2018) ITS] and to encode units in stories, stores a word-form representation of these units, a contextual representation unique to that story and more or less orthogonal to that of other stories, and 

...