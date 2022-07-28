By the start of last week, I'd handed Becky a lot of fitting results for Semantic CMR to each condition of the CDCAT behavioral dataset. I'd fitted the model separately to each condition, and so she in turn performed paired t-tests to measure differences in configured parameter distributions between conditions and was trying to interpret the differences she'd identified.

A few factors got in the way of that being easy:
- The effect of each parameter on model behavior is kind of obscure from just reading the model specification and becky hasn't done a lot of work w CMR
- The significance of a parameter's configured value seems to depend on other parameters' configured values, 
- Tons of statistically significant results in odd directions that made drawing a cohesive story hard
- Possibility of overinterpretation. Interpreting parameter distributions can be difficult if you assume that CMR is right and heavy vs light distraction just changes the parameters that CMR operates. But it's even harder if you try to acknowledge that this assumption is almost certainly wrong. 
- Ambiguity of possible "solutions"

I redid the parameter variation simulations for Becky so she could see how each parameter controls the shape of the lag-CRP, SPC and so on. 

But at the same time, I started grappling with the question of how we could begin to account for the differences we see between these two conditions and find a suitable mechanism for CMR w/o losing tons of time.

So I got caught up in exploring an approach for getting becky better information about how these parameters work and what role they should play in her story of the CDCAT behavioral dataset, and also for maybe finding a more systematic approach to characterizing and addressing gaps revealed by a dataset about a model.

The whole generalization test thing didn't seem to applicable here since we only have two conditions and there's no way to fit CMR to, say, the light condition in a way that lets us cleanly predict what might happen in a heavy distraction condition since there's no concrete scaling across those conditions like there are, say, across list lengths or presentation times. So instead it seemed the goal for a cross-condition account of recall performance is good hierarchical model fits. We find a specification of CMR that can fit a smaller number of parameters than if we fit it separately between conditions (26 parameters) but accounts for performance about as well. Instead, we want to specify a more localized mechanism that behaves differently (and thus can be configured separately) between conditions while other parameters can maybe be largely held static across conditions.

To start, I tried to identify the parameters that are most and least useful for accounting for differences between our heavy and light distraction conditions. To do that, I wrote code that enabled me to fit a subset of CMR's parameters to different values based on trial condition while fitting CMR's other parameters to the same value across conditions. For example, I might look for a best fitting light condition encoding drift rate and heavy condition encoding drift rate while only looking for a single primacy scaling parameter.

Next, for each parameter in CMR, I fit the model to CDCATBEH while allowing just that parameter to differ between light and heavy conditions. Then I ranked each parameter by how much letting it differ between conditions improved the base model's performance. To avoid discounting parameters that only add value when other parameters are allowed to differ by condition, I also considered combinations of parameters this way, instead of just one. 

I got some interesting results.

The biggest negative result I got was that some parameters didn't add any value at all to model performance if you let them have different values between conditions. 

Primacy scale, stop probability scale, MFC learning rate, and semantic scale all preferred to be configured to the same value between conditions. In fact, model performance could decline if you tried to fit separate values, since the optimal value for the extra parameter was sometimes not found. This has implied to me that the mechanisms behind differences in these parameters' values aren't touched by our continual distraction intervention. I was most surprised by the sparse impact on semantic scale, since a lot of Becky's results suggests that continual distraction impaired processing of or organization by semantic features. 

But also strikingly, the most useful parameters to let differ between conditions were the recall-focused parameters -- instead of encoding, where distraction events actually happen. I expected the model to favor manipulation of **encoding drift rate** and **primacy decay** between conditions. Instead, the rate of **contextual drift during recall**, the **growth rate of stop probability** over successive item recalls, the heat/**choice sensitivity parameter** controlling how "deterministically" recall competition proceeds, and the **start drift rate** parameters were valued a lot more. 

Why? Looking to the parameter shifting simulations I provided becky provided some clues. A lower encoding drift rate can produce the suppressed TCE we see in the heavy condition. But it also tends to suppress the recency effect rather than enhance it -- and the recency effect in our heavy condition is inexplicably large. And lower primacy decay values can enhance the recency effect, but since it also sustains attention throughout study phases, it also increases the temporal contiguity effect instead of diminishing it or leaving it alone! Accounts of differences in temporal contiguity and recency that focus on changes to contextual cues during retrieval don't face these conflicts.

But we can't credibly interpret this as meaning continual distraction primarily interferes with retrieval mechanisms. 

Oberauer, K., Lewandowsky, S., Farrell, S., Jarrold, C., & Greaves, M. (2012). Modeling working memory: An interference model of complex span. _Psychonomic bulletin & review_, _19_(5), 779-819.

Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D., Conway, A., Cowan, N., ... & Ward, G. (2018). Benchmarks for models of short-term and working memory. _Psychological bulletin_, _144_(9), 885.

Mundorf, A., Lazarus, L. T., Uitvlugt, M. G., & Healey, M. K. (2021). A test of retrieved context theory: Dynamics of recall after incidental encoding. _Journal of Experimental Psychology: Learning, Memory, and Cognition_.

Sean has a variable distraction FR task.

