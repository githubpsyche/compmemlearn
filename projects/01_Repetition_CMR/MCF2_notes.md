Good Ending Fits:

cmrde_free_parameters = [
    'encoding_drift_rate',
    'start_drift_rate',
    'recall_drift_rate',
    'shared_support',
    'item_support',
    'learning_rate',
    'primacy_scale',
    'primacy_decay',
    'stop_probability_scale',
    'stop_probability_growth',
    'choice_sensitivity',
    'familiarity_scale']

       x: array([ 0.8288465 ,  0.50993888,  0.95218802,  0.08518901,  0.02942056,
        0.42780997,  2.69029983,  0.3172665 ,  0.02183178,  0.12121347,
        1.64728941, 19.40911784])

Comparative Baseline Fits:
       x: array([8.52857286e-01, 8.88028670e-01, 9.51357591e-01, 5.29883176e-02, 2.22044605e-16, 
       4.19448554e-01, 1.18989510e+00, 2.05877266e+01, 2.18319490e-02, 1.21211203e-01, 
       1.24136833e+00, 0])

What looks pretty similar?
'encoding_drift_rate',
'recall_drift_rate',
'shared_support',
'learning rate'
'stop_probability_scale'
'stop_probability_growth',
'choice_sensitivity'

What's unclear?
'start_drift_rate', (.51 in CMR-DE, .89 in base cmr)
primacy scale      (2.69 in CMR-DE, 1.19 in base cmr)

What looks meaningfully different?
item support (much lower in baseline cmr)
primacy decay (much higher in baseline cmr)

Does this make sense? 
SPC differences find a much steeper primacy effect for base cmr than cmr-de and data. This could potentially explain the entire enhancement of model performance. Less steep primacy decay technically disproportionately enhances right-transition probability. [I can test this by comparing predicted summary stats when primacy scale and/or decay are held to the same numbers.]

Higher primacy scale for CMRD-DE does seem to drive higher first recall of item 0. Apparently doesn't mean we get a higher recall rate overall for item 0, and still not a higher PFR than the data. Higher start drift rate for base_cmr over cmr-de might be the reason why.

I still don't have a clear understanding of how item support affects model performance. Mathematically, it shapes the initial diagonal of Mcf - self connections that determine how much relative support for recall of an item you get when its corresponding contextual unit is activated. That seems to be a forward association thing. Given that I just recalled an item A with mfc associations to item B, item support affects how much I'm now primed to recall item B. 

Why is item support so low though? The idea is that including a familiarity scale mechanism allows the model to configure the item support parameter to a higher value even when learning for repeated items is evidently weaker. In other words, the idea is that familiarity scale lets the model more flexibly configure self-support (mcf's diagonal), improving generalization to control lists, improving prediction of forward transitions in control lists. [I can test this by comparing predicted summary stats when item support is held to the same numbers.]

And what about backward transitions? The familiarity scale mechanism improves prediction of backward transitions a little, but not much. And a consequences seems to be power SPC fits for the latter half of items in a list, though that's just a guess. My intuition was that Mfc learning rate controls this, but I found no improvements in model fit from applying familiarity scale to modulate learning in Mfc as I've found success with for Mcf.

I think I need a visual of Mcf and Mfc to understand this better.

Could it also just be a problem accounting for distraction?