# March Model Maintenance
As quickly as possible we want to make sure that:
- Model speed and fitting performance is at least as good as previous benchmarks
- Models are accurately documented
- Parameters affect model behavior the way they're intended to


## Model Comparison
But how will I do this?

Well let's think about how I want to organize the overall documentation. 

One group of notebooks solely outlines models.

Another group of notebooks outlines some typical ways the models might be analyzed.

A third group of notebooks marshalls models and analysis routines to answer specific questions about the models.

And a final group of notebooks organizes supplementary material, like ancillary notes that wouldn't be the focus of any paper.

I'm mostly done with the first two groups, and and trying to get to work on the third. But groups 1 and 2 need some maintenance. Where does that go?

Well frame it as a report. Performance Benchmarks? 

No, it's still model comparison is what it is. I'm working on the section of the paper that relates ICMR with CMR.

What happens in this model comparison notebook?

Get timing and performance info for both models.

(Compare against previous benchmarks.)

(Test approaches to improvement.)

Compare parameter behavior, making any necessary updates. 
(ICMR_Parameter_Bounds can be expanded into a general analysis of parameter impact on model behavior.)

Update documentation to match final state of model.


## Do I Want to Redo The Memory Analyses?
Right now, much of my model analysis code is unduly segmented; a lot of functions that work for ICMR don't work for CMR, and vice versa. This makes for some shitty follow-up notebooks. Do I bother fixing my notebooks or push forward?

I'm gonna push forward.


## Issues


### Ditch Sync Call
First, Jupytext's sync call doesn't play well with my cross-platform approach. Let's give up and move back to --to.

### README still missing figures
Not sure why.

### CMR Documentation Missing Any Explanation of Model
That's always been lower priority. 

### It looks like my version of data likelihood is outdated
The version inside fitting_models_to_data no longer works for the current version of InstanceCMR.

### Model Fit to First Subject Is Worse Than It Used to Be
Will probably want to revert the model somehow.

```python

```
