---
marp: false
headingDivider: 3
---

> The report to Sean for this week

# Workflow Improvements
I'll keep documenting improvements to tools I like.

## Paper Summaries With Argdown?
Argdown is a Markdown-like syntax for efficient argument specification.

It makes associating ideas with their pros and cons as easy as building a bulleted list. 

For deeper analysis, also supports more complex relations like logical premise-conclusion structures.

It's mostly designed for philosophical work and critical thinking courses, but I've been thinking of using it to represent my paper notes.

![bg right:40% contain](2021-01-28-06-09-49.png)

### Argdown Treats Arguments as Queriable Graphs
Besides helping you structure arguments, the syntax also supports quick visualization of encoded arguments as a viewable graph of argument/claim relations. Those can be exported as images, rendered as interactive web components, or embedded in documents.

These graphs can be pooled across documents, or flexibly subsetted to focus on particular ideas. 

So in theory, I can treat a collection of paper summaries specified in Argdown as a queriable evidence network built organically as I write them.

![bg right:40% contain](2021-01-28-06-13-08.png)

### Downsides in Practice
**It takes extra work.** Default mode is to just use search. A good search engine can identify related papers using PDF texts and citation networks. They won't tell me the exact ideas and evidential relations between them across these papers, but do we get a huge extra bang for buck by tracking them?

**It requires attention to wording across entire collection.** If a paper words a claim a little differently from another paper, I have to track this in some way, or the papers will be disconnected in any supergraph. A consistent naming scheme might help and be enforceable in small-scale projects, but scaleability seems impossible.

**Complex argument graphs aren't necessarily all that helpful!** Could add cognitive load instead depending on use case.

I don't really have anything to _lose_ by specifying my paper notes in Argdown; it's not really any extra work, and keeps options open. But I probably should let go of any ambition for Argdown to support building queriable large-scale evidence graphs.

# Instance CMR
| Week | Milestone |Description |
| ---- | --------- | ---------- 
| **1** | **Match** | **Demonstrate (or not) equivalence to CMR across datasets.**
| 2 | Distinguish (Theory) | Clarify latent theoretical distinctions between models, linking these with testable predictions and the literature. |
| 3 | Distinguish (Data) | Prove proposed distinctions are real (or not!) by relating models to relevant existing data sets.
| 4 | Update | Update model specification based on results, and re-analyze.
| 5+ | Relate | Connect ICMR to other instance-based models, e.g. ITS. | 
| Beyond | Convey | Develop paper, presentations, supplementary analyses. |

<!--
We're on Week 1 of my pretty tough timeline for progress on ICMR. In some sense, this one should be easier, since I started some of its specification last week (i.e. an implmentation for CMR) and classes at the moment are starting slowly. But even with those affordances, what I hoped to pull off this week could be too much, especially with my parallel effort to finish up PCITpy and make time for my narrative memory project(s). 
-->
_
## A rough strategy for tackling the week's goals
**Reproduce CMR, documenting parallels.** Our notebook outlining the implementation will extend our discussion from last week.

<!--
I started this last week, and was hobbled by a poor grasp of the operations performed over each matrix/graph. Now that I understand them, it's easier to relate ICMR to those operations as well. 

I'll try to respecify ICMR such that it encodes and explicitly tracks as few a set of departures from classic CMR as possible - only those necessary to realize our goal of an instance-based implementation of CMR.

We'll clarify precisely what constraints are entailed when we say Instance CMR.
-->

**Compare models' fit to behavioral data (`MurdData_clean.mat`).** We'll track parameters, costs. Big differences require reflection. If they aren't an order of magnitude different, that's evidence the models are similar. Discussion can review core phenomena the models must account for, and explain why results aren't just identical.

**Show where ICMR's $M$ and CMR's $M^{FC|CF}$ correspond in principle.** We can make a function that calculates for any state of ICMR's $M$ a corresponding $M^{FC|CF}$ by computing for each orthogonal $f_i$ (or $c_i$) the model's corresponding echo representation. Pairing an explanation of the function with simulations showing corresponding representations across encoding and retrieval should be convincing.

<!--
## Development-Focused Way to Put It
**Make sure our CMR works**. And that model analysis functions can be readily applied to it, including fitting.

**Review ICMR and CMR side-by-side**. Find the shortest comprehensive explanation of where ICMR departs from CMR, and confirm that these are the minimum necessary changes to achieve an instance-based CMR implementation.

