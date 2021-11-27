---
marp: true
headingDivider: 3
---

# Semester 2

## Workflow Improvements
I wanted to go over some improvements to my workflow I've experienced since they seem relevant to a lot of the stuff
we've been tackling lately (e.g. dev environments, open science, lab practices).

### Moving Beyond Jupyter...
Literate and interactive programming are great and how I got started, but Jupyter itself is feature-light.

Has got weak debugging and poor language support, lacking features like linting, code completion, variable exploration,
work preservation, refactoring. Also harder to customize!

IDEs support including code/markdown cells in Python scripts to give access to these features and support
notebook-driven development at the same time. 

Extensions like Markdown Everywhere and Jupytext make the experience even more compromise-free!

<!--
I had a lot to say about dev environments in our email thread this week because it's something I've been unreasonably
obsessive over for years now. (And I'm sorry again if I was a bit much!) Back at Princeton, I only really got
comfortable as a programmer once I started working in Jupyter, and stuck with it pretty uncritically up to maybe a year
ago. However, while the paradigm it supports is great, Jupyter is itself pretty flawed. I mean, I've had some really
important days these past couple years ruined because of Jupyter's flaws. 

However, I've found them actually hard to notice if Jupyter's the only context you ever work in. I went a long time not
really knowing much about genuine debugging or appreciating the vast extent of IDEs' language support because in Jupyter
these features just aren't even in the conversation. The more I've gotten experienced with IDEs like VSCode and PyCharm
and and the more I've discovered extensions and workflows that give me access to everything I like about Jupyter without
its compromises, the more I've drifted from the platform. I've lately shifted entirely to using cell-delineated Python
scripts as my notebooks, letting me develop in VSCode and enjoy its features while giving me all the most advantages of
notebook-driven development.

I might change my mind again, as it seems I have a habit of getting overconfident in this sphere, but it feels like I've
overcome a lot of the tension I've faced with workflows thanks to this revelation.
-->

![bg right:30% contain](2021-01-22-02-31-46.png)

### ...But Going All-In On Literate Programming (NBDev)
See https://vucml.github.io/instance_cmr/ for a work-in-progress example.

One source, one workflow to automatically generate:

1. **Documentation**. Readable, explorable, complete specification of project components, easily refactorable into a
   paper draft.
2. **Library package**. A library of all project functionality installable in a single `pip` command, facilitating
   sharing, reuse, and extension.
3. **Testing**. Tests can be included in notebooks and executed in parallel with a single command. They can either work
   as library demonstrations in actual docs, or be kept hidden!

All from a collection of notebooks (or cell-formatted scripts, with Jupytext).

<!--
Still, though, I'm quite committed to one feature of Jupyter, and that's literate programming: preparing and presenting
code as if writing an essay, interspersing source code with exposition thereof in clear, natural language, and in
general proceeding in the order demanded by the logic and flow of our thoughts rather than by the structure imposed by
the computer. Most frameworks for achieving that sort of workflow are pretty clunky and force you into poor programming
habits or feature-light development contexts like Jupyter. With the new library called nbdev, the approach feels like it
makes sense instead of just being a self-imposed handicap.

nbdev lets you develop a traditional python package like the ones you install with pip or conda in the context of a
notebook, putting all of your code, tests, and documentation in one place and letting you develop it in a single flow.
If you check out my instance_cmr repo, you'll see what I mean. A collection of script-based notebooks in the root
directory work as the ground truth for everything else in the repo, reflecting the most up to date state of my project.
I add  notebooks just based on the increment I'd like to make for the project - stuff like implementing or writing out a
specification of some model, developing new helper functions to visualize or analyze outputs, etc. Normally, that would
be where the conversation stops as far as notebooks are concerned and I'd have to do a lot of refactoring to achieve
anything else. But with nbdev, a single command prepares a pretty neat documentation website and an installable Python
package from these notebooks - and lets me use the notebooks as a testing framework too. When I revise a notebook, all
three of these are updated at the same time, saving me a lot of headache surrounding consistency.

This stuff might seem like window dressing compared to the main objective of science - a well-written paper - but the
workflow achieves a few outcomes that usually happen in separate increments across a project. First, if written with the
idea in mind, this documentation is easily refactorable as a publication draft; implementational details like function
APIs just have to be discarded. A link to the documentation site can be included in the publication to keep a codebase
accessible and open. Maintaining a module library achieves similar objectives and more; it also maximizes extensibility
reusability. All the functions and classes developed over the course of a project can be re-used for new work via a
single pip command, making it easier to develop new analysis or leverage past successes for new projects. And testing of
course is critical but easy to overlook in an exploratory workflow. The magic of nbdev is that it gives you that,
detailed project documentation, and a module library without disrupting the traditional exploratory pattern scientists
favor or requiring you do much extra. 

There are some big caveats, probably the biggest being the fact that this tool is only useful for Python projects, and a
lot of weird bugs I haven't worked out yet, but I'm increasingly enthusiastic about the workflow it supports at least.
-->

### Other Workflows
**Presentations**. Currently Marp -> Google Slides. Still feels janky, amateurish. May explore RevealJS and Beamer
options, or even Microsoft Office.

**Literature Review**. The Google Scholar extension makes connecting any reference to its source barely harder than if a
literal link were included. I previously encoded literature notes as slide decks with a Markdown source, including
detailed hidden comments where relevant. This helped build a coherent view and enabled quick presentation, while staying
easily integrated with other frameworks like version control and inclusion in notebooks. But arguably not super
scaleable or helpful for identifying latent patterns. Exploring other options, like markdown-based argument mapping.

**Writing**. Wrote ICMR spec and final paper for Vision course within notebooks. So pretty experienced fitting LaTeX
into markdown and understand formatting, but still haven't developed in LaTeX proper. May ultimately stick with Markdown
and convert downstream (with `pandoc`) for private efforts. ICMR seems to be my next important test. Also have been
studying writing practices more generally!

<!--
I've already told you about how I often create slides with a framework called Marp that can generate slide decks - like
this one - from Markdown documents. These slide decks are easy to produce quickly, but are kind of amateurish if only
because they aren't very customizeable. Lately I've adopted the workflow of starting presentation design in marp and
then moving to Google Slides for fine-tuning. 
-->

## Projects
Current "live" projects are 
- InstanceCMR
- Narrative Unit Extraction
- CATRBC
- Narrative Memory Model Exploration

### A Staggered Bimonthly Pattern For Maturing Projects?
With the exception of fMRI or other heavy-duty efforts, we could select and constrain projects to a 2-4 month timeline,
where they each spend 2 months as the primary focus of work and are otherwise planned out, or finalized, in the
remaining time.

A project might be suitable for focus when have we a concrete idea of what we can achieve for it with ~2 months of
focused effort. A project that turns out to need more than 4 months of focused work may need to be broken up or
reconsidered.

This helps control project scope, keep attention undivided, and enforce a steady output. 

But is flexible in the end because we can do whatever we want!

<!--
We might say we're 3 weeks into focused work this year on ICMR, with the Narrative Unit project next up for a couple
months of focus after we clarify its status. **Two submissions by Committee Meeting would be neat!**
-->

### A Rough Timeline for ICMR (A Tight Fit!)
| Week | Milestone |Description |
| ---- | --------- | ---------- 
| 1 | Match | Demonstrate (or not) equivalence to CMR across datasets.
| 2 | Distinguish (Theory) | Clarify latent theoretical distinctions between models, linking these with testable predictions and the literature. |
| 3 | Distinguish (Data) | Prove proposed distinctions are real (or not!) by relating models to relevant existing data sets.
| 4 | Update | Update model specification based on results, and re-analyze.
| 5+ | Relate | Connect ICMR to other instance-based models, e.g. ITS. | 
| Beyond | Convey | Develop paper, presentations, supplementary analyses. |

<!--
I need to present in April; this outline pressures me to finish core analyses by the end of Februrary. It is a tight
fit, but I get two months of slack for milestones that take longer (e.g. if we have to do online data collection)
-->

### Planning Milestones for Narrative Unit Project
In the background, we want to clear a project in waiting for successive focus periods. Particularly easy this time given
that I've been here a year and a half. Goal is preparation for a two month window of focus that ends in a complete
project.

| Index | Milestone | Description
| ----- | --------- | ---------- 
| 1 | Reinstate | Review and document status of project as it is now.
| 2 | Clarify | Expand diagnostic analyses to clarify project frontier.
| 3 | Review | Connect analysis outcomes to what we now know about the literature and what we want for the project.
| 4 | Concretize | Specify timeline and corresponding milestones for focus period.

### Planning the Narrative Memory Modeling Project
There's a hackathon run by Stanford (Treehacks) coming up on February 12-14.

I'm thinking of using the event to focus on developing our own implementation of the Landscape model of text
comprehension (or whichever model we're interested in at the time) and configuring it within some app or browser
extension to generate recall probabilities for roughly specified idea units in arbitrary texts using some default
parameters.

This would kick off our modeling effort, look cool for the lab, and start work an objective I've long had for cognitive
modeling research: technological applications in naturalistic contexts.

Until then, I'll focus on literature review.

<!--
We'd have a baseline model and cost function for fitting) Web app could be included 

Having a browser-based implementation would also open up experiment design possibilities. In general, I want to explore
existing tools for translating Python functions into client-side JavaScript-based functionality.
-->

### CATRBC and Browser-Based Experiments
I'm interested in reworking my flow for developing browser-based experiments in general based on Python-based paradigms
I've gotten familiar with. 

I think we can get just as comfortable developing and reporting outcomes of Javascript and HTML-based code as we are
with Python/MATLAB code. 

I can prioritize this effort based on your preference.

## What's Different and the Same (For Now) Between Instance and Classic CMR?
- We use our sensitivity parameter $\tau$ differently
- But otherwise learning mechanisms apply the same Hebbian mechanism
- Item retrieval is also mostly identical, despite trace/item activation distinction
- We make a lot of decisions to enforce model equivalence that could be flexed!
- These options mostly revolve around making the most of trace specificity and/or our unitary memory system

### We Can Conceptualize a Latent $M^{FC}$ and $M^{CF}$ in ICMR
For exploring and demonstrating model equivalence, we can calculate for any state of ICMR's dual-store memory array $M$
a corresponding $M^{FC}$ (or $M^{CF}$) by computing for each orthogonal $f_i$ (or $c_i$) the model's corresponding echo
representation. 

Because echoes taken this way are how we retrieve $F\rightarrow C$ and $C \rightarrow F$ associations in the model, the
resulting matrices characterize model behavior identically to how they would in classic CMR. This convention lets us
compare model performance internally as well as externally.

### When to Apply the Choice Sensitivity Parameter
Both CMR and exemplar models apply a choice sensitivity parameter $\tau$ to control the contrast between well-supported
and poorly supported items. High values of $\tau$ will cause a greater influence of differences in support, while low
values will cause relatively uniform probabilities of recalling each item.

In CMR, activations are only relevant during item retrieval, and $\tau$ specifically only impacts the probability
distribution of the item to be recalled next.

However, in ICMR, activations are also computed to retrieve associations between feature representations and context -
the equivalent of finding $M^{FC}f_i$ in CMR. The echo obtained when presenting $f_i$ as a cue to memory contains the
contextual information that will update context, both during encoding and after any item is recalled!

### Otherwise Learning F->C and C->F Associations Seems Identical!
If we only apply the sensitivity modulation during item retrieval, then I think (though have not yet proven) that our
two-store approach to associating features with context works _exactly_ the same as the hebbian process modulating
$M^{CF}$ and $M^{FC}$. 

We can demonstrate this theoretically or empirically by comparing the impact on $F\rightarrow C$ associations of adding
a new trace in InstanceCMR or of adding $\Delta M^{FC}$ to $M^{FC}$ in classic CMR. In both cases, it seems to just be
simple addition, merely at different timepoints.

We may be interested in keeping a universal $\tau$, or even consider fitting for separate $\tau_{echo}$ and
$\tau_{item}$ parameters depending on the type of retrieval that's happening. It's pretty likely that adding a second
parameter will improve model fits; whether that's interesting or not is another question. 

### But What About During Item Retrieval?
In classic CMR, the pattern in $M^{CF}c$ determines the activation of each item $a$. 

The same is more or less true with respect to ICMR's _latent_ $M^{CF}c$ encoded in our dual-store memory array $M$: 

Based on its activation when $C$ is treated as a cue, each memory trace supports the item representation with the
closest feature content.

But we make some decisions to enforce this equivalence! 

### Discarding Trace Context, or How We Don't Treat $M$ Like a Single Memory
Even though traces in ICMR are unique, we discard their unique contextual content when configuring $c_{in}$ to cue
successive recalls, instead using the equivalent of $M^{FC}f_i$ as performed by CMR. 

This information could instead be used as a direct cue for the next recall, with or without its accompanying feature
content. Since that may be too insular, it could also included with the retrieved item's feature content as part of the
memory cue to our equivalent of $M^{FC}f_i$. 

If we did either wrt to retrieval, successive recalls would be biased to a _particular trace context_ rather than a
balanced sum of all contexts with relevant feature information, creating some interesting consequences for even single
presentation experiments.

<!--
More generally, we decide against ever treating $M$ as a unitary memory system when it comes to free recall. Even though
we use a single array to represent $M$, we only ever cue it with either feature information or contextual information.
-->

### Some Less Interesting Flex Points
- Instead of using the echo mechanism for some kinds of retrieval and activations for others, echo content could set up
  a retrieval competition based on cosine similarity to item representations. _This would certainly be simplifying in
  some respects, but otherwise probably achieves the same retrieval dynamics with extra steps post- trace activation._
- We can decide $c_{IN}$ using $c_{i-1}$ along with $f_i$ instead of just using $f_i$. _This is probably just equivalent
  to using a smaller drift rate parameter, since it would keep $c_i$ more like $c_{i-1}$._

### Also: We're Missing an Extra Drift Event and Parameter
> To simulate the end-of-list distraction in Experiment 2, we assumed that distraction during the retention interval
> causes a change in context (Sederberg et al., 2008). Context is updated according to Eq. (12), where $\beta$ is set to
> $\beta_{RI}$ and $c^{IN}_i$, and  is a vector that is orthogonal to the pre-experimental contexts of the studied
> items.

I don't know what $\beta_{RI}$ refers to here or if I should be drifting $c$ to something orthogonal even to pre-list
$c_0$. But either way, $\beta_{delay}$ doesn't really seem to come up explicitly in the text of Morton & Polyn (2016)
except in Table 1.

I could either add it or leave it out of the implementation of CMR we're using for model comparison.

## What Next?
- Finish and confirm/realize equivalence between ICMR and CMR at least where equivalence is expected, across core data
  sets (which are?)
- Systematically explore consequences of potential modifications outlined here in terms of ICMR's fit to data sets
  already under consideration
- Identify and evaluate model versions against data sets where these candidate distinctions might be of particular
  relevance (e.g. repeated presentations)

```python

```
