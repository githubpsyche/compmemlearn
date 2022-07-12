I have to make my own sem_crp function. But first I need to correctly generate the distances matrix. First I need a list of item_strings from the events df that can be subsetted with the same arguments that I use to subset trials. Is that possible? It looks like I cannot because it's an item-level feature. So it looks like I'm tackling this problem earlier than planned.

Okay, so current push: retrieve a list of each item_string in a trial. How?

Let's do it the same way I extract presentations.
pivot_table doesn't seem to handle item_strings right.
Changing the agg_function away from `np.sum` seems to work. But the one suggested at https://stackoverflow.com/questions/34442214/pivoting-a-pandas-dataframe-containing-strings-no-numeric-types-to-aggregate will grow the string if there are repeats. Instead I want to just use the first item_string.
Okay, there are some built in aggregation functions: 

-   `count` / `nunique` – non-null values / count number of unique values
-   `min` / `max` – minimum/maximum
-   `first` / `last` - return first or last value per group
-   `unique` - all unique values from the group
-   `std` – standard deviation
-   `sum` – sum of values
-   `mean` / `median` / `mode` – mean/median/mode
-   `var` - unbiased variance
-   `mad` - mean absolute deviation
-   `skew` - unbiased skew
-   `sem` - standard error of the mean
-   `quantile`

I'll use first. We pass this argument to aggfunc as a string.

How do I fit this retrieved item level information into my simulation code?

Presentation and trial are both item-level information arrays. When I just want the unique items, I can set column to item like so:

`events.pivot_table(index=['subject', 'list'], columns='item', values='item_string', dropna=False, aggfunc='first')`

but if I want item level features for each study or recall event, I'll want:
- column to be "input" when using study events. as long as there is only one input position per trial, there will be no conflict. 
- column to be "output" when tracking recall events.

Then I grab the relevant piece of information as a vector like I would grab presentation or trial. And add the information to the list.

The only thing missing from this is an account of when a feature is a trial-level or item-level element. I can't assume one or the other uniformly anymore. 

I'll have to specify a {column_name: is_item_level} dictionary named `is_item_level` and from there handle columns differently based on the mapped value. Should I try to implement this now? My head is in it, so it's more efficient if I do, I guess.

It looks like for study keys it's sufficient to only pair item strings with study events. I don't have to worry about the recall events. Do I want a nan for invalid recall events? I'm already excluding invalid recall events. 

list_keys will apply to both study and recall eventsm even if they aren't paired with recall or study events, respectively. recall_keys will always apply to recall events, but not necessarily to study events that don't have a corresponding recall event.

If I may handle intrusions later, it's simplest to stick with list_keys. In my data prep, it's important to exclude intrusions though. 

Okay, this seems fixed.