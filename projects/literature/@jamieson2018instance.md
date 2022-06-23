---
title: An instance theory of semantic memory
authors: Jamieson, Randall K and Avery, Johnathan E and Johns, Brendan T and Jones, Michael N
year: 2018
---
  
## Characterization of Prototype Models
>  The mechanisms posited by DSMs to transform episodic experience to semantic representations vary widely, ranging from simple co-occurrence counting to error-driven reinforcement learning (see Jones et al. [2006](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR43 "Jones, M. N., Kintsch, W., & Mewhort, D. J. K. (2006). High-dimensional semantic space accounts of priming. Journal of Memory and Language, 55, 534–552."), for a review).
>  

This review isn't very relevant.

Exactly how representations are pulled together into prototype representations is irrelevant to the characterization.

> To be clear, Word2Vec is a multilayer network; hence, it can predict the same output word (e.g., _bark_) given very different input patterns (e.g., _bark_ in the tree sense versus _bark_ in the dog sense). But the final representation for a word is the complete pattern of weights—the prototype. Two words are typically compared via the cosine of their respective vectors in all models, and so a homonym such as _bark_ will be pulled between its two senses just as it is in LSA or BEAGLE.

## Characterization of Instance Models
> . But it invokes a naïve theory for retrieval that ignores established wisdom from the study of human memory: Remembering is context dependent (e.g., Godden and Baddeley [1975](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR23 "Godden, D., & Baddeley, A. (1975). Context dependent memory in two natural environments. British Journal of Psychology, 66, 325–331.")), constructive (Bartlett [1932](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR4 "Bartlett, F. C. (1932). Remembering. Cambridge.")), and conditional on the interaction between how information is encoded and accessed (e.g., Morris et al. [1977](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR54 "Morris, C. D., Bransford, J. D., & Franks, J. J. (1977). Levels of processing versus transfer appropriate processing. Journal of Memory and Language, 16(5), 519"); Tulving and Pearlstone [1966](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR78 "Tulving, E., & Pearlstone, Z. (1966). Availability versus accessibility of information in memory for words. Journal of Verbal Learning & Verbal Behavior, 5, 381–391."); Tulving and Thomson [1973](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR79 "Tulving, E., & Thomson, D. (1973). Encoding specificity and retrieval processes in episodic memory. Psychological Review, 80, 352–373.")).

## Critiques of Prototype Models
>  virtually all DSMs may be classified as prototype models in that they try to construct a single representation for a word’s meaning aggregated across contexts. This prototype representation conflates multiple meanings and senses of words into a center of tendency, often losing the subordinate senses of a word in favor of more frequent ones.
>  
>  This shared characteristic may represent a significant architectural flaw in DSMs, leading the field to assume that semantic abstraction is a learning mechanism rather than a retrieval mechanism.

What clear evidence/predictions correspond to this criticism? When should prototype-based models fail? When should they work just fine? How does this criticism generalize beyond language, and when does it fail?

> [[@jones2017big]] has recently suggested that current “abstraction-at-learning” DSMs suffer from the same issues as prototype theories in categorization, a problem that arises from collapsing the many contexts in which a word occurs to a single best-fitting representation. Doing so discards idiosyncratic regularities that are important to word meaning. Here, we argue that homonyms present an ideal method to define and evaluate the potential shortcoming.

So it seems the idea is that problems emerge when the mean representation corresponding to a cue isn't sufficient to capture variation across different contexts (environmental cues), and rare context-specific outputs aren't as easily selectable.

> Griffiths et al. ([2007](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR22 "Griffiths, T. L., Steyvers, M., & Tenenbaum, J. B. (2007). Topics in semantic representation. Psychological Review, 114, 211–244."); see also Griffiths et al. [2005](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR21 "Griffiths, T. L., Steyvers, M., Blei, D. M., & Tenenbaum, J. B. (2005). Integrating topics and syntax. In Advances in Neural Information Processing Systems (pp. 537–544).")) have suggested that homonyms present a core challenge to spatial DSMs that the models cannot adequately explain, arguing instead for probabilistic topic models.

> Prototype DSMs lose the tail when collapsing to a prototype, but humans can regularly comprehend the multiple less frequent meanings that are averaged out in DSMs. Hence, DSMs have great difficulty with the subordinate senses of homonyms (e.g., the river sense of _bank_ is dominated by the financial institution sense in the prototype representation). Thus, disambiguating the meaning of homonyms constitutes a valid falsification criterion for DSMs that posit abstraction at learning.

Is this still a problem now? Sort of. It's just kinda addressed by model complexity.

