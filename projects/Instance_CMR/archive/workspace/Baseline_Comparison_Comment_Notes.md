# Baseline Comparison Comment Notes

**sean.polyn**: I think the value of this section could be enhanced if you first present the overall fits, and then add some analyses at the end of the section specifically showing how the two models give rise to the "benchmark phenomena". Or rather, specifically the recency effect and the contiguity effects.   This could be a figure where the simulated PFR curves are presented for each model, side by side, and each one is showing a family of curves with a particular parameter being adjusted… so like this could just make the simple point, for the PFR, that the same parameter Benc determines the sharpness of the recency effect in both models.  Could also have two more panels showing that recency sharpness is also affected by the tau / exponentiation parameter in both versions of the model
**sean.polyn**: That would be followed by a similar examination of the lag-CRP, showing that you can manipulate the sharpness and forward asymmetry in both models… they have similar degrees of flexibility

Hmm this is an interesting point. So the first set of results is also the section where I clarify how the model works. Reminds me of the Jamieson et al paper, okay. So to be clear, I first present results like I'm already doing. Then I clarify how models give rise to these phenomena okay. Cool yeah that's way better discourse.

**sean.polyn**: 
> where each item is presented just once per study phase
The significance of this phrase isn't clear, maybe not necessary to re-state this here

Yeah, its significance is only clear in relation to the Repetition analyses, where I can emphasize the distinction just there. Okay. Sentence seems sort of bare with that phrase gone though.

**sean.polyn**: OK so the first paragraph/block of text says the big take-away, which is that the 3 models performed similarly well. Now you need to describe Fig 2, which examines 2 of the 3 models from Fig 1. It is a straightforward story you are trying to tell here! The neural net CMR and the instance CMR both do well. This is in itself a victory because no one has implemented an instance-based CMR before, so you've demonstrated that it can be done, and that the model doesn't suffer from any obvious deficiencies.

**sean.polyn**: So you want to have a good topic sentence again, which establishes how and why you made the panels in figure 2.
**sean.polyn**: There's what you did, and then there's why you did it. 
What you did: Took the best fitting parameter set for each participant, used it to generate a bunch of recall sequences, ran 3 benchmark behavioral analyses on those recall sequences and compared them to the same analyses run on the empirical data. This doesn't really strike me as a "topic sentence" so maybe this is the 2nd sentence in the paragraph…
**sean.polyn**: Why you did it: The best-fitting likelihood values are equivalent, but that doesn't necessarily mean the models perform equivalently on these important summary stats. In fact, if all we had were the likelihoods, it could be that all the models are equivalently terrible, like maybe none of them do well…
**sean.polyn**: So the summary stat analysis tells us that the models are each doing a good job accounting for the performance of the participants.

**You**: 
> Figure \ref{fig:MurdOkaSummary}
Maybe should report MSEs or something here?

**sean.polyn**: Maybe there's another paragraph talking about the aspects of the data that both models don't get quite right… Here's what I see.  Both models undershoot the recency effect in the SPC, both models predict a monotonic recency effect in the PFR but really it has a non-monotonic 'kink' in it, and both models underpredict the sharpness of the lag-CRP
**sean.polyn**: From one perspective, the fact that both models screw up in exactly the same way may actually be a good thing for our story… in that the main point we want to make is that the two models are very similar in their dynamics, and that you don't lose anything in shifting from a neural net framework to an instance framework.

**sean.polyn**: We might want to add in a follow up analysis or two in a subsequent draft of the paper, but for now, the goal is just to describe the analyses that are already inserted. So the only thing left to do is make sure the section wraps up with at least some kind of take-away point

**You**: Could use a table with the best fitting parameters

## Resolutions
Oh, most of these comments are from may and I've already addressed them! It's the stuff at top about adding a workthrough of how the models realize organizational details and how parameters control them that he wants elaboration for. Okay! So one core action item here. Well two - the figure(s) and the writeups(s). Likely to be broken down a bit, too.