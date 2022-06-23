# Similarity-Driven Contextual Reinstatement as a Unifying Concept in List Learning and Narrative Comprehension

## Premise
According to Retrieved Context Theory, 
1. Each study event in a list learning experiment is associated in memory with temporal context, a representation that reflects your recent experiences. 
2. When you study an item in a list-learning experiment, you're reminded of past experiences with that item. You retrieve its pre-existing contextual associations and integrate that into the current temporal context.

These two points have really interesting implications in a list with item repetitions such that the item was studied at two positions, $i$ and $j$. When you see the item at position $j$, you reinstate the temporal context from when you saw it at position $i$.

Because of (1), a side effect of this reminding is that neighbors of the item's first presentation ($i+1$, $i+2$) will also get reinstated into context. This information will persist in context for a few study events, so the item's first presentation neighbors can end up independently associated in memory with the item's second presentation neighbors. Even though the items at $i+1$ and $i+2$ were never restudied! 

Lynn worked out this implication and showed that this neighbor contiguity effect is both predicted by CMR and also shows up in behavioral data. When people later recall an item in {$i+1$, $i+2$}, they transition to recalling items in {$j+1$, $j+2$} at rates much higher than chance. Even if they never actually recall the item repeated at positions $i$ and $j$!

The way this ties into semantic or narrative memory though is that this analysis is useful for detecting *any* reminding effects in a free recall experiment. Lynn's results show that when you see an item for the second time in a list learning experiment, you're reminded of the first time you saw it in a way that alters the representations you eventually use to perform recall.

We can similarly ask if this happens when you see **two distinct but highly related ideas** in a study sequence. 

If I see the word KING at position $i$ and then the word QUEEN at position $j$ in a study list, do I get reminded of my experience of the word KING in a way that shapes how I process the list going forward and later remember it?

If I read a sentence about how dangerous wild animals are at one point in a narrative and then a bear shows up later, do I get reminded of the "wild animals" sentence in a way that shapes how I process the story going forward and later remember it?

I'm pretty sure a positive answer to the latter question is already common knowledge in the narrative comprehension literature -- they call the phenomenon [bridging inference](https://en.wikipedia.org/wiki/Text_inferencing#:~:text=Backward%20inferences%20require%20the%20reader%20to%20bridge%20the%20current%20text%20idea%20to%20one%20that%20occurred%20earlier%20in%20the%20text.) and make a big deal about it. Most theory competition in the narrative comprehension literature concerns when and how readers perform bridging inferences to comprehend a text.

But showing that it's also a thing in list learning to the extent that you can measure it in behavior and account for it with changes to a model like CMR might be a great bridge between the literatures. It would draw a direct line from this core idea in narrative comprehension — backward inference — to a core idea in the list-learning literature — context reinstatement. And hopefully set the stage for a unified account of both processes.

## Experiment 1: Demonstrating the Principle
To investigate whether similarity-driven contextual reinstatement organizes the list learning process, we can start by replicating part of Lynn's 2016 experiment.

Participants were presented with control lists and mixed lists. Each list contained 40 unique positions. In the control lists, 40 unique items were presented just once. In the mixed lists, 6 pairs of repeated items were mixed among 28 once presented items. Across lists, there were an equal number of item pairs repeated at spacings of lag $\in$ {0, 1, 2, ..., 8}, where lag is defined as the number of intervening items between an item's repetitions. 35 subjects saw lists of each type 12 times over 3 sessions. 

To analyze the data, Lynn measured the percent of transitions made between items that follow the presentation of the same repeated item. If an item was presented at positions $i$ and $j$, and if one of the items was recalled from either $S_j = {j + 1, j + 2}$ or $S_i = {i + 1, i + 2}$, they then counted the percentage of times that a transition was then made to one of the items in the complementary sets $S_i$ or $S_j$, respectively.

To measure the percent of transitions expected by chance, over 100 reshuffled datasets, repeated items in control lists were matched to the same serial positions as the repeated items in mixed lists, and the percentage of transitions was counted.

To measure similarity-driven contextual reinstatement, we can replicate these results and add a condition similar to our mixed list condition. Whereas in mixed lists, 6 pairs of repeated items were mixed among 28 once presented items, in our additional condition we can use 6 pairs of items with high semantic similarity to one another but low semantic similarity to other list items. The remaining 28 items will be enforced to have comparatively low semantic similarity to all list items. Then to analyze the data, we can measure the percent of transitions made between items that follow the presentation of items in the same pairing.

If we observe that this percent of transitions is significantly higher than chance, we can conclude that similarity-driven contextual reinstatement influences list learning and the course of free recall.

If we don't, but under the same conditions can replicate Lynn's results regarding the mixed list condition, we can surmise that similarity-driven contextual reinstatement does not influence list learning.

