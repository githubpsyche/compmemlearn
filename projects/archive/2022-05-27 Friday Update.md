## Main goals for this week...
- Finalize results
- Draft a robust introduction/discussion

Not quite done at either. Why not?? A lot of shifting chairs around?

## Milestones this week...

### Reviewing Subtle Variations
There are signs I'm observing meaningful difference in model performance accounting for the Lohnas and Howard, Kahana datasets even with our current model version, but I'm suspicious of these results. So I took the time to review and clean up the code

I reviewed the various branches taken to get to our current version of ICMR, focusing on the subtle modifications I made thinking they could be behind degraded performance. In reverse chronological order, these include:

- Single stack vs two stack model architecture
- Applying learning rate modulation before rather vs after activation modulation
- Echo- vs Trace-Based Activation Scaling
- Activation Scaling when retrieving any associations vs only when retrieving C->F associations

The decisions for 1 and 4 seem sound and the decision for 3 seems necessary to set up the architecture comparison. The decision for 2 is easy to argue for, but I'm not 100% it's actually relevant now that we're doing the dual store implementation. 

There are signs I'm observing meaningful difference in model performance accounting for the Lohnas and Howard, Kahana datasets even with our current model version, but I'm suspicious of these results. So I took the time to review and clean up the code these model implementations and started a full comparison between each possible configuration of the first 3 of these commitments. I'll choose the best or most consistent of the models found, note any consistencies across models, and maybe mention the others in a paragraph or separate appendix or in model documentation. I won't pursue any further variations after these results arrive.

### Updated Model Comparison Code
Following our decision to fit the models to each subject separately, I was generating wAIC scores for each model and for each subject and then plotting the distribution for each model. But Morton & Polyn (2016) seems to have aggregated log-likelihoods across subjects and derived wAICs from the results. Aggregating scores to generate a single wAIC seems to make model comparison results more decisive.

I'm also still tracking mean log-likelihoods, t-statistics, and the ratio of subjectwise model outperformance. These values weren't used in the Morton & Polyn paper, but are popular in other modeling papers I've seen (like Nosofsky's). The story that the models work similarly seems clearer if I use the latter method, but less clear when I use wAICs.

Unfortunately still finalizing results based on these changes.

### Completed Literature Review
Anderson's chapter about linear associators and prototype models is apparently a recurring theme across many of his papers during the 90s. At any rate, the math there clarify what was mostly sort of gestured at (with either language or empirical contrasts) in other papers I've read: how and when snf why prototype models make different predictions from instance models loaded with the same representations. 

At minimum, these enable a pretty incisive introduction and discussion if I pull it off right. They could also motivate some decent follow-up simulations or analyses if we decide they're worth it.

In particular, they predict a concrete scenario we can computationally search for given a dataset and two fitted models when the models should disagree most about how likely a recall will be. Prototype models should be most confident about a response when the cue is highly similar to the "center" of training instance representations associated with that response. Due to their nonlinear trace activation scaling mechanism, instance models don't build prototype representations so readily and should be most confident when cues are highly similar to a specific training instance. 

I'm imaginng that we can illustrate this principle by building a scatter plot of sorts across recall events in our datasets relating model disagreement about each event's probability with the ratio of the recall cue's proximity to its nearest prototype over its proximity its nearest training instance. Anderson's account further suggests that these discrepancies should be more frequent in lists with more item repetitions that are less spaced apart. Still mysterious though is 1) how recall cues relevant for model competition might emerge organically during free recall and 2) whether the similarity structure between contextual states paired with the same item can really lead to formation of prototype effects like in Anderson's demo. I'm happy to just cover all this in a future directions section though.

I'm not looking to decide the contest between instance and prototype models with this paper, but I think something along these lines will propose a convincing strategy for probing deeper if a reader wants to.

Though what I've read suggests we need more exemplars per item to find a difference, it also implies that the comparisons we're doing are still well motivated, especially if our project is mainly to say you can use ICMR just like PCMR without losing anything. If there was going to be a difference between the models in a preecisting dataset, it was going to happen in the Lohnas or Howard datasets, not one of the datasets probing semantic organization.

