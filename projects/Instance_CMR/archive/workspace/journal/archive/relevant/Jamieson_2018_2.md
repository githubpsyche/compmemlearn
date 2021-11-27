# Jamieson 2018, Natural Language Experiments

## Why
Solving a toy problem doesn't guarantee a solution to the problem at scale.

References Feldman-Stewart and Mewhort (1994) as an example. That paper finds that learning in small connectionist networks does not generalize to large networks; some patterns hold for the former but not for the latter. For example, increasing the rate-of-learning parameter beyond 1 increases the rate of learning in considered experiments, while in large networks the same manipulation reduced the rate of learning. This implies that research focused on small networks can't be assumed to generalize effectively to large networks, discrediting their use for exploring toy problems.

Feldman-Stewart, D., & Mewhort, D. J. K. (1994). Learning in small connectionist networks does not generalize to large networks. Psychological Research, 56(2), 99-103.

## Taxonomic Structure
Test difference between models' ability to recognize taxonomic category. 

> For example, a competent theory of semantics should recognize that items from the category of animals are more similar to one another than they are to items from the category of vehicles.

All three models do a good job of identifying which words belong to the same category and which do not, as visualized by another MDS analysis.

## Disambiguating Meaning in Context
A lexical decision task where participants had to identify strings as either words or nonwords as quickly and accurately as possible. 

Three successive letter strings were presented and decisions were always about the third string. Trials were either cued or miscued. On cued trials, first two strings cued the appropriate meaning of the third string (e.g. "save" and "bank" both apply reasonably to "money"). On miscued trials, first two string cued an inappropriate meaning (e.g. "river" and "bank" don't fit with "money"). Participants are faster to identify the third owrd on cued than miscued trials, a quasi-priming result.

To test models, representations were retrieved using the first two strings, and compared to the echo of the last string. Hypothesis: higher similarity between cues and test string will be found for cued rather than miscued trials.

Initial results also find that prototype and DSM models disambiguate words effectively in this experiment. So a follow-up was performed. 

Examined performance for individual items in the stimulus set, supplemented by separate participant ratings on the semantic ambiguity of homonyms. 0 for maximally ambiguous, 1 for super clear. 36 words, 27 listed in Table 3, were in both datasets.

For really ambiguous homonyms, ITS's cue->test string comparison tracked the cue/miscue distinction more reliably than LSA's or BEAGLE's!

