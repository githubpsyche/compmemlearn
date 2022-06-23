![[Pasted image 20220619220855.png]]

> sean.polyn: This section needs to be better grounded before getting into some of the theoretical ideas. The reader needs to first be oriented, I'll try to explain what I mean below

```latex
\section{Instance and Prototype Accounts of
Abstraction}\label{instance-and-prototype-accounts-of-abstraction}}

%% SMP adding some text here to develop some ideas %%
- Our goal is to compare and contrast connectionist and instance-based approaches to models of human memory. 
  - What we mean by connectionist, this includes neural networks in the PDP tradition, but also linear associative networks (some cites)
  - What we mean by instance-based, this includes... (some cites)
- Both approaches are fundamentally representational, or attribute-based (Polyn chapter).
  - Both types of models define vector spaces as representational layers.
  - Both types of models assume that when an item is studied or presented, this is simulated by activating the item's representation on a particular layer.
- The two approaches diverge most substantially in their implementation of a learning event. 
  - In both models, a learning event involves the creation or modification of associative structures that store information about the particulars of that event. 
  - Both types of models use matrices to define these associations, but these matrices operate in different ways.
  - In connectionist models, associative matrices allow different representational layers to influence one another. These associative matrices are of a fixed size, usually containing an element for each pairwise combination of units in the two communicating layers (all-to-all connectivity). The learning event involves adjusting the strength of these associative connections.
    - Why these models are referred to as 'prototype' models. If multiple learning events involve repeated encounters with the same item, this involves adjusting a common set of associative connections.
    - For example, in the semantic memory model of Rogers et al. (Rumelhart cites too), a connectionist network is created that represents different animals and plants. The network is trained to learn multiple facts about a given organism, with separate learning events conveying different facts, e.g. "canary can sing", and "canary can fly". A single prototypical canary representation is activated for each learning event, and over the course of learning the network strengthens the associative connections linking canary to each of its features.
    - Trying to get to the point about abstraction: Here, a form of abstraction operates during learning. By the end of learning, the prototypical canary representation has a variety of associated features. 
    
  - In instance-based models, each learning event is stored separately in memory.
    - Could describe a hypothetical instance-based model learning about canaries, or could refer to something specific about Jamieson model.
    - Here, a form of abstraction operates during retrieval. 
  
- The two approaches also differ in their retrieval dynamics.

%% end of SMP scratch space
```

![[Pasted image 20220619221046.png]]

![[Pasted image 20220619221255.png]]

