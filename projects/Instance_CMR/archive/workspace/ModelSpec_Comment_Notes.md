# Model Specification Comment Notes

## CMR
**sean.polyn**: I think it would be reasonable to insert a section before this one that provides more set-up.  In the 02 section I suggested moving the activation equations to their own subsection, which could basically come before the more detailed description of the model, and do a better job setting up what we are trying to do here.

This kinda conflicts with what I thought after reviewing Intro Comments that I'd do about the math. Maybe I do need a prior section that gets into the math of instance-based models and reinforces the significance of its nonlinear activation thing? I'm still not clear how I'd do that.

**sean.polyn**: 
> Since context-to-feature associations organizes the competition of items for retrieval, the $\alpha$ parameter further causes items to support one another in retrieval in a uniform way.
Could mention why this parameter exists. Basically it was meant as a way to represent inter-item associations, like semantic associations, in a simplified way. Though I've never been fond of this mechanism!

**sean.polyn**: 
> Meaningful differences have been observed between recall performance depending on the duration and events between the encoding and retrieval phases of the free recall task. 
Maybe remove this sentence

**sean.polyn**:
> In part to help account for this variation, we assume that between the encoding and retrieval phase of a task, the content of $C$ has drifted some amoung back toward its pre-experimental state and set the state of context at the start of retrieval according to following, with $\rho$ calculated as specified above:
Could just say that this mechanism is meant to help the model account for the primacy effect

**sean.polyn**: 
>  Given that recall is not stopped, the probability $P(i$) of recalling a given item depends mainly on its activation strength according 
So here you transition into perhaps the most critical part of the methods for this model, as this deals with degree of support for individual memories, right?  So you could start a new paragraph and explicitly mention why this is important

**sean.polyn**: 
> $\tau$ here shapes the contrast between well-supported and poorly supported items: exponentiating a large activation and a small activation by a large value of $\tau$ widens the difference between those activations, making recall of the most activated item even more likely. Small values of $\tau$ can alternatively driven recall likelihoods of differentially activated items toward one another.
Like I guess the idea is that in the instance model there's going to be nonlinearities that get involved in determining the activation of individual items… and here's a nonlinear transformation in the prototype model. So if this is going to be important later, you can mention that! (and like put a forward ref to what section we return to the issue)

I agree. Should maybe go even further and have a subheading. Tricky part is the fact that CMR actually realizes nonlinear activation of traces just fine under normal conditions, right? And also all my results show the models are largely equivalent! Readers should at no point be surprised by my results section, so I should find a way to discuss this difference without suggesting we'll see results that don't happen. Kinda off.

## InstanceCMR
Reminder not to use prototypical CMR.

I kind of like ProtoCMR. The extra syllable "type" wasn't doing tons of work.

**sean.polyn**: 
> Prototypical CMR stores associations between item feature representations (represented a pattern of weights in an item layer $F$) and temporal context (represented in a contextual layer $C$) by integrating prototypical mappings between the representations via Hebbian learning over the course of encoding.
the meaning of this phrase is unclear to me. Maybe this sentence can be unpacked somewhat. Maybe could focus on the learning events. With each study event in ProtoCMR, the association between item and context is stored in associative matrices. Could say what makes this prototypical. 2 things right? Each item representation acts as a prototype, but each context unit does too.

What makes this prototypical is that the preserved representation from trial to trial is an aggregate over all experiences so far rather than a growing store of discrete instances. I can use the language Sean provides here and then clarify what makes this prototypical with an additional sentence like my last one.

**sean.polyn**: 
> Each trace representing a pairing $i$ of a presented item's features $f_i$ and the temporal context of its presentation $c_i$ is encoded as a concatenated vector:
Maybe more to the point, could say that instead of having associative matrices, an item is linked to the co-active context by concatenating the two vectors and placing them in the same memory trace.

Yeah ok.

**sean.polyn**:
> Before the study phase is simulated, memory traces are intialized in $M$ to reflect pre-experimental associations between item features and contextual states.
Could say, Proto-CMR is initialized with pre-experimental associations reflecting a person's prior experience with a given study item. Similarly, Instance-CMR contains a set of pre-experimental memory traces containing this same information.

Yes that's a lot better.

**sean.polyn**: 
> Similarly to control pre-experimental context-to-item associations, the content of each entry $j$ for the contextual component of each pre-experimental trace $c_{pre(i,j)}$ is set by:
This needs to be re-phrased.  Can be explicit that whereas in protoCMR there are 2 distinct associative matrices containing pre-experimental associations, in instanceCMR there is just one set of pre-experimental memory traces containing both item and contextual information.

Again largely gives me the exact sentence I should use.

**sean.polyn**: Here and there when a mechanism is very similar to proto-cmr implementation, you could say, "as in prototype-CMR…" maybe?
**sean.polyn**: Then you could say the part that's similar, and follow it up with the way it is different

