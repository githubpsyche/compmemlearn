Hi Sean, yeah I'd like to meet, too. I'm in town and all; have been working from home lately to ensure I catch some deliveries but can show up at the lab on pretty short notice. I have been working on two pushes for ICMR lately, one focused on the writing and another focused on the results.

## [[Single vs Dual-Stack Memory]]
On the results side, I've come up with a way to test the explanation I proposed to you about why ICMR's performance seems to fall off relative to PCMR as list length increases. I proposed that this was due to a difference between how pre-experimental MFC and MCF are related to one another across the architectures; ICMR's single store memory makes the two's representations bleed into one another in a way that seems to limit the flexibility of our alpha parameter as specified in Morton & Polyn (2016). To determine whether this is the root of our problem, I've made a dual store variant of ICMR that uses separate memories for F->C and C->F retrievals to avoid the bleed-in issue but otherwise sticks to an instance-based architecture for the both of them. I don't intend for this to be the design we propose in our paper, but if it eliminates the degradation of model performance as a function of list length, we can be sure that's the root of our issue. If the degradation persists, then we can be sure it's something else entirely -- potentially something more central to the architectural distinction we're investigating.

## [[Theory competition across different areas of memory research has focused on differences in how architectures access associations.]]
On the writing side, I've been trying to deepen my grasp of the literature contrasting instance and prototype models. Through the end of my committee presentation, my literature review has been pretty focused and dependent on the narrative from Jamieson & Jones (2018) presenting and arguing for an instance theory of semantic memory. We've known for a long time now though that the critique of prototype models in the paper is not very relevant at all to any well-known issues in the list learning / memory search literature or to particular distinctions between our ICMR and PCMR implementations, but I've still leaned pretty hard on that paper's analysis of the architectures, only sort of lightly dipping my toes into the broader debate playing out in the categorization literature. 

I've been working on clarifying whether the issues in the categorization literature are the same as those emphasized in the Jamieson (2018) paper, or substantially different. While I'm still digging into the details, I've found that they are quite different. Jamieson (2018) focuses on the ability of instance models to account for rare senses (contextual associations) of polysemous words and explains it in terms of the architecture's access to a nonlinear response rule. But the categorization literature finds advantages for instance models over prototype models that implement the same non-linear activation rule that Jamieson (2018) casts as special. And it's developed quite a few "strong, a priori, qualitative contrasts" between the predictions from the models as opposed to the more ambiguous contrasts our datasets enable. I think that if I get a deeper understanding of how they achieved this, we'll be able to either leverage them to draw contrasts in our own paper, or provide a really principled account for why ICMR and PCMR don't differ in our domain.

On the broader front, I've come up with a sort of rough flowchart for where we might go based on the outcomes of these pushes.

Seems to me that the final design of our paper depends on a few pivot points.
1. Whether ICMR comes out ahead or not after we make our results more consistent.  
2. Whether a fuller view of the literature contrasting instance and prototype models identifies scenarios relevant for the list learning paradigm.  
3. Whether any observed differences between our models actually has anything to do with the issues described in the literature or other fundamental architectural discrepancies. 

If we find that ICMR doesn't come out ahead, then it seems to me we have to put in a bit more effort justifying the work we put in to show this. 
If our results effectively demonstrate that there wasn't really a good reason to conjecture that the architectures might differ in our comparisons in the first place, 
then it seems we want evidence that this false conjecture has had enough currency that it's was worth our efforts. 

My guess is that we can tackle this problem by casting our results as 
1) identifying a deviation from a trend of advantages for instance over prototype models demonstrated elsewhere in the literature, and 
2) 2) clarifying boundary conditions for this advantage, thereby improving our understanding of how the architectures relate to one another. 

My idea is that we'd not only show that the models perform the same on our benchmark datasets, but also that the issues providing important contrasts between the architectures in other domains aren't relevant here.

Motivating the paper is easier if ICMR does come out ahead, but we're still in a tricky situation if we can't find a deeper architectural discrepancy -- whether rooted in the literature or not -- that would explain this advantage. 
I think we'd have to keep working to find/make something convincing. 
If we find an instance/prototype distinction in the categorization literature that's genuinely relevant for list-learning, then I feel like we can sort of focus on that in our introduction and right after presenting our benchmark results. 
The right dataset and/or simulation experiment would be able to demonstrate our finding, and overall the paper would be a lot neater imo. 
I had hoped that the repetition data from the Lohnas paper would fill this niche and even performed some simulations drawing a clear contrast, but the model comparison didn't play out as cleanly as I'd hoped. 
Maybe our final results will help with that.