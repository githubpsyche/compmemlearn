# [[Subtle Contrasts]]
We are seeking a version of ICMR that's equivalent enough to PCMR that ICMR fits about as well as PCMR to any free recall dataset that doesn't touch on some important difference between instance- and prototype-based model architectures. We are also interested in extensions to this basic ICMR that consistently improve model performance. 

We also want to keep track of the main subtle implementation differences relevant to ICMR and CMR that we evaluated so we can discuss these manipulations in our paper. Except for the contrasts involving major architectural changes, rather than implementing these variants as separate models, we'll just use a single implementation that contains switches between pertinent modes of model behavior. For each contrast, we want to generate model comparison results across our datasets and write up a few paragraphs summarizing the contrast and our results.

## [[Learning Rate Modulation Before or After Activation Scaling]]
✔ Implement a switch between early and late application of learning rates during activation scaling @15m @started(22-05-24 23:28) @done(22-05-24 23:33) @lasted(5m44s)

I hypothesized that scaling trace importance based on learning rate before trace-based exponentiation was distorting the selection process. But it's more CMR-like to not do this, right? CMR does all the learning rate stuff before anything activation tuning. On the other hand, activation tuning in CMR is not trace-based in the first place. I'll have to check it out.

## [[Echo and Trace-Based Activation Scaling]]
✔ Implement switch between echo and trace-based scaling within InstanceCMR @done(22-05-24 22:41)

InstanceCMR should roughly perform just like Classic CMR when doing echo-based scaling. Any manipulation I expect to emerge as a result of trace-based scaling should only occur when using the trace-based scaling rule.

Interesting because it's a clear test of erstwhile equivalence between model variants.

## [[Activation Scaling For Retrieval of Contextual Input]]
✔ Implement a switch for F->C trace-based scaling @done(22-05-24 22:43)

It's unclear whether trace-base scaling should be applied when performing recall, or also when retrieving feature-to-context associations. Memory suggests I seem to get better model results when I don't do trace-based scaling when retrieving contextual input -- but why is that so?

Interesting because it's an option in ICMR but not in CMR. But I should confirm rough equivalence between models first.

## [[Echo- and Item-Based Contextual Reinstatement]]
✘ Implement switch between echo and item-based contextual reinstatement @cancelled(22-05-24 22:44)

CMR uses the retrieved item to cue contextual reinstatement after a recall. But why not use the same representation retrieved when performing context-based retrieval in the previous recall?

This is sort of ancillary. It's not relevant to the question of "what distinguishes instance- and prototype- models when it comes to free recall?"

## [[Single vs Dual-Stack Memory]]
✔ Implement switch between two-stack and one-stack memory @done(22-05-24 22:45)

I hypothesized that differences in pre-experimental memory associations were affecting model comparison. Switching this stuff seems to have big consequences.

## [[Exponential vs Power Activation Scaling Rule]]
✘ Redo evaluation of activation scaling rule @cancelled(22-05-24 20:14)

I considered both the exponential and the power/softmax scaling rules. I didn't find any difference in results. Right? But this was a comparison within CMR, so I'm not particularly interested in it here. The power scaling rule is more similar to the conventions established for ICMR.

## Discussion
Which contrasts are genuinely relevant for *this* project, though?
The single and dual store models are genuinely relevant. I know this because I can point out the difference in representational structure in pre-experimental memory.

The echo and trace-based scaling mechanisms are relevant because they offer an important way to demonstrate when differences in model performance are because activation is driven by trace similarity or not. Is that right? It may not be. Perhaps activation is still driven by trace similarity but we simply aren't scaling the determinism of the response rule? I'll find out.

The learning rate thing is sort of speculative. I found ICMR doing better when I made the change, but I'm not sure if it's because I made ICMR more like CMR or for some other reason. I should use whichever is best. It's mysterious exactly how the interaction between the episodic learning rate and the trace selection mechanism should play out.

The MFC scaling thing is only relevant as a potential extension. If I don't find that it consistently improves model performance, then there's no reason to explore it further except to assert that we ruled it out as a potential extra parameter.

So focuses are on dual store vs single store, echo vs trace activation scaling, and applying learning rate modulation before or after scaling trace activations. In that order.

I'll include the outcomes of any evaluations in a separate report, right?