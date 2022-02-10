Sean's helping me see the ICMR manuscript in a new light. I should review each comment and decide on a clear plan for revising the document, hopefully implementing it if I have the time.

# Introduction Comment Notes
My equations aren't numbered like they should be.

### First Paragraph: Defining Instance-Based (and Prototype-Based) Models
**sean.polyn**: This first paragraph contrasts instance-based models and prototype-based models, but I think it jumps too quickly to some key points. I think it will help to shuffle these sentences around a little bit. 

My first paragraph is a jumble. I get what I'm trying to convey, but my eyes just glaze over even as I'm familiar with the subject matter. I think I'm maybe missing cues of flow between sentences as I try to concisely summarize the architecture. 

**sean.polyn**: Suggestion, start with paragraph describing instance-based models of memory, and giving citations and examples of memory-dependent behaviors.  Then second paragraph should transition to prototype-based models, explain what they are, and give summarized examples of behaviors they have been applied to.

Main trouble here is that I might have a hard time picking out good representative examples. I can lean on past instance-model work for that side of things, but prototype-based models are a huge space and most discussion I've seen that characterize them that way focus a lot on DSMs. I suppose that one recent Kahana review might help, but I maybe don't want to get right into free recall, etc? Start with that paper though.

**sean.polyn**: So then paragraph 3 can contrast the two approaches, using the logic that you're developing here. But if that logic follows from 2 orienting intro paragraphs setting up what each model is all about, it will be easier for the reader to process the key points about the distinction between the two model types / approaches. 

To an extent, the paragraph does introduce instance-based models just as he suggests I focus. He probably actually wants a higher-level overview of instance-based models where I perform initial explanation by surveying examples? There is more than a little contrasting happening in the paragraph though - I almost define them in terms of how they're different from prototype-based models. I just need to figure out a way to describe instance-based models in a way that's not contrastive.

**sean.polyn**: The idea of abstraction should be developed a bit more, and this should be easier if you have separate paragraphs for each approach before you get to the direct contrast.  Maybe you could be more explicit in saying what abstraction means in this context.  It really just means that the model is blending together information from a number of traces.

Okay yes I should do this. Maybe I introduce and define the word in one sentence, and then use it to clarify what instance-based models are in another.

**sean.polyn**: This could be the opener for para 1 introducing instance theories

Referring to:
> While originally specified to help understand category learning \cite{hintzman1984minerva,hintzman1986schema,hintzman1988judgments}, this basic architecture has been applied to understand a truly vast range of memory-dependent behaviors \citep[for a short review see][]{jamieson2018instance}.
Sure - though it's not that different from my first sentence (on purpose).

### Second Paragraph
I'm reasonably happy with the next two paragraphs, though I agree that they aren't in the best location. There's not enough setup before I get into the meat.

**sean.polyn**: To be clear, this would be part of para 3 contrasting the 2 approaches

Yeah. So I can keep that sequence going a bit. But then this implies he thinks the first paragraph should be mostly dumped wholesale.

**sean.polyn**: paragraph 2 could set up what this means. Maybe giving a concrete example in para 2. I can think of 2 possible concrete examples. one would be the example of a category representation that is modified as you have more experience with items from the category. Another would be like a neural network model where there's a unit corresponding to a particular item, so any associations you link to that item are all attached to this same core representation

"This" here refers to my "to build aggregated representations" line. I think this goes back to his suggestion that I elaborate a bit more on what I mean by abstraction. He suggests I give an example; that's more than I thought I'd do. Hmm maybe I start with an example like this near the very start of my introduction? 

I think I see. He wants me to start specifically with a sentence referencing instance-based models' prominence in the category learning literature. I use that as a scaffold to talk about ways to conceptualize how category representations are modified. There's even a simple diagram I can draw about this based on my old talk slides. Okay.

**sean.polyn**: I propose you create a subsection for this mathematical treatment, and move these equations and associated text downwards in the document. So the background will set up the theories in words, and then this new subsection will specifically set up the importance of considering the equations governing the activation of memory traces.

This is a natural suggestion and something I thought about even as I wrote out the section. The reason I didn't do that is because I didn't know how to provide a concrete enough explanation of the model without a mathematical treatment. But maybe with a fuller exemplar-based discussion of abstraction it won't be so hard.

**sean.polyn**: I think Jamieson et al used cosine similarity, but MINERVA 2 used a kind of normalized Hamming similarity… but I don't know whether Hintzman used cosine sim elsewhere…

That's a side note but worth clarifying. The two metrics are the same if your representations contain only binary scalars.

**sean.polyn**: If you move this text to a section further down, you can also expand some of the description you are developing here. For example, it isn't clear from the text whether this next equation is something that happens in an instance model or a prototype model.

Re:
> A sum of stored traces weighted by these nonlinearly scaled activations is taken to build an abstractive representation for retrieval
Yeah, my context indicating that I'm describing instance-based models is pretty far down the line. He wants a longer description and that's okay. A clear subheader would maybe do a lot of the work to clarify the reference too.

### Third Paragraph
**sean.polyn**: So this next paragraph still belongs here in the background section 02, but you just won't have the actual equations here, they will be below.
**sean.polyn**: You can say something like "in section __ below we examine the equations used to implement these dynamics"

Ah but this means I should present non-mathematically the nonlinear trace-based activation mechanism without describing the math. That is a toughie, and not something an example-based explanation of abstraction might cover. Ah, maybe it's not a big deal. Diagram is just relating variables without using mathematical symbols; think of it that way. Surprised he doesn't have broader critiques of that paragraph in mind.