### Modeling
With data from Experiment 1 and by integrating a similarity-driven contextual reinstatement mechanism into CMR, we can also test the hypothesis through model comparison. We can demonstrate that the mechanism contributes unique predictions about the outcome of our neighbor contiguity analysis in our novel experimental condition. And through likelihood-based model fitting, we can show these differences either improve or worsen the model's capacity to account for applicable datasets overall.

The mechanism would alter how the model calculates contextual input, $c^{IN}_i$, during list learning. In the classic specification of CMR, $c^{IN}_i = M^{FC}f_i$, where $M^{FC}$ is a matrix that learns associations between orthogonalized item representations and contextual states. In a modified model, we might maintain a parallel memory structure $M^{sem}$ that learns associations between distributed semantic representations of items and contextual states. This way, contextual reinstatement upon processing an item will be graded based on the similarity of the item's semantic representation to semantic representations of other items in memory. 

These associations may prove easier to implement within an instance-based architecture than a traditional linear associator model. A nonlinear activation scaling mechanism could be used to control the extent to which similar items' contextual representations are reinstated upon item processing.

## Experiment 2: Generalization to Arbitrary Word Lists
A natural follow-up to our results in Experiment 1 is to generalize the experiment to arbitrary word lists. Using benchmark datasets from Morton & Polyn (2016), we can perform model comparison to evaluate whether the hypothesized mechanism can generalize to improve CMR's account of memory for word lists with less structured similarity relations between studied words.

These results would help clarify the scope of results in Experiment 1, ruling out or confirming that...
1. the design of our original experiment influenced subjects to process paired high-similarity words like item repetitions, but that subjects do not do so naturally.
2. similarity-driven contextual reinstatement can influence free recall even when semantic similarity is not enforced to high levels.

## Experiment 3/4: Generalization to Written Narratives
Finally, we can attempt to generalize our results to memory for written narratives.

Two approaches are possible. On the one hand, we can try to create narratives whose structures mirror those of the control, mixed, and similarity-pairing lists from our Experiment 1. Each narrative can contain a connected sequence of 40 "idea units", or subjects/predicates in single words or phrases. In our "control" narratives, we'll enforce idea units to be unique and have low similarity to one another. In our "mixed" narratives, 6 pairs of repeated idea units can be mixed among 28 once presented idea units. And in our similarity-pairing condition, we can use 6 pairs of idea units with high semantic similarity to one another but a low semantic similarity to other idea units. The remaining 28 idea units will be enforced to have comparatively low semantic similarity to all idea units. 

This design might enable a clear demonstration of a similarity-driven contextual reinstatement mechanism in narrative recall but seems to require constructing very unnatural stories since a typical narrative includes some item repetition. So alternatively, we might use naturally structured narratives identified from previous research into narrative comprehension, and apply the likelihood-based model comparison technique from Morton & Polyn (2016) to evaluate how including a similarity-driven contextual reinstatement mechanism in CMR influences the model's ability to account for narrative recall datasets.

At the same time, we'd also be evaluating retrieved context theory itself as an account of narrative recall. We may include implementations of other comprehension models in this analysis.

## Discussion
So what do we get from all this trouble? Ideally, theoretical unification. 

Similarity-driven contextual reinstatement is a powerful mechanism wielded in models of narrative comprehension to account for readers' ability to organize otherwise seemingly disjointed text ideas into a coherent discourse representation. It may also be an important way semantic knowledge shapes new episodic memories in general. These proposed experiments suggest a way we might convincingly connect these ideas under a single familiar theoretical framework -- retrieved context theory.

Our extension of the neighbor contiguity analysis from Lohnas & Kahana (2016) gives us a way to cleanly demonstrate the behavioral predictions suggested by the mechanism under controlled conditions and independently of formal theoretical commitments. It also helps us focus on a specific mechanism/theme instead of a general memory account as we go forward.

Similarly, the likelihood-based model comparison technique from Morton & Polyn (2016) gives us a way to evaluate the effectiveness of the mechanism as part of a complete account of memory search under more general experimental conditions.

Proceeding to use connected narratives rather than structured word lists to evaluate our model allows us to connect our findings, methods, and ideas to debates in the narrative comprehension literature, and vice versa.

Our extension of CMR can be validated as an account not just of memory search, but of story understanding. Our toolbox of free recall analyses can provide novel theoretical constraints for the study of narrative comprehension. And in turn, a vast literature of ideas and techniques exploring how rich semantic associations form can inform the broader study of semantic and episodic memory. 

Some natural follow-up questions:
- How does extended CMR compare to other accounts of narrative comprehension?
- Apply benchmark recall and repetition effect analyses to list and narrative recall datasets and compare the results.
- ...