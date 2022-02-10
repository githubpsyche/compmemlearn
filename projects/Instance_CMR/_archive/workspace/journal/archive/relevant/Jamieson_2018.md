# An Instance Theory of Semantic Memory

## Background
Some stuff under the header of "distributional semantic models" is stuff that holds for ITS, too. For example, ITS is also a way of characterizing co-occurrence of words across a document corpus; it just builds the vector representation representing words' aggregate meanings at retrieval rather than at encoding. I worry students might get confused if the distinctions/similarities aren't made super clear.

For this reason and others, it might be better to introduce "semantic memory" or whatever separately from DSMs/ITS. There are a lot of ways to do this; could provide (or elaborate on Jamieson et al's own framing of) context about the research question itself, perhaps w/ some implicit Marr-ian framework. Like just presenting and clarifying questions such as "How do humans transform first-order statistical experience with language into deep knowledge representations of word meaning?" "How do humans transform episodic experience into semantic representations?". I c/ped these from the intro. 

## Motivation

### Big Idea
The "big idea" of ITS as a demonstration that "semantic memory can be conceptualized as an artifact of retrieval from episodic memory rather than an encoding mechanism" may deserve underlining. Could also point out how this isn't a new idea: Hintzman's 1986 papers make the same point.

Similarly could outline while explaining the MINERVA 2-basis of Jamieson et al (2018) is how the framework makes model development as simple as finding an interesting way to encode episodic memory traces as vectors and relating the model's echoes to behavioral phenomena. This is basically all that Jamieson et al (2018) extends.

### The XOR Problem?
I suspect students will have questions about why exemplar-based theories are so preferred over prototype theories in the categorization literature. Jamieson et al's presentation of the XOR problem is pretty short and unclear.

#### Is ITS Computationally Tractable?
Similarly, they often bring up the critique that instance-based models of semantics are computationally expensive - either in terms of memory (something like Kahana's critique) or even in terms of processing (integrating over tons of traces means linear scaling of computation time with each new experience). The latter critique might be answered (partially) by explaining that in the brain computations proceed in parallel; however the former might require at least gesturing at work like:

Kelly, M. A., Mewhort, D. J., & West, R. L. (2017). The memory tesseract: Mathematical equivalence between composite and separate storage memory models. Journal of Mathematical Psychology, 77, 142-155.

Highlights:
- Comparative analysis points towards a unified mathematical basis for memory models.
- MINERVA 2 is proven to be equivalent to a fourth order tensor associative memory.
- A holographic lateral inhibition network approximates MINERVA 2.
- MINERVA 2 can be implemented as a fully distributed neural model.
- MINERVA 2 can be scaled up arbitrarily assuming an arbitrarily parallel computer.

### Summarizing DSMs
Really like the summary of BEAGLE; I did not really understand it until you put it so simply. Might be worth underscoring how LSA, Beagle, Word2Vec (connectionist architecture, probably most familiar of all to many students in course) all count as prototype models ("the final representation for a word is the complete pattern of weights—the prototype")

Singular Value Decomposition remains pretty mysterious, but calling it math that reduces dimensionality of word co-occurence vectors is clear enough.

## Semantic-Episodic Distinction
Students teed up an interesting discussion of neural evidence of dissociations between the episodic and semantic memory system: 

> I think semantic memory as retreival from episodic memory vs. semantic memory as as separate encoding system are both reasonable and interesting positions. However, I do wonder how the former theory would explain dissociations between the episodic and semantic memory system, for example, why children with developmental amnesia after neonatal hypoxia/ischemia develop relatively functional semantic memory systems despite severely impaired episodic memory (e.g., https://doi.org/10.1016/j.neulet.2018.04.040)
>
> On the other hand, maybe the former position better explains why adults with acquired amnesia demonstrate impoverished semantic memory, even for concepts acquired well before their injuries (e.g., https://doi.org/10.1016/j.neuropsychologia.2015.10.017). If accessing semantic memory requires retrieving and reconstructing episodic memories, you would expect people with amnesia to demonstrate a lack of depth and richness in their semantic associations.

> I know there is some recent debate about whether the semantic-epsidodic distinction is valid (https://doi.org/10.1016/j.tics.2019.09.008) from a neuroimaging & behavioral perspective. There is some evidence of overlapping neural correlates, and close behavioral ties, but I still think the dissociations that have been found eg in the clinical literature are convincing--and I wonder what instance theories would have to say about this

Could approach in a few ways. Could evaluate this evidence, talk up the value of delving into ideas before shooting them down, could bring up theories that combine prototypical and instance-based accounts of memory but emphasize the value of exploring how much behavior can be accounted for solely w/ instance-based models, or could just review how instance theorists tackle the issue. I don't have relevant citations though.

## Artificial Language Corpus (Table 1)
Generate a corpus of experiences to serve examination of ExemplarModel

`words` are represented as a unique vector where each dimension takes a randomly sampled value from a
normal distribution with mean zero and variance 1/n. Experiences are encoded as the sum of the word vectors
occurring in a given context.

A simple artificial language is constructed to generate a corpus of experiences (specified in Table 1 of
paper), consisting of 12 words sorted between 7 lexical categories and 3 sentence frames grammatically
specifying how triplets of words from different categories can be associated within a verbal context.

To explore whether an exemplar model can predict human judgements even in the case of homonyms - words with
the same spelling/pronunciation but different meanings - 20,000 grammatical sentences are sampled from the
artificial language and encoded as experiences for an ExemplarModel instance.

## Using Context to Disambiguate the Meanings of Homonyms
This section brings up MDS and uses it to make plots for Figure 1 and 2, but it's not explained what MDS is. 

Given a distance matrix with the distances between each pair of objects in a set, and a chosen number of dimensions, N, an MDS algorithm places each object into N-dimensional space (a lower-dimensional representation) such that the between-object distances are preserved as well as possible, enabling plots on a scatter plot for N=2, for example. So MDS is a backhanded approach to dimensionality reduction.  

Maybe important to clarify what disambiguation means here. A word's meaning is disambiguated by a model if the representation associated with a word and its sense-disambiguating context by the model is especially similar to that of words that mostly only occur in that sense-disambiguating context. Presenting "break/car" and finding that the result is more similar to your representation for "stop" than for "report" or "smash"

Also probably worth highlighting that LSA and BEAGLE are just fine at disambiguating the contextually appropriate meanings of words in the artificial language. Makes the final critique of distributional models way more subtle that might be guessed from the intro: distributional models can be sensitive to context, after all.

## Analysis of Disambiguation When Homonym has a Dominant Sense
Reconstructed artificial language again such that polysemous words primarily occur in one sense instead of being evenly distributed.

Students seem confused why LSA (with BEAGLE) fails in this experiment but not ITS. Indeed, Jamieson et al only really gestures at an explanation of why: it reiterates that an instance-based model can produce nonlinear activation of stored instances, while DSMs cannot.

It may be worth working through what this means why this matters, since it's the core of the critique. In ITS, the representation associated with a cue combining a word and a sense-disambiguating context (e.g. break/car) is generated by taking the product of activations associated with each word. The result is that representations in stored traces only figure substantially in the final resulting echo if they're similar to all words in the probe.

In either LSA or BEAGLE, retrieval is linear: the centroid of the vectors associated with each word in a cue is used for comparisons w/ other words. The vector for "break" will always reflect a composition of all the contexts it was presented in, weighted by the statistical distribution of those contexts, and the same goes for "car". 

Technically, ITS could do this, too - the centroid of the echoes associated with each word in a context could be taken. (We actually do this in ICMR to achieve performance that looks like CMR's). But while ITS also has the option of building semantic representations through nonlinear coactivation of traces, linear sense disambiguation is distributional models' only option. 

This is a huge problem. At encoding, distributional models and ITS get the same scarce information about relatively uncommon use contexts for polysemous words, but distributional models discards - or constrains access to, depending on how you look at it- much of this information by the time retrieval happens. ITS's retrieval mechanism is more flexible: it can selectively retrieve the traces where ONLY both of the words in a joint probe occur while inhibiting activation of traces where they don't (with its cubic function). **DSMs constrain retrieval via the integrative commitments it makes at encoding.**

The natural language experiments are a no man's land for me tbh. I have never actually read them. 