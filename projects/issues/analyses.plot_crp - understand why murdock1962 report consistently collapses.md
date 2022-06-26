When I try to generate figures for the Murdock1962 report, my kernel always crashes inside the lag_crp function around line 190 of `compmemlearn.analyses.py`.

The Lohnas Kahana condition 1 fits are better and I don't have the same problem. And yet, the list size and other issues are presumably the same. There is still some chance that this is a memory issue. List length might be the same, but there may be more subjects or more trials per subject or both.

I guess I should try redoing the fitting and simulation. Let's redo the simulation first.

I defined a separate "TestCMR" and am generating figures just for the fitted data.

trial query is targetting lidt oengths of 30 but sim df still only has list lengths of 20. This probably explains the assertion error. But what abiut the ither error?

It looks like the error was limited to one line of code that excluded the bit updating "list length" to a specific value. But this still leaves a mystery -- where did the list length tag come from, then?

`labels[column] = labels[column][list_length_mask]`

the above line in simulate_df_from_events doesn't filter out labels the way I expect it to. It should reduce the label vector to 

Also trial mask is just `subject > -1`! Should that be the case?

Trial query is not even an argument to the function. A global is being accessed unintentionally.

So that's the problem. I'm using trial_query to generate the list length mask instead of what

The bug reproduces using the novel fits/simulations. The CRP error I seee in the 20-item subset is in the data, not the model. Is this a separat issue?

Implies that for some reason, with LLs over 20, the pipeline using `plot_flex_crp` detects extremely low transitions rates *across* lags. IIrc, it instead finds extremely sharp temporal contiguity when using `plot_crp`.

I may want to move into the data prep or plotting code for this debugging instead of focusing on the report template.

Result for first subject doesn't seem as bad as in the thing...

Bug is the list_lengths variable. I don't index the correct list length, so wrong values from result of lag_crp are sampled.

This seems to make the CRPs look better and eliminate the crashing, but to be sure, I need to run the whole rotation before I can close the issue.