## Outcomes
Big suggestion: use dot product instead of cosine similarity and make sense of the difference.

Sean still really wants to see updated results. I do too

## Fitting Results
I did these fits to:
1. Ask whether a particular implementation of ICMR performs the most equivalently with PCMR on the right datasets (Lohnas condition 1, Murdock 1962, Healy Kahana 2015).
2. Confirm that differences between ICMR and PCMR on more mysterious datasets were driven by the former's nonlinear trace activation scaling mechanism. 

I'll be happy when I have a version of InstanceCMR without trace-based activation scaling that works as well as PCMR on all datasets, and when ICMR with trace-based activation scaling works as well as PCMR on single-presentation datasets.

I get an assertion error in some of my fits. This is probably a 0 log-likelihood. I should figure out when/why so I can confirm the best course is just to remove the assertion. I imagine there are some parameters of CMR that create this situation. 

Affected ntoebooks at minimum include:
- Double healykahana
- Double lohnas kahana 2014
- double murdock 1962
- double murdock ll40
- double murdock non ll20
- double murdock not ll40

Also Lohnas Kahana Single expired.

Advantages for PCMR:
- double Howard kahana finds advantage for prototype. 
- doulbe howard kahana condition 1
- double lohnas kahana condition 1
- double lohnas kahana condition 4
- single howard kahana 05.
- single howard kahana condition 1
- single lohnas kahana condition 1
- single lohnas kahana condition 4
- single murdock 1962
- single murdock ll20
- single murdock 62 ll40
- single murdock not ll 20
- single murdock not ll40

Advantages for ICMR:
- Double Murdock 1962 LL20. ICMR_2_1_1. That's context sensitivity free, learning rate after scaling.
- single healykahana. icmr 1-1-1. 

Pretty crappy showing. Bug seems isolated to double stack model.

Forced to conclude that models really do differ even in the single presentation case and even after all my changes.

Next steps will have to include...
- Identifying and fixing the bug in double stack variant
- Switching to dot product association testing
- Updating library version on ACCRE
- Running fits and performing comparison against old versions

I won't have to redo fits for old versions if they finished, unless I find that the bug in double was throwing stuff off.

I should also see if there are any systematic patterns across my model changes...

What's the most efficient plan of attack for this?

I'll pick the smallest dataset where double stack didn't finish fitting and performance should be the same. I'll go ahead and produce the dot product variant. Then I'll re-execute fitting for both variants of the double stack model while retrieving results from PCMR for comparison. I'll work to get the entire notebook to run locally and then on ACCRE. Once I suceed, all those steps above will have been successful or ready for success through a more extended follow-up.

Think it's murdock ll 40. 

What does the dot product model look like? Is it really more equivalent to the PCMR? 
It's probably more similar, but the output of a probe operation should still be a bit different when there's a partial mismatch. A partial mismatch in an instance framework  just retrieves a little less of the associated representation. A partial mismatch in a linear associator selectively retrieves part of the associated representation based on the parts that are similar. These can have distinct consequences for retrieval separate from the question of prototype vs instance model.

If that's true, how do I distinguish between the scenario where ICMR isn't a parallel implementation and the scenario where linear associators are just better at retrieving the appropriate representation? Code review, I guess. And then consideration of how predictions differ. I'm going to have to implement the comparator at some point. 

Dot product model shouldn't matter here. Cosine similarity is just a dot product divided by product of vector norms. Probe norm is always 1. Vector norm is either one value or another based on pre-experimental/experimental divide. This means my learning parameters that vary based on pre-experimental/experimental divide already account for it unless I'm still letting context magnitude drift or creating other issues. The best reason not to switch to dot product so I can store learning rate is that applying learning rate afterwards should improve fits.

I think my results with echo cmr and the learning rate thing imply that my fitting method isn't robust/high resolution enough. So I'll also need to remember how Neal did it and approach some of that sophistication.