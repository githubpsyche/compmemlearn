I think I will turn to cleaning up the codebase and finishing up generation of my results.

Double beats Single store, for sure.
How about echo vs trace?

In healhy Khana, trace 
in murdock, trace
in lohnas1, trace
in lohnas4, mixed
in lohnas+, trace
in howard, trace
in howard1, trace

But what about learning rate position?
in healy, after by far
in murdock, before by a bit or after if you focus on total waic
in lohnas1, before by a bit
in lohnas4, mixed
in lohnas, mixed
in howard, mixed
in howard1, mixed

So the after model puts on the best performance.

How does the after model compete with CMR?
Healy, BETTER waic but NOT t-test
murdock, BETTER waic AND t-test
lohnas1, WORSE  waic AND t-test
lohnas4, WORSE waic but NOT t-test
lohnas, BETTER waic AND t-test
howard, WORSE waic AND t-test (sort of)
howard1, WORSE waic but NOT t-test

So clear difference in Murdock and Lohnas.
Mixed results in Healy, Lohnas4, howard1
Negative difference in Lohnas c1, howard.

What do I do about this? 
I can dismiss the lohnas c1 results as depending on less data than the other single condition datasets and prioritize evaluating models overall. Then when I focus on repetition effects, my results reveal reliable differences even though they're inconsistent about the direction.