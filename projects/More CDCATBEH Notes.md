Observations from fits:

Semantic CMR surprisingly seems to fit to heavy distraction condition somewhat better than the light distraction condition.

Encoding drift rate is .07 higher in light condition
recall drift rate is .19 higher in light condition
...I need to make sure I understand the effect of this. Faster drift rate means new information replaces old information faster. Forward transition rates are achieved through persistence of information in context for successive study events. Minus transition rates similarly require persistence. So what's this? Hm.

item support is .03 lower in light condition
...probably not a big deal?

learning rate is about .1 higher in light condition
...i need to remind myself what htis parameter does to behavior

Start drift rate is .09 higher in light condition
primacy scale is about 2 higher in light condition
primacy decay is about 8 lower in light condition
...implies that people start recall with the first item more often in the light condition. previous work apparently suggests people might habituate to distraction over time. another possibility is that start of list contextual reinstatement is disrupted in the heavy condition. taking this mechanism seriously requires a better understanding of why and when people reinstate start of list context before beginning retrieval.

stop probability scale is about .004 lower in light condition
stop probability growth is about .05 lower in light condition
...implies that people terminate recall a bit later in light condition. effect is not as strong as one might thing, but maybe i'm misreading the values. 

shared_support is .09 higher in light condition
choice sensitivity is about .15 higher in light condition
...A mixed story here. Higher choice sensitivity implies that the most supported (contiguous) transitions occurs more often in the light condition. Could be a sign that the cue or contacted memories are "stronger". But higher shared_support should counter choice sensitivity's effect, so idk.

delay drift rate is about .003 higher in light condition

semantic scale is about .5 higher in light condition
...Temporal organization isn't the only thing impacted. 

What can I conclude from this?
- I need to clarify the effect of these different parameters on model behavior, especially drift rate, shared support, primacy scale/decay, start drift rate, stop probability growth/scale, choice sensitivity, learning rate. 
- I need to see how distraction events that can be recalled will affect model simulation if parameters are held constant. Isn't this just a doubled encoding drift rate? Uh, yeah. 
- I need to explore a role for noise here. It's straightforward to encode noise in semantic representations as a function of primacy or condition.
- I think to have a clearer understanding of how behavior differs across conditions according to the model, I need to do a serious generalization test and observe trends in model errors. Then I can test for accommodation mechanisms. 
- But how do I "fit" the distraction-sensitive parameters anyway? There's no clear marker of distractedness that I can stake a metric to. I think I'd need a weaker test -- like overall fit to the dataset. Yeah, I'll hold parameters the same across conditions except for a condition-unique distraction parameter.

Okay, so I have to do something more like hierarchical modeling of distraction effects where I fit across conditions and have a parameter vary its setting across conditions. First I will try to clarify how parameters normally modify recall organization. Then based on what I learn, I will try examining mechanisms for event intervention, diminished attention/learning, and noisy encoding. Still missing qualitative constraints that would make the paper stronger. Also, what's the deal with the primacy issue? I'll be hoping that event intervention accounts for the difference.

Are there other behavioral phenomena I can hope to account for besides the primacy gap? I'll need to dig into Becky's literature review to know for sure.

To do list...
0) Get fits for Base CMR and Semantic CMR across conditions
1) Reinstate parameter manipulation experiments to help understand model predictions.
2) Specify conditionwise objective function that uses a different value for the model depending on the values of a condition vector. 
3) Specify, implement, and test intervening events mechanism where primacy weighting and context continue to evolve through distraction events by a specified amount
4) Specify, implement, and test impaired encoding mechanism where continual distraction intensity modulates the noisiness of encoded feature representations

The model doesn't have as much problem getting PFR right between conditions but the same parameters can't predict distinct PFR curves or distinct CRPs. The biggest failure exhibited across conditions is actually the prediction of recall rates of terminal items. Maybe an overcorrection from accounting for recall rates of initial items. Eh.



***

Interestingly, the "intervening event" account of distraction effects on memory search doesn't seem to offer a clean account of how semantic organization might be suppressed under our best CMR variant so far.  It's easy to see how putting an event in between two study items might weaken one's ability to store strong temporal associations according to retrieved context theory (RCT), but our best CMR variant so far assumes semantic organization operates mostly independently of the contextual dynamics specified by RCT. So the differences we find in semantic organization between conditions seem to me to imply that we'll have to decide in favor of at least one of these two ideas:

1. The degree of semantic organization in free recall does depend in part on co-activation of study items in working memory that adding intervening events can keep from happening (i think we kinda know this is true based on neural evidence)
2. Distraction can degrade semantic contiguity by mechanisms separate from the whole "intervening event" thing. (For example, it might reduce the quality of encoded item representations).