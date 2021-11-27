When I first planned this week, I slotted one day for fixing up my library/documentation and another for extending it via exploration of novel datasets and exploration paradigms. 

In particular, I want to encode in the documentation/library a _complete_ translation of CMR into an equivalent instance-based model that returns the same cost function outputs for the same inputs.

Then I want to identify datasets and experimental paradigms where either
1) Existing retrieved-context models could benefit from instance-based representations
2) Existing instance-based models could benefit from temporal contextual representations

I expected this to take two days but if I finish it faster, I can make progress on other efforts.

To help get me started while I obviously feel repelled by the main effort, I'll turn on recursive notebook searching and reorganize what I have now by section. I'll make the sidebar match this organization and update my jupytext command sequence to track these patterns. Index will need updating too, I guess. I'd like to use the lego-mindstorms repo as inspiration!

There's this underlying question of whether I'd like to use something else to generate my docs, but I don't know how I could bear to bother with that.

Ok, go.
- Update settings.
- Move files.
- Sidebar

Oh, but what kind of organization?
I distinguish between models and model_analysis in my library. As well as homonym experiment, etc.

Lets do "model_specification", "model_analysis", and "experiments". That'll be the structure of my paper, too! Model analysis outlines basic model analysis functions - including the computing of fits. Model specification includes specifications for any model I implement, plus any tests demonstrating their basic worth.

## CMR v ICMR 2
In our current version of ICMR, feature to context associations and context to feature associations are codetermined by the same associative network.

