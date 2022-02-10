According to deficient-processing theory, memory systems devote fewer resources to encode items that have already been encoded recently, with this effect diminishing with increased time or items between study events. Within the framework of retrieved context theory, the primary outcome of encoding is association in memory between the studied item and current temporal context. Later retrieval of an item then retrieves encoded associations and updates the current state of context before it is used as the cue for the next item recall. For an item presented at positions $i$ and $j$ in a list, deficient encoding of its second presentation corresponds when the item is later recalled with weaker reinstatement of the temporal context associated with the item's second presentation. This in turn drives an attenuated lag-recency effect relative to the item's second presentation: after a repeated item is retrieved in a free recall task, the combined theories predict rarer transitions to recall of items near this second presentation (i.e., items at any of $\{\ldots, j-2, j-1, j+1, j+2, \ldots\}$) compared to items presented near their first presentation (at $\{\ldots, i-2, i-1, i+1, i+2, \ldots\}$).

We look for evidence of a stronger temporal contiguity effect for the first presentation of an repeated item relative to its second in the free recall dataset reported by Lohnas & Kahana (2014). In the dataset, 35 subjects performed delayed free recall of 48 lists. Subjects encountered four different types of lists: 
1. Control lists that contained all once-presented items;  
2. pure massed lists containing all twice-presented items; 
3. pure spaced lists consisting of items presented twice at lags 1-8, where lag is defined as the number of intervening items between a repeated item's presentations; 
4. mixed lists consisting of once presented, massed and spaced items. Within each session, subjects encountered three lists of each of these four types. 

In each list there were 40 presentation positions, such that in the control lists each position was occupied by a unique list item, and in the pure massed and pure spaced lists, 20 unique words were presented twice to occupy the 40 positions. In the mixed lists 28 once-presented and six twice-presented words occupied the 40 positions. In the pure spaced lists, spacings of repeated items were chosen so that each of the lags 1-8 occurred with equal probability. In the mixed lists, massed repetitions (lag=0) and spaced repetitions (lags 1-8) were chosen such that each of the 9 lags of 0-8 were used exactly twice within each session. 

To measure the lag-recency effect relative to the first and second presentation of a repeated item, we found the probability of making a recall to serial positions $i+lag$ or $j+lag$ immediately following recall of an item presented at serial positions $i$ and $j$. We identified in the dataset's mixed list trials all recalls of repeated items with at least 4 items intervening presentations. For each of these recall events, we measured the difference in serial position of the next recalled item from each serial position at which the repeated item was presented -- their presentation-relative serial lag. We also counted across considered recall events the number of number of transitions possible to an item of each first-presentation-relative and second-presentation-relative serial lag. From this, we found for each presentation-relative serial lag the conditional probability of making a transition in recall to the item with the serial lag given that the transition was possible. Figure ~\ref{fig:AltContiguity} plots the outcome of this analysis for lags $\pm 2$ relative to the first and second presentation of considered repeated items.

```python

```

We also expect deficient encoding of an item's second presentation within the framework of retrieved context theory to impact the rate of transition during recall from nearby items to the repeated item relative to the rate of transitions from items near the first presentation of the repeated item. To test this hypothesis, for spaced items (lag >= 4) in mixed lists we find the proportion of times, given that a subject made a transition from an item in $S_i = {i-2, i-1}$ or $S_j = {j-2, j-1}$ during free recall and the item presented at ${i, j}$ has not been recalled, that they then transition to recall of that item.

```python

```

From my notes on Chapter 9 of Crowder 1972 book Principles of Learning and Memory.
Elmes et al., 1972]] - Look at items presented nearby to repeated items.
If variability of attention occurs for repeats, perhaps this
facilitates performance on nearby items.  Repeat with lag 0, 3, 10.
Performance on repeated word: 12, 21, 23%.  Performance on word
following repetition: 38, 25, 18%.  Consistent with the idea that when
lag is small (0) the subject attends a bit less to the repeated word,
and frees up some resources for the next word.  Would be interesting
to look at the conditional probability of recall of the word following
the repeated item, given recall of the repeated word.

```python

```
