It looks like giving items a unique index per item_string is backfiring. I need indices to start from 0 per trial for my codebase to work. That is probably a new issue. 

[[projects/issues/fitting - make it possible w diverse item representations.md]]

Also, generate_trial_mask fails when the trial-level factor is a string instead of a number.

[[projects/archive/Make generate trial mask work properly for queries over string columns]]

So now I can confirm that summary statistics fit right. Now how about the model? Why does the likelihood function keep returning odd values anyway?