**Develop tests for parameter correspondence**. (1) Make sure modifying parameters have similar consequences across models. (2) See how much parameter fits differ across models. (3) Test for differences in content and use of model constructs like `memory` and `context`.
-->

<!--
## Even More Fine-Grained
I need to extend the CMR notebook to either draw credible CRP/RSP/PFR curves from hand-fit parameters or find those parameters via all-parameter fitting.

Then I need to rework both models simultaneously to be even _more_ similar, using what I've learned again about encoding/retrieval mechanisms. I need to explicitly document these parallels somewhere. That probably means a separate model comparison notebook. I may also need to bring MINERVA 2 back into the conversation too, for discussing exactly what it takes to make something an instance-based model.

At the same time, or perhaps beforehand, or perhaps afterwards, I need to make sure these changes _scan_. I need tests to help me converge to a CMR/ICMR duo that genuinely work as similarly as they can under relevant constraints. That will be a lot of code by itself.

I'll probably end up neglecting thorough documentation here; however, I do need enough to draw the connections that make this work worthwhile.
-->

## What's the next reasonable step?
I want a flexible development workflow, so I'll make a separate notebook and directly include specs for CMR/ICMR as code cells, removing docstrings. I'll start in jupyter and literally just have headers and empty code cells.

Next I'll specify relevant tests. What do I want? For each model, show what happens when hand_fit_parameters are the model's parameters: encoding states, retrieval states, organizational analyses. For each model, show what happens when you do a fit to a subject of murd_data - parameters, costs, runtime.

Then I'll make three separate views of the notebook (CMR, ICMR, analyses) and get to work.

Once satisfied with the code, I'll clean up documentation, and refactor back to relevant notebooks.

If I finish this today, then tomorrow I can think about narrative stuff! Weekend will be PCIT again.

I have encoding stages and memory states, with the M-Mfc/Mcf translation I was talking about.  
I'm working on retrieval states.   
I still need actual comparative SPC/PFRC/CRPC visualizations.   
I still need comparative fits.  
I still need comparative design and documentation.  
I still need to test that parameters configure the models similarly.  

I'm now very confident that the models operate more or less identically. But let's see if we can do even better.

Some ideas:
**Change how I handle weighting**. Can these be a property of the memory store, too, or should I leave them a feature of the activation function?
**Reserve choice sensitivity parameter for item recall rather than also Mfc/Mcf activations.**
**Compute activation with just a dot product rather than cosine similarity.** Key difference though is that we have modulate activations to manage the consequences of parameters like primacy, learning_rate. 
**Weight by primacy/learning_rate during encoding instead of activation.** If cosine similarity isn't the core activation function, then I don't have to worry about "distortion".

**

What's actually different between CMR and ICMR?

**Initialization**. All but identical. Even ICMR's memory matrix is roughly just CMR's Mfc and Mcf concatenated with one another.

**Experience**. Same sequence of updating context based on encoding drift rate and the content of experience and then updating memory. But the way memory changes is different. In CMR, updating occurs by adding a modulated quantity (outer product of updated context and current experience) to Mfc/Mcf. ICMR basically preserves information about current experience and context so it can perform these operations later: during retrieval. [The modulation of learning by the current configuration of `learning_rate` and `primacy_weighting` happens during encoding. Even the control exerted by `learning_rate` and `primacy_weighting` occurs during retrieval, in the model's activation function, but that might not be necessary.]

**Updating context**. Both models start contextual updating by calculating a contextual input by activating existing F-C associations based on current experience (F). This contextual input is integrated into context according to the exact same formulas across model.

**Activating memory representations**. Whether when extracting F->C associations or C->F associations, both models compute activations by first performing a dot product between the relevant memory store and some cue - either current C or F. But ICMR's activation performs some operations on the fly that CMR otherwise does during learning. [First, it performs a a weighting of the contribution of individual learning episodes based on whether they're prexperimental or experimental, and on whether they occurred early/late in the list. I do wonder if I can just do that during encoding, though, especially if I ditch cosine similarity as my activation function.] Second, there's basically an extra layer of associations. Not just F->C or C->F, but F->T->C and C->T->F. Computationally, it's a second dot product.

**Recall**. Exact same, just using the mechanisms and structures outlined above.


