# InstanceCMR

## Abstract
![[instance_cmr/index]]

This section's main limitation is that it's missing a results statement. I'm also struggling to meet the promises in that last sentence, so it could need to be changed. How do I note this for Sean?

Specifies main requirements for the paper:
1. Explanation of retrieved context theory
2. Review of retrieved context theory's main feats.
3. Explanation of prototype models and linear associators
4. Explanation of instance models
5. Review of contrasts and correspondences between instance and prototype models
6. Relation of these issues to issues in memory search literature
7. Presentation of instance and prototype specifications of CMR, both the math and the "intuition"
8. Simulation of benchmark phenomena and model comparison
9. Simulation and examination of conditions where model predictions might differ
10. Demo extension of model to account for broader pool of phenomena

## Introduction
![[00_Introduction]]

I feel like I need to break this section down, probably into the components listed above. One note for each substantive idea is the game here.

What do I already have here?

Paper starts by starting with problem of pooling information distributed across encoded experiences to retrieve information relevant to a probe. Then gets right into the prototype/instance model debate. A really short version of 3/4. Then a small attempt at 5.

Then 2. Review of benchmark phenomena anyway. Then actual RCT. Then an attempt at 6.

So all the intro components are here, they just aren't very well developed. Should I try to refactor into separate notes? Sure. Which? 

- [[instance_cmr/Abstraction]] or whatever I think the question is that each architecture is answering, 
- [[instance_cmr/Instance Models]], 
- [[instance_cmr/Prototype models]], 
- Each relevant critique of each architecture, 
- [[instance_cmr/Linear Associators]], 
- [[instance_cmr/Retrieved Context Theory]], 
- [[instance_cmr/Benchmark Phenomena in Free Recall]], 
- [[instance_cmr/Architectural Contrasts in Free Recall]], 
- [[instance_cmr/Prototype vs Instance CMR]] 

If I can do that, then update my model spec and result sections, I'll more or less have a complete draft for Sean. Though the discussion might also need an update. And Sean will still want an additional section.

Thirteen things. Assume 2 hours of work for each. 26 hours. 8 today, 8 tomorrow, 8 monday. C'mon.

## Abstraction
![[Abstraction]] 
**Is abstraction really the word for this?** Wikipedia defines abstraction as a conceptual process where general rules and concepts are derived from usage and classification of specific examples. So yeah, that's it. Article also emphasizes that abstraction is a filtering process.

> For example, abstracting a leather soccer ball to the more general idea of a ball selects only the information on general ball attributes and behavior, excluding but not eliminating the other phenomenal and cognitive characteristics of that particular ball.

**Is abstraction the question that instance and prototype architectures answer?** I think so. It's thus kind of paradoxical that I'm making a big deal about the differences between these architectures when I care more about retrieving the specifics of an experience (episodic memory). That will require a clear explanation.

**What is a cognitive architecture anyway?** It looks like cognitive architecture has lots of definitions. When did I decide that this was the right term for the difference between these two? It's probably safer to use "model types" instead.

**How does something like abstraction come into play when we consider an issue like episodic memory, where it's just one episode being targetted?** The recall competition specified by CMR is not abstraction itself; it's not selecting information across past experience to retrieve a general representation. But an abstract representation is thought to drive the retrieval process -- though apparently only sometimes. Current context is passed as a probe into memory, item information over past experience is selected based on its relevance to the probe, and then the information retrieved is used to decide which item is retrieved. Similarly, each time an item is recalled, contextual information over past experience is selected based on its relevance to the item, and then the information retrieved is used to form contextual input. 

**What is a good label for these abstract representations produced during retrieval?** Abstraction is "extracting a general pattern over specific examples". In ITS, that's a contextual vector, a summary of the contexts over which a word occurred. CMR similarly retrieves summary representations of co-occurrence statistics between items and contextual states, and vice versa. And just as in ITS where these abstractive representations contain information about semantic similarity, abstractive representations retrieved according to CMR contain information about the support in memory for recall of an item. In the categorization literature, retrieved abstractive representations similarly encode response tendencies. 

**What does all this imply about what I should add or remove?** Most of this is useful primarily for drawing connections between episodic memory and models of abstraction processes. Retrieved context theory supposes that we perform abstraction over our memories using contextual cues to generate responses during free recall, and using item cues to adaptively update contextual cues. 

## Architecture Introductions
**What do I think is missing in the previous draft?**
- A fuller review of the range of architectures that are instance- or prototype-based,  
- a more concrete account of what unifies models under one framework or the other
- Concrete account of differences in types of predictions 
- Review of subtleties/overlap between architectures to help build intuition about similar performance

But what's the novel angle I want to go for? Original seems to introduce and draw contrasts between instance and prototype accounts of abstraction. I definitely want to bring up the models. But shouldn't retrieved context theory come up *soon*? Maybe I should elaborate about instance and prototype models later in the paper? How would I do that?

Start by introducing the concepts clearly enough that I can state my thesis w/o any of the necessary words being ambiguous. What's the thesis again? RCT works about as well as an account of free recall whether we use an instance or a prototype architecture to implement it. So we need...free recall, instance, prototype. And a motivation for the contrast -- so, roughly, what I already have. 

So I mainly just need to add additional section(s). And maybe refactor some ideas from this one -- probably the introduction of benchmark recall phenomena. Instead, I should start at a higher level account of the faculty being modeled. My slides from before might be a good approach.

But my review of the motivation is kind of inept, right? What does the introduction need?

I want the gist to be...abstraction is an important component of most models of memory. People classify approaches to this issue in these two ways (instance and prototype). This has been consequential for modeling in these domains (categorization, semantic). But on the other hand, But there's this other domain (free recall) where these comparisons haven't happened. I don't really need a reason besides that it hasn't happened, I guess. 

Why is this domain important? It's important model unification, for understanding these architectures, for examining the relationship between abstraction and episodic memory. But what will I say? 

I'll move everything besides this core to a secondary introduction. In the secondary introduction, 
- A fuller review of the range of architectures that are instance- or prototype-based,  
- a more concrete account of what unifies models under one framework or the other
- general specifications of the more specific instance and prototype frameworks i'm interested in
- Concrete account of differences in types of predictions 
- Review of subtleties/overlap between architectures to help build intuition about similar performance

To summarize current course...
I'll update the core introduction by refactoring really specific details into a main introduction using the principles 1) only enough for thesis statement to make sense and be interesting to a general audience, and 2) preview content in secondary introduction.

Secondary introduction intends to more deeply cover the two model frameworks first, similar to structure of ITS paper. Tertiary structure focuses on retrieved context theory, introducing benchmark phenomena and articulating how PCMR and ICMR account for them in same way except for distinct accounts of association, abstraction, retrieval.