# Prototype and Instance Theory Competition
Prototype-based models collapse the many contexts in which items are observed into a single best-fitting representation that best represents the item's associations. 

An instance-based model can produce nonlinear activation of stored instances based on a provided cue, enabling more flexible retrieval of highly relevant instances.

We're interested in clarifying the conditions under which prototype and instance models make different patterns of predictions given the same data and the opportunity to fit models.

### Word Sense Disambiguation
[[@jamieson2018instance]]

1. The task of learning and retrieving word->context associations
2. Some words are "homonyms": they tend to occur in multiple distinct clusters of contexts
3. Prototype models represent words with just one pattern, so a homonym such as _bark_ will be pulled between its two senses.
4. Instance model ITS can better access subordinate word senses through nonlinear activation of language instances

Episodic memory models use temporal contextual representations as cues to retrieve appropriate item representations. 

Distributional semantic models use orthographic representations as cues to retrieve appropriate distributional representations or meanings.

The advantage of instance models in this paradigm depends on orthographic representations being paired with distinct clusters of contexts, with one cluster pairing substantially more prevalent than the other(s). When this happens, prototype representations of a word's meaning are pulled so hard toward dominant senses that information about subordinate senses gets discarded to an extent that doesn't match patterns in human behavior.

To create a similar contrast-enabling design in the list-learning paradigm, a given temporal contextual state would have to be repeatedly matched with one "dominant" item as well as more rarely with some "subordinate" item. We might also find that humans are better able to retrieve the subordinate item more easily given this contextual cue than predicted by our prototype model. However, designs even remotely like these are rare in episodic memory research; by their very nature, it seems impossible to control and/or measure temporal context-item pairings in the way that word-context pairings can be measured.

### Category Learning
But the broader theme is at least clearer: The big predictive difference between our architectures is that one assumes generalization is based on similarity to a learned prototype, and the other assumes that generalization is based on similarity to specific old exemplars. 

If features of studied exemplars are themselves ambiguous about category membership, models make different predictions about how similar testing exemplars will be classified.

More generally, compared to prototype models, instance models more confidently predict the successful classification of test instances that are highly similar to specific training instances, even when their features are otherwise ambiguous about category membership.

1. The task of learning and retrieving multi-featured items -> category associations

#### Contrast by Critical Training Stimuli
[[@stanton2002comparisons]]

2. Attended features of a "critical training stimulus" can be ambiguous for category membership even though a label is assigned.
3. Later, novel "neighbor" transfer stimuli can be distinct from but have the same attended features as critical training stimuli. 
4. Prototype models assume neighbor stimuli are classified with roughly equal probability into categories based on prototype similarity.
5. Instance models assume neighbors are classified into the category of their matching training stimulus based on instance similarity.

This is a graded effect, not absolute, aiming to qualitatively explain patterns of model performance.

If we wanted to test the prediction in the context of episodic memory, we'd need to create or identify temporal contextual states in the study phase whose relevant features are ambiguous about which item is the appropriate response supposing those states were cued again. Those would be our **critical training stimuli**.

Next, we'd need to make or identify novel temporal contextual states in the recall phase whose relevant features match the relevant features of critical training stimuli. These are our **neighbor** transfer stimuli. 

Finally, we'd need enough recall events based on neighbor stimuli and a good analysis method to measure whether recall tends to be driven by instance- or prototype- comparison in these situations.

It's difficult to imagine a situation like this in traditional list learning datasets. The fact that temporal contextual states are latent variables whose configurations are only estimated through model fitting and simulation adds a level of complexity. On the other hand, the "feature attention" construct used in the category learning papers I've seen are also latent states discovered through the model fitting.

#### Contrast by Exception Stimuli
[[@nosofsky2002exemplar]]

2. "Exception stimuli" studied as members of category A can be presented with exceptional features that make them more typical of category B.
3. Prototype models tend to predict that similar new items will be classified into the opposite category to which each exception belongs.
4. Instance models tend to predict that such transfer items will be classified into the same category as their matched exceptions.
5. The same principle as critical training stimuli, but training stimulus features are not just ambiguous, but misleading about category membership.

#### Contrast by Prototype Distortion
[[@nosofsky2002exemplar]]
2. Constructed transfer stimuli that were either low, medium, or high distortions of the predicted prototype representation for a category.
3. Prototype model struggle to account for rare HIGH distortion exemplar classification without underpredicting the rate of successful LOW or MEDIUM.  
4. Adding a response scaling process seems to address this deficit in prototype models, proving it's necessary for both architectures.

### Nonlinear Category Structures
[[Nonlinear Category Structures]]

