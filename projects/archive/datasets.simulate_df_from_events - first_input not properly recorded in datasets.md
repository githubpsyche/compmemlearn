  

Seems very likely that there's a bug in simulate_from_events where first_input improperly encodes presentation_index (study position) instead of using find_first to find the appropriate study position. The error is also apparently present in my data preparation code. What is first_input even for if I'm doing this?

In `events_metadata`, I'm using it to generate my trials_array. I make the same erorr in `contiguity_disruption.Delayed_Recall.simulate_df_from_presentation` and related scripts.

Error is in both lohnas and howakaha csvs. How is it that my analyses work anyway? Do they? How did I get this far?

It's because I was usually matching the value in my trials array back to the item at the indicated study position. This is what the lohnas data likelihood function does anyway. This means it was always pointing to the same item anyway. My extracted presentations array always retrieved an item index, too. So as long as I wasn't assuming my trials `study_positions_in_recall_order` always pointed to the first study position, I was golden.

What about the more advanced repetition effect analyses?

Lag-CRP? Fine if dependencies are alright.

recall_by_all_study_positions? It takes recall_by_first_study_position as an argument. But then only uses its value to find the item_index in presentation. So, fine.

What about the RPL function?

Trial is converted into a 0-indexed study position vector.

Then I scan through each unique item in my presentations vector. I first find the first study position of that item and then I look for its second, so I can track a lag. Critically, I decide if the item has been recalled by checking if the first study position is in my trial vector. This shouldn't be possible given the bugs in my code, but let's see.

It looks like I previously used the presentations and trials vectors generated directly from prepare_lohnas2014_data. This would explain why I plotted the RPL just fine in this notebook.

(I'll probably want to refactor RPL like I did the benchmark analysis notebooks.)

What about the repetition contiguity analysis?

Roughly the same thing. I previously used the trials array generated directly from the preparation function. I haven't yet integrated this function into the workflow.

Actually, it seems that I have newer code elsewhere (in the repetition_cmr repository).

I also only use trials to identify item indices within my presentations array. So the analysis is fine. That code will be something to review later. I'm so dumb.

Next...neighbor contiguity.

I have a lot of versions of the same function that probably all don't work haha. Result seems to be the same when I re-run at least. Ah, what a mess.

Okay, anyway, I'll update the code above to address the issue.