```
[7.8400056e+00 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05
 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05
 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05
 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05 6.4016001e-05]
[2.84934738e+00 4.72054030e+00 1.63865601e-04 1.63865601e-04
 1.63865601e-04 1.63865601e-04 1.63865601e-04 1.63865601e-04
 1.63865601e-04 1.63865601e-04 1.63865601e-04 1.63865601e-04
 1.63865601e-04 1.63865601e-04 1.63865601e-04 1.63865601e-04
 1.63865601e-04 1.63865601e-04 1.63865601e-04 1.63865601e-04]
[1.04203468e+00 1.72031729e+00 3.77531228e+00 2.45893761e-04
 2.45893761e-04 2.45893761e-04 2.45893761e-04 2.45893761e-04
 2.45893761e-04 2.45893761e-04 2.45893761e-04 2.45893761e-04
 2.45893761e-04 2.45893761e-04 2.45893761e-04 2.45893761e-04
 2.45893761e-04 2.45893761e-04 2.45893761e-04 2.45893761e-04]
[3.84996671e-01 6.31970303e-01 1.37783032e+00 3.45661002e+00
 3.03073281e-04 3.03073281e-04 3.03073281e-04 3.03073281e-04
 3.03073281e-04 3.03073281e-04 3.03073281e-04 3.03073281e-04
 3.03073281e-04 3.03073281e-04 3.03073281e-04 3.03073281e-04
 3.03073281e-04 3.03073281e-04 3.03073281e-04 3.03073281e-04]
[1.44619724e-01 2.35205367e-01 5.07352061e-01 1.26229279e+00
 3.34436840e+00 3.40247538e-04 3.40247538e-04 3.40247538e-04
 3.40247538e-04 3.40247538e-04 3.40247538e-04 3.40247538e-04
 3.40247538e-04 3.40247538e-04 3.40247538e-04 3.40247538e-04
 3.40247538e-04 3.40247538e-04 3.40247538e-04 3.40247538e-04]
[5.57780638e-02 8.93939770e-02 1.89549041e-01 4.65275723e-01
 1.22159362e+00 3.30441802e+00 3.63584048e-04 3.63584048e-04
 3.63584048e-04 3.63584048e-04 3.63584048e-04 3.63584048e-04
 3.63584048e-04 3.63584048e-04 3.63584048e-04 3.63584048e-04
 3.63584048e-04 3.63584048e-04 3.63584048e-04 3.63584048e-04]
[2.24114912e-02 3.51162689e-02 7.24814441e-02 1.74111862e-01
 4.50448709e-01 1.20710630e+00 3.29030533e+00 3.77957458e-04
 3.77957458e-04 3.77957458e-04 3.77957458e-04 3.77957458e-04
 3.77957458e-04 3.77957458e-04 3.77957458e-04 3.77957458e-04
 3.77957458e-04 3.77957458e-04 3.77957458e-04 3.77957458e-04]
[9.56938002e-03 1.45049293e-02 2.87420038e-02 6.67502414e-02
 1.68668950e-01 4.45170169e-01 1.20198843e+00 3.28543523e+00
 3.86715246e-04 3.86715246e-04 3.86715246e-04 3.86715246e-04
 3.86715246e-04 3.86715246e-04 3.86715246e-04 3.86715246e-04
 3.86715246e-04 3.86715246e-04 3.86715246e-04 3.86715246e-04]
[4.44813296e-03 6.44202833e-03 1.20387420e-02 2.65744799e-02
 6.47276806e-02 1.66730810e-01 4.43305349e-01 1.20022230e+00
 3.28383293e+00 3.92018065e-04 3.92018065e-04 3.92018065e-04
 3.92018065e-04 3.92018065e-04 3.92018065e-04 3.92018065e-04
 3.92018065e-04 3.92018065e-04 3.92018065e-04 3.92018065e-04]
[2.30563180e-03 3.15369270e-03 5.45132970e-03 1.11958588e-02
 2.58084905e-02 6.40072318e-02 1.66046045e-01 4.42661807e-01
 1.19964123e+00 3.28335660e+00 3.95217090e-04 3.95217090e-04
 3.95217090e-04 3.95217090e-04 3.95217090e-04 3.95217090e-04
 3.95217090e-04 3.95217090e-04 3.95217090e-04 3.95217090e-04]
[1.35502005e-03 1.73847711e-03 2.73531849e-03 5.11034700e-03
 1.08973821e-02 2.55354978e-02 6.37526579e-02 1.65809728e-01
 4.42450074e-01 1.19946849e+00 3.28324920e+00 3.97142744e-04
 3.97142744e-04 3.97142744e-04 3.97142744e-04 3.97142744e-04
 3.97142744e-04 3.97142744e-04 3.97142744e-04 3.97142744e-04]
[9.05213016e-04 1.09015064e-03 1.55082878e-03 2.59003787e-03
 4.98926314e-03 1.07909260e-02 2.54390162e-02 6.36647992e-02
 1.65731977e-01 4.42387131e-01 1.19942954e+00 3.28325038e+00
 3.98300383e-04 3.98300383e-04 3.98300383e-04 3.98300383e-04
 3.98300383e-04 3.98300383e-04 3.98300383e-04 3.98300383e-04]
[6.78730406e-04 7.73443803e-04 1.00037707e-03 1.48501164e-03
 2.53826831e-03 4.94603169e-03 1.07532916e-02 2.54057161e-02
 6.36358919e-02 1.65708863e-01 4.42372938e-01 1.19942996e+00
 3.28327523e+00 3.98995776e-04 3.98995776e-04 3.98995776e-04
 3.98995776e-04 3.98995776e-04 3.98995776e-04 3.98995776e-04]
[5.58465418e-04 6.09443752e-04 7.27793213e-04 9.68573237e-04
 1.46146698e-03 2.51976065e-03 4.93074273e-03 1.07403011e-02
 2.53947595e-02 6.36272984e-02 1.65703651e-01 4.42373094e-01
 1.19943898e+00 3.28329902e+00 3.99413302e-04 3.99413302e-04
 3.99413302e-04 3.99413302e-04 3.99413302e-04 3.99413302e-04]
[4.91931274e-04 5.20412380e-04 5.85010277e-04 7.11478033e-04
 9.57152586e-04 1.45303762e-03 2.51321226e-03 4.92546461e-03
 1.07360267e-02 2.53915023e-02 6.36253607e-02 1.65703708e-01
 4.42376378e-01 1.19944760e+00 3.28331656e+00 3.99663923e-04
 3.99663923e-04 3.99663923e-04 3.99663923e-04 3.99663923e-04]
[4.54035733e-04 4.70366275e-04 5.06816772e-04 5.76217333e-04
 7.05599855e-04 9.53058052e-04 1.45005358e-03 2.51095123e-03
 4.92372783e-03 1.07347560e-02 2.53907679e-02 6.36253820e-02
 1.65704914e-01 4.42379522e-01 1.19945396e+00 3.28332829e+00
 3.99814333e-04 3.99814333e-04 3.99814333e-04 3.99814333e-04]
[4.32027389e-04 4.41552790e-04 4.62592122e-04 5.01899625e-04
 5.73041143e-04 7.03489845e-04 9.51607832e-04 1.44902306e-03
 2.51020718e-03 4.92321150e-03 1.07344695e-02 2.53907759e-02
 6.36258303e-02 1.65706069e-01 4.42381840e-01 1.19945822e+00
 3.28333576e+00 3.99904592e-04 3.99904592e-04 3.99904592e-04]
[4.19084815e-04 4.24701803e-04 4.37026254e-04 4.59770936e-04
 5.00120169e-04 5.71899952e-04 7.02742185e-04 9.51106916e-04
 1.44868393e-03 2.50998599e-03 4.92309508e-03 1.07344726e-02
 2.53909458e-02 6.36262595e-02 1.65706920e-01 4.42383389e-01
 1.19946093e+00 3.28334041e+00 3.99958753e-04 3.99958753e-04]
[4.11413747e-04 4.14748569e-04 4.22035546e-04 4.35380020e-04
 4.58748715e-04 4.99480388e-04 5.71495446e-04 7.02483898e-04
 9.50942058e-04 1.44858310e-03 2.50993611e-03 4.92309636e-03
 1.07345389e-02 2.53911085e-02 6.36265760e-02 1.65707489e-01
 4.42384377e-01 1.19946262e+00 3.28334326e+00 3.99991251e-04]
[4.06845117e-04 4.08833277e-04 4.13166694e-04 4.21064537e-04
 4.34783050e-04 4.58381023e-04 4.99253557e-04 5.71355689e-04
 7.02398888e-04 9.50893045e-04 1.44856037e-03 2.50993666e-03
 4.92312329e-03 1.07346024e-02 2.53912285e-02 6.36267875e-02
 1.65707852e-01 4.42384992e-01 1.19946365e+00 3.28334499e+00]
InstanceCMR
```