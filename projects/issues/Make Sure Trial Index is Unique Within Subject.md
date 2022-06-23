It looks like I currently subset by experiment, which can vary within subject. Ah wait no, I don't because I set the subject afterwards.

What about the trial index? It looks like when I have more than one experiment, trial_index is not unique within subject.

`experiment*len(presentations) + trial_index` starts at 0 at experiment 1, `len(presentations)` at experiment 2 and so on. 

I'll need to test this later but ok.