### Introduction of Organizational Effects
**sean.polyn**: This is the first place you're talking about organizational effects. So you could have your topic sentence(s) say: "Primacy and recency effects demonstrate that the temporal structure of the list affects the memorability of the items within it. This temporal structure can also be seen in the organization of responses throughout the response sequence." (or something to that effect)

That's great if he likes it then just use that sentence. 

**You**: I was going to add exemplary figures here to demo the effects, but it might be wiser instead to rewrite the description in a way that doesn't emphasize a particular analysis and instead explains the phenomenon in its own terms.

He didn't comment on it, and I don't really know what this means anyway. Oh it means stuff like "don't define Lag-CRPs right here!". I think that's right.

### Back to Core Message
**sean.polyn**: could be more specific that each trace would contain item and context information, basically the co-active representations. Then a new sentence for the "collapse at retrieval" point.
**sean.polyn:** "collapse over" isn't intuitive what you mean.  is the point that during retrieval all traces involving a given item (or context) can be activated and "collapsed over" or blended/reactivated

re:
> In contrast, an instance-based alternative would track this history by storing a discrete record of each experience in memory to collapse over only at the point of retrieval.
First comment is largely a simple edit. Second comment suggests he doesn't find the "collapse over" language particularly intuitive. A longer sentence or better setup might clarify it better. Or I could just stick to "abstract over" or something to make the connection clear. I guess I'm trying to convey that by the end of the process we have a weighted mean of stored instances. Hmm.

**sean.polyn**: this internal phrase makes this sentence unwieldy… consider rewording

re:
> Notably, \citet{logan2021serial} introduced the Context Retrieval and Updating (CRU) model, which extends retrieved context theories' conceptualization of context as a recency-weighted history of previously presented items to account for performance on whole report, serial recall, and copy typing tasks. 
I can definitely split this into two or three sentences, yeah.

**sean.polyn**: I think I prefer "prototype CMR" to "prototypical CMR"… gotta think about this though

Okay, no problem for me. I think I'll say prototype-based CMR in one sentence and put PrototypeCMR there in parentheses to show I'm using that for further references.

**sean.polyn**: Could end the sentence here. then new sentence describing the three datasets. One involves a manipulation of list length, one involves a manipulation of the number of times a particular item is studied. Then could have a separate sentence for the point that the repetition manipulation requires abstraction over the memories of the repeated presentations?

re:
> I fit InstanceCMR and its original prototype-based counterpart (prototypical CMR) to the sequences of individual responses made by participants in three distinct free recall task datasets, including one requiring abstraction across repeated presentations of items in distinct contexts, finding each time that both models account for behavior across each dataset with similar effectiveness. 
Okay, he wants further (and discrete) elaboration on each of the datasets considered. That's reasonable.

**sean.polyn**: unclear what outcomes are being referred to here. But I think you can return to this paragraph once the results and discussion sections are better developed… basically here you are foreshadowing all the modeling results, which can be tricky to do in a clear way prior to even having the modeling methods sections

re:
> Analyses of the two specifications for CMR suggest that these outcomes can be largely explained by the model's assumption that feature representations corresponding to studied items in free recall experiments are orthogonal --- activation of each unit on an item feature layer corresponds to one item.
I mean instead of "these outcomes" I could say "outcomes of these analyses" and perhaps be clearer about the context being reference. "these" is a bad word I should ctrl+F for.

**You**: % SMP: I would want to include some acknowledgement / citing of earlier models of free recall. Mainly Raaijmakers and Shiffrin 1980 & 1981, but also Davelaar et al 2005 Psych Review. Also Brown et al. 2008 Psy Rev (the SIMPLE model). RaaiShif and DaveEtal were using the SAM framework, which can also be described as a simplified neural net, but instead of a dynamic context representation, there's a short-term buffer. But it is true that modeling of organization of response sequences has been dominated by ret-con models.
**sean.polyn**: This comment above I was thinking could be a sentence or 2 where you  introduce the ret-con models. Could mention that there are these other approaches, and that they for the most part also use prototype machinery. Could mention somewhere that there's a model of FR that uses instance machinery, the Lehman and Malmberg model, and that we will return to that one in the discussion

It's a couple of sentences, but calls for a bit of reading to write up correctly. Okay, what have I got?

## Resolutions

> I think I see. He wants me to start specifically with a sentence referencing instance-based models' prominence in the category learning literature. I use that as a scaffold to talk about ways to conceptualize how category representations are modified. There's even a simple diagram I can draw about this based on my old talk slides. Okay.

I need to rewrite my introduction of instance-based and prototype-based models such that I give them room to be outlined and for examples of each to be described before I start contrasting or otherwise analyzing them. In particular, I need to be clear about how the architectures handle abstraction differently, and clarify that concept thoroughly.

I will do that through a worked example of sorts based on category learning, perhaps paired with a helpful diagram (a better version of my talk figure) to reinforce conceptual relationships. That's the high-level overview I was worried about! 

Math stuff should ideally be moved to a later section. I'm not sure how to dig into the flow correctly. I introduce the problem in my introduction using the diagram. But how am I engaging with nonlinear trace activation? That's like the distinction I'm presenting as a big deal between the models, right? ~~Oh, I think I get it. I might not actually need to move the section so much as do the section's work when I'm presenting the specification for InstanceCMR. Yeah. Still, that's no small work either.~~

Also still need that deeper review of FR models, especially the instance-based ones. 

And a few edits breaking up or clarifying sentences. 

5 action items, since a diagram is a whole thing.