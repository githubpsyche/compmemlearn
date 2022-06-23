---
title: An introduction to neural networks
authors: James A Anderson
year: 1995
---

This chapter from an old text on neural networks is amazing. The deepest examination I've found of where simple linear associator networks sit in the prototype/instance model debate, complete with experiments, simulations, and surprisingly-actually-clarifying math. I think it provides enough background to fill in the parts of the paper where we clarify how/when switching between architectures might lead to distinct predictions.

The chapter seems to demonstrate that linear associators are pretty instance-like when learning instances are either relatively few or highly dissimilar from one another. Under those conditions, response matching is based on the nearest, or several nearest, stored instances. But something different happens if instances with the same label are numerous and similar enough. Linear associators exhibit a prototype effect: they learn a new pattern, the prototype, that may have never even existed but reflects the central tendency across instances. And response-matching is predominantly driven by similarity to this representation that was never among the learning instances. Instance models

This provides an intuition that list learning experiments with both 1) a lot of item repetitions and 2) relatively low spacing between repetitions pose the best odds of distinguishing ICMR and PCMR. At the same time, they help explain we might not observe significant performance differences in our datasets where items are repeated just once or twice. The minimum number of examples required per label to create a prototype effect like PCMR predicts isn't very high (this chapter's simulations observe a minor one even with 2 unique example representations), but is likely higher than those provided in either of the datasets we consider. There's also the issue that PCMR and ICMR both kinda suck at accounting for repetition effects in free recall in general.

How do predictions differ exactly when a model is being instance-like or prototype-like? 

In an instance-based memory, responses will tend to be most confident when a cue is particular similar to specific a training instance. In a prototype-based memory, responses will be most confident when a cue 

Cue representations vary over the course of free recall. Instance models should be most confident when a cue is especially similar to an individual learning instance. Prototype models should be most confident when a cue is especially similar to the center of learning instances sharing a common label. 

Along these lines, we can track across recall events in a dataset 
1) the similarity of the current recall cue to the nearest study instance, 
2) the similarity of the current recall cue to the nearest item prototype,
3) The confidence of our prototype model's prediction that the next recall will be of the nearest prototype's corresponding item
4) The confidence of our instance model's prediction that the next recall will be of the nearest instance's corresponding item

As a sanity check, 1/4 and 2/3 should be associated. And correspondingly, the difference between 1 and 2 should be associated with the difference between 3 and 4. We can then ask how often either model wins out in this situation, and with how frequently/under which conditions this situation arises at all. 