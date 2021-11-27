## Model Paper Drafting
Here we progressively sketch out plans for what might appear in an eventual paper. This is worth considering separately from but concurrently with model development and exploration since 1) writing a scientific paper is a different kind of task from doing and even documenting the associated research, and 2) considering what a scientific paper about ICMR might look like can help organize the course of the actual project. Sections should be updated as research worth reporting in a paper gets completed.


### Title


Working title can just be "An Exemplar Model of Context Maintenance and Retrieval". Probably should pick a title that uses more accessible language. May consider other model papers to see how their titles are structured.


### Abstract


Should premise with the concrete research question about relating connectionist and instance models of human memory and the possibility of an integrated model of the phenomena they are both well-suited for. "We investigate properties of exemplar and connectionist models of human memory..." or something. Background should specify these two models and why they’re interesting and their non-overlapping gaps. Then I’ll outline the model development process, the kinds of tasks we’ve developed simulations for, and outcomes. Then I'll emphasize 'novelty': what do we get that the model that we couldn't get from previous iterations? Conclude with talk about equivalence relations between instance-based and connectionist models. The other details here can go to the introduction.


### Introduction


Guidance goes like this:
> The first paragraph of the introduction describes the general area of research.
> The middle paragraphs summarize past research studies (the “bricks”) and give your interpretation of their meaning and importance (the “mortar”), arranged in a way that logically leads to my hypothesis.
> The last paragraph briefly describes the method used and the primary variables studied, and they state the hypotheses or research question.

What’s that mean here? We want to describe, contrast, and propose syntheses between instance and connectionist models of memory performance, as well as between the kinds of phenomena that these models are designed to account for. Outlining the work on these models and the surrounding phenomena they account for, and connecting them to build up to our approach to making something that deals with both is key. I don’t have enough references yet to pull this off.

Where should I start? Find a review paper on CMR and on instance models. Identify for each model, list of relevant tasks, analyses. Also identify concepts that don’t get any coverage, and any lack of overlap between specified model functions. And then look for other work that’s addressed these gaps. Of course for now the top priority is obtaining a working instance model that can reproduce classic organizational properties in free recall that CMR can. That determines the course of the rest of the paper.


### Model Specification


We'll work iteratively on text-based specification as we improve the model.


### Other Sections


We'll want a section for each relevant simulation analysis, describing them all in a reproducible and comprehensible way. Then I can talk about ‘empirical simulations’ and model fitting, where discussion of data provenance becomes relevant.

A discussion section would review what we found and outline the stuff we couldn't make the time/room for yet. Definitely premature to start workshopping this now.

We'll build a set of references below as we conduct our literature search.


## Relevant Work
It's worth keeping track of each reference we spend any substantial amount of time thinking about in relation to ICMR. Here, I'll collect citations, paper abstracts, and any paper specific notes worth holding out from the rest of the document.


### Hintzman, D. L. (1984). MINERVA 2: A simulation model of human memory. Behavior Research Methods, Instruments, & Computers, 16(2), 96-101.


An overview of a simulation model of human memory is presented. The model assumes: (1) that only episodic traces are stored in memory, (2) that repetition produces multiple traces of an item, (3) that a retrieval cue contacts all memory traces simultaneously, (4) that each trace is activated according to its similarity to the retrieval cue, and (5) that all traces respond in parallel, the retrieved information reflecting their summed output.

The model has been applied with success to a variety of phenomena found with human subjects in frequency and recognition judgment tasks, the schema-abstraction task, and paired-associate learning. Application of the model to these tasks is briefly summarized.


### Jamieson, R. K., Avery, J. E., Johns, B. T., & Jones, M. N. (2018). An instance theory of semantic memory. Computational Brain & Behavior, 1(2), 119-136.


Distributional semantic models (DSMs) specify learning mechanisms with which humans construct a deep representation of word meaning from statistical regularities in language. Despite their remarkable success at fitting human semantic data, virtually all DSMs may be classified as prototype models in that they try to construct a single representation for a word’s meaning aggregated across contexts. This prototype representation conflates multiple meanings and senses of words into a center of tendency, often losing the subordinate senses of a word in favor of more frequent ones.

We present an alternative instance-based DSM based on the classic MINERVA 2 multiple-trace model of episodic memory. The model stores a representation of each language instance in a corpus, and a word’s meaning is constructed on-the-fly when presented with a retrieval cue.

Across two experiments with homonyms in both an artificial and natural language corpus, we show how the instance-based model can naturally account for the subordinate meanings of words in appropriate context due to nonlinear activation over stored instances, but classic prototype DSMs cannot. The instance-based account suggests that meaning may not be something that is created during learning or stored per se, but may rather be an artifact of retrieval from an episodic memory store.


### Murdock Jr, B. B. (1962). The serial position effect of free recall. Journal of experimental psychology, 64(5), 482.


The serial position curve is characterized by a steep, possibly exponential, primacy effect extending over the 1st 3 or 4 words in the list, an S-shaped recency effect extending over the last 8 words in the list, and a horizontal asymptote spanning the primacy and recency effect. The shape of the curve may well result from proactive and retroactive inhibition effects occurring within the list itself.


### Morton, N. W., & Polyn, S. M. (2016). A predictive framework for evaluating models of semantic organization in free recall. Journal of Memory and Language, 86, 119-140.


Research in free recall has demonstrated that semantic associations reliably influence the organization of search through episodic memory. However, the specific structure of these associations and the mechanisms by which they influence memory search remain unclear.

We introduce a likelihood-based model-comparison technique, which embeds a model of semantic structure within the context maintenance and retrieval (CMR) model of human memory search. Within this framework, model variants are evaluated in terms of their ability to predict the specific sequence in which items are recalled.

We compare three models of semantic structure, latent semantic analysis (LSA), global vectors (GloVe), and word association spaces (WAS), and find that models using WAS have the greatest predictive power. Furthermore, we find evidence that semantic and temporal organization is driven by distinct item and context cues, rather than a single context cue. This finding provides important constraint for theories of memory search.


### Johns, B. T., & Jones, M. N. (2012). Perceptual inference through global lexical similarity. Topics in Cognitive Science, 4(1), 103-120.


The literature contains a disconnect between accounts of how humans learn lexical semantic representations for words. Theories generally propose that lexical semantics are learned either through perceptual experience or through exposure to regularities in language.

We propose here a model to integrate these two information sources. Specifically, the model uses the global structure of memory to exploit the redundancy between language and perception in order to generate inferred perceptual representations for words with which the model has no perceptual experience.

We test the model on a variety of different datasets from grounded cognition experiments and demonstrate that this diverse set of results can be explained as perceptual simulation (cf. Barsalou, Simmons, Barbey, & Wilson, 2003) within a global memory model.