Yeah sure. I figured I was doing that but I could do it more.

**sean.polyn**: Now is it fair to say that the probe representation is analogous to the activation states of the two neural network layers in the protocmr model?  In proto-CMR items probe the Mfc associations to retrieve context info, and contexts probe the Mcf associations to retrieve item info. Here there is a single probe representation with item features and context features concatenated to one another. But it is analogous to those representational vectors

These are also sentences I could just add to the manuscript.

**sean.polyn**: 
> During normal simulation of the model, however, the probe is always partial.
I think this becomes clearer if you are more explicit about how the two associative matrices in protoCMR are replaced by a single associative matrix in instanceCMR. I think if you organize this section more explicitly in reference to the protoCMR section it might help.  In the protoCMR model item representations are used to retrieve blends of contextual states. Here's how that operation works in the instance model.

**sean.polyn**: 
> To avoid the possibility of assigning a probability of 0 to any possible recall, we set a minimal activation for each item to $10^{-7}$.
a note that some readers may not instantly know why this is important

Honestly, this isn't even that important and I might just delete the sentence. Model fitting works just fine even if sometimes the loss function returns a np.nan.

**sean.polyn**: We might want to number these equations using the \begin{equation} markup, some of these we will want to refer to again

**sean.polyn**: So if this is the same equation from the introduction, you could move the associated text from the intro to be here or just below

**sean.polyn**: We need to modify this series of equations... they are too redundant with one another.  It looks like everything inside the big parentheses is the same across all 3 equations… in which case the first equation defines what ai is, then the second and third equations should use the term ai instead of the big internal part.  Either that or just say in the text that the support for different memory traces in the ai equation  can be modified in order to bring protoCMR and instanceCMR into closer alignment

Yeah, this has been my main annoyince with my InstanceCMR specification since I first wrote it up. I'd rather have a "cleaner" model in general. Not sure how to tackle just yet, but will return.

**sean.polyn**: 
> In the abstraction step $E$, a single representation reflecting this pattern of activations (called an echo $e$) is constructed by summing each trace, weighted by its corresponding activation.
This is a critical paragraph, I think it needs a more informative topic sentence. "The final step of the retrieval operation in InstanceCMR involves an abstraction operation, whereby the activation of the various memory traces determines how strongly they contribute to the reactivated representation" or something along those lines

Another free sentence!

**sean.polyn**: 
> \subsection{Encoding phase}
So the reason the two methods sections have different organizations is that you kind of have to describe how the memory is probed in order to describe how pre-experimental context contributes during the study period. Maybe say this more explicitly? like "The memory probe operations described above are engaged during both the study period and during memory search."

Free sentence!

**sean.polyn**: And you know, if the equations are numbered, you could simply say,  "the current state of context is updated according to Equation X from the protoCMR section" and if there's a bunch of details that are equivalent say that explicitly.  Like here I think all the integrative dynamics are the same, so all you have to do is say, here's how instanceCMR constructs cIN, and then the rest of the context dynamics are identical to protoCMR

Okay, great, that's an awesome way to reduce redundancy between the sections and highlight congruence. I worry that sometimes differences variable names could make that less workable, but I can try harder to equalize or still include the equation reference even if, yknow.

**sean.polyn**: Again, just mention that the same primacy mechanism from protoCMR is implemented here without redescribing
**sean.polyn**: Also here, if the termination dynamics are identical, just say so without re-presenting any duplicate equations

**You**: I originally explored (and created figures with) this echo-based instance model to help rule out a possible explanation of any observed differences between CMR and ICMR. However, if I never find a compelling difference between the two in the first place, maybe specifying this variant and including results about it in my figures doesn't add much value.
**sean.polyn**: Yes, I think you could move this text temporarily to an Appendix, and that would give you a bit more space to at least justify why it appears at all.  Then if it turned out to be critical, the text could always refer the  reader to the appendix to see what that variant is all about

Ok great.

## Resolutions
Most comments include the sentence he'd like it changed to or way he'd like a thing moved, so I could just implement these and click "Resolve".

In both sections, I need to clarify the relevant parts of the model specifications: how abstraction happens, how retrieval happens. He suggests clear topic sentences; I might even try a subheading.

In particular, I need to work out how I'm going to talk about the distinction between prototype and instance-based models that Jamieson et al emphasize but CMR's specification complicates by having F representations be orthogonal (C representations aren't, though!). 

Sean once suggested that I should make the model specification sections kind of separate. But here direct reference to the CMR specification can clarify how InstanceCMR is different and avoid redundancy, particularly if I include equation numbering. Should I should implement that across the manuscript.

That part of the InstanceCMR with redundant equations has been an issue since I first wrote it up and I need to resolve a way to avoid it - either by just english-languaging some of it or rewriting things. To be honest, every time I've looked at it I've wanted to redo the whole model. May discuss this part with Sean in meeting.

Five action items!