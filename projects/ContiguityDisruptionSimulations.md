# Jordan Simulation Notes
> I think we can put some details regarding each simulation in the Appendix, after the model description. There can be a subheading like "Details of specific simulations" in there, I'll return to this below when I get to the Appendix section to-do.

## Semantic Scale Shifting
> JG: Figure 2A simulation, lag CRP. Simulation of a list with widely spaced categorized items. Doesn't have to match Expt 1 exactly, nor does it have to match Fig 2A schematic exactly. Lists have at least 6 categories. Probably should do some scrambling of category order, otherwise same-cat transitions will always be the same lag which will cause a spike in the lag-CRP at that lag. Maybe 3 lines: Category strength 0, cat strength medium, cat strength high, showing contiguity effect getting progressively weaker.

What do I currently have?
15 categories, list length of 90. So each category has 6 items. I should see if I can match the experiment more closely. This seems close enough though the presentation structure might be different.

I also vary between `[0, .4, .8, 1.2, 1.6, 2]`. Sean suggested 3 lines, with labels "0, medium, high". I might try to do this - `[0, 1, 2]`. Add labels? In practice, I suspect we'd exclude a legend from the actual figure file. I'm not sure, though.

Anyway, I consider this done. I might try to exclude or refigure the legend, though. And there will have to be an update to the writeup.


## List Length Shifting
> JG: Figure 2B simulation, lag CRP. I think you already did this one. Simulation of multiple list lengths, showing lag-CRP getting progressively weaker as list length increases. 

This is essentially already done, too. So why am I uneasy? I feel like I'm generating the same figure but with a unique legend. Implies the write-up/contextualization is more pivotal.


## Variable Restudy Order
> JG: Figure 2C simulation, lag CRP. One line: Items presented once. Second line: Items presented once, then again in a permuted order, but lag CRP is relative to the first presentation order. Should show weakening of contiguity effect in the second case.

If the trials array passed to fast_crp is always the first presentation position of the studied items, I might not need new code.  I've added an optional argument to `plot_lag_crp` to make it ignore item repetitions when I want this kind of output.

This is done. Aside from the styling issues. Interesting result is that lag-CRP is primarily only disrupted from the positive transitions side. Why? When item gets recalled, MFC retrieves a blend of its first presentation and second presentation contextual states. Then this blend is effectively passed as a retrieval cue to MCF. 

## Contiguity as Function of Serial Position
> JG: Clair ran a lag-CRP analysis conditional on remembering an item from the first half or second half of the 40 item list and found TCE was weaker for 2nd half of list. Can you re-do this analysis to confirm it is true?

I don't have Claire's data handy. But when I try this on the HealyKahana2014 (task == -1) and LohnasKahana2014 (condition == 1) datasets, I find no such effect. Kind of a a relief.

But I might have Claire's data handy. Let's see...It's MAT files, so I dunno. I'm going to just report what I have for these other datasets for now. I suspect results might depend on shape of PFR curve. Strong recency (like in heavy distraction of CDCATBEH) might correspond with stronger second half contiguity. Her dataset seems to use delayed FR, which will exhibit strong primacy. But no, the Lohnas dataset has strong primacy and also exhibits the same pattern. So I dunno.


## Experiment 6
- JG: Exp 6 reports mean and standard error of the mean for recall performance, other expts report standard deviation. We have to either change this one to SD or the others to SEM
- JG: Exp 6 SPC and CRP should be in the same style as the other experiments
- JG: Need to run a regression analysis on the three lag-CRP curves like in prev experiments
- JG: Include a simulation of mixed-category and same-category conditions. 

I don't understand why he's asked me to do these thiungs. Maybe a sign in the slack discussion?

## Matching Figure Style
Grid lines are limited to the border of the figure. Varies line style instead of color. Legend placed at top right of figure, with separate border.

***

try parameter shifting but with classic activation scaling rule

remove values from plot outside of range of interest

polombo et al paper has a regression over lag crps to quantify cotniguity effect

move legend inside