> We conclude that the common criticism (see Griffiths et al. [2005](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR21 "Griffiths, T. L., Steyvers, M., Blei, D. M., & Tenenbaum, J. B. (2005). Integrating topics and syntax. In Advances in Neural Information Processing Systems (pp. 537–544)."), [2007](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR22 "Griffiths, T. L., Steyvers, M., & Tenenbaum, J. B. (2007). Topics in semantic representation. Psychological Review, 114, 211–244.")) of LSA and, by corollary, related prototype models is valid when comprehending a homonym’s subordinate sense.

> But ITS is also able to explain subordinate senses of homonyms in context due to nonlinear activation of language instances, where prototype DSMs lose the distinction due to their aggregated representation.

> Across two experiments with homonyms in both an artificial and natural language corpus, we show how the instance-based model can naturally account for the subordinate meanings of words in appropriate context due to nonlinear activation over stored instances, but classic prototype DSMs cannot.

What does "naturally account for" mean here?

> In contrast to abstraction-at-learning DSMs, an instance-based model can produce nonlinear activation of stored instances, which allows it to access the subordinate sense of a word when provided the appropriate cue (e.g., _bank_ as in the sense of turning a plane rather than _bank_ in the sense of financial instructions). The model is able to account for traditional phenomena that have been used as support for DSMs. But, it can also explain patterns of responses to subordinate meanings of a word in context that are difficult to account for with traditional DSMs, and to do so without the requirement for an explicit store for semantic memory per se.

## Categorization Literature
[[Critiques of Prototype Models in the Categorization Literature]]

> However, the notion of building a single prototypical center of tendency disagrees with the current state-of-the-art in related fields of cognition, such as categorization and episodic memory. The categorization literature, for example, has largely converged on the superiority of exemplar-based theories over prototype theories because prototype theories cannot explain human behavior when dealing with category structures that have nonlinearly separated structure, such as in classic XOR. Even if linear category structures are used that should be optimal for prototype models, exemplar models produce a superior quantitative prediction of human data (e.g., Stanton et al. [2002](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR72 "Stanton, R. D., Nosofsky, R. M., & Zaki, S. R. (2002). Comparisons between exemplar similarity and mixed prototype models using a linearly separable category structure. Memory & Cognition, 30, 934–944.")).

Is this an overstatement? He mentions "episodic memory" but this reference solely cites a categorization literature paper. 

> Although we have provided an instance-based DSM to encode word meaning from language experience, Storms et al. ([2000](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR74 "Storms, G., De Boeck, P., & Ruts, W. (2000). Prototype and exemplar based information in natural language categories. Journal of Memory and Language, 42, 51–73."))) have examined the distinction between an instance-based and prototype-based approach to natural language classification. In that work, they relied on the generalized context model (Nosofsky [1984](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR61 "Nosofsky, R. M. (1984). Choice, similarity, and the context theory of classification. Journal of Experimental Psychology: Learning, Memory, & Cognition, 10, 104–114."), [1986](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR62 "Nosofsky, R. M. (1986). Attention, similarity, and the identification-categorization relationship. Journal of Experimental Psychology: General, 115, 39–57.")) rather than the MINERVA2 framework. In some of their work, the evidence favored an instance-based conclusion (Smits et al. [2002](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR71 "Smits, T., Storms, G., Rosseel, Y., & De Boeck, P. (2002). Fruits and vegetables categorized: an application of the generalized context model. Psychonomic Bulletin and Review, 9, 836–844."); Voorspoels et al. [2008](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR82 "Voorspoels, W., Vanpaemel, W., & Storms, G. (2008). Exemplars and prototypes in natural language concepts: a typicality-based evaluation. Psychonomic Bulletin and Review, 15, 630–637.")). In other work, their evidence favored an intermediate representation somewhere in between an instance and prototype representation (Verbeemen et al. [2007](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR81 "Verbeemen, T., Vanpaemel, W., Pattyn, S., Storms, G., & Verguts, T. (2007). Beyond exemplars and prototypes as memory representations of natural concepts: a clustering approach. Journal of Memory and Language, 56, 537–554."); Voorspoels et al. [2011](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR83 "Voorspoels, W., Vanpaemel, W., & Storms, G. (2011). A formal ideal-based account of typicality. Psychonomic Bulletin and Review, 18, 1006–1014.")). Taken together, their work suggests that it may be naive to pit the instance and prototype DSMs against one another as though they were mutually exclusive.


## Etc
solving a toy problem does not guarantee a solution to the problem at scale (e.g., Feldman-Stewart and Mewhort [1994](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR18 "Feldman-Stewart, D., & Mewhort, D. J. K. (1994). Learning in small connectionist networks does not generalize to large networks. Psychological Research, 56, 99–103.")).

The notion that semantic abstraction may be better conceptualized as a retrieval mechanism rather than an encoding mechanism was originally posited by Kwantes ([2005](https://link.springer.com/article/10.1007/s42113-018-0008-2#ref-CR48 "Kwantes, P. J. (2005). Using context to build semantics. Psychonomic Bulletin & Review, 12, 703–710.")).

