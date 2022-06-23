The generalizeable model evaluation workflow isn't real, right?

Anytime I swap a mild detail of the code hose, everything falls apart. Why?

I think it's pandas. I like the query function and the psifr format. But every transformation is a mess.

What are some examples I can focus on? 

**events_metadata** only returns trials, list_lengths, presentations arrays corresponding to a df. It returns one array per list length.

I then hope I can dynamically filter these arrays with **generate_trial_mask**. That is supposed to select trials based on a provided query. However, the mask is generated per list length! 

When it's time to process subjectwise data, I have to call generate_trial_mask AGAIN to select subject-specific trials and then compare that with my trial mask. 

Then there's generate_objective_function. It assumes it'll get a list of trials, list of presentationsm, list of list lengths. I think it's fine, actually. But it means I have to mind a rule this whole time:  **arguments passed into generate_objective_function for trials and presentations must be lists**

Rules I have to follow:
- arguments passed into generate_objective_function for trials and presentations must be lists
- `data_to_fit` argument for murdock_data_likelihood has to be a list, maybe a numpy List. So does item_counts. 
- Debugging a model class requires changing the library code! This substantially limits its value as a library for general use. 

Issues I'd like to address:
- Base definition for model_classes and other library functions lack numba spec; instead I selectively add it within my codebase. 
- I don't want to use trial_queries outside the main function. 
- Accurately tracking item-level extras in my simulate_df_from_events code. Will be necessary for performing analyses on semantic features.
- Add comparison by conditions, not just sim vs data. Seems to merely require making `trial_query` a list of queries. 

I've defined some issues on github that I might focus further discussion on here.