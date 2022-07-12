# CDCATBEH Notes

## Thursday, July 7
Jordan Gunn
  3:53 AM
fits are done. i think these are these results you wanted? i have some figures too if they turn out to be desirable. serial position curves are kind of odd


beckycutler
  9:15 AM
you are wonderful :pray:


beckycutler
  9:52 AM
yeah, figures would be awesome! I am intrigued by SPC because the main thing we’re trying to capture is that drop in primacy items with heavy distraction. I wonder if we can explain that with a decrease in a ‘start-list-context’ parameter?


beckycutler
  2:38 PM
woo - okay im seeing that we do have Bstart !! and that is significantly lower for heavy. This is exciting!


Jordan Gunn
  3:25
as you can see, even though the PFRs are well accounted for, the CRPs and the SPCs especially are quite off. I have to guess it has something to do with the category structure of the stimuli or something
3:26
b_start is significantly lower for heavy because the PFR curves are significantly different; recall disproportionately starts at the first item in the light condition


beckycutler
  5:40 PM
Thank you for these figs! Yeah there’s definitely some nuances that aren’t captured and I agree the category structure is probably key. It’s interesting because I have been kind of proposing that the effect is ‘heavy distraction = less primacy’, but there is this additional insight that suggests ‘heavy distraction = less primacy, because there is more recency’.
What are your thoughts on how the block structure might be affecting this? Like we were discussing, it’s nearly impossible to disentangle semantic and category within block, but they do contain this mini temporal structure (1,2,3). Although you can see in this fig that that info is captured in the overall SPC


## Friday, July 8th

Jordan Gunn
  6:51 AM
still wrapping my head around the design. i really like your proposal; it's super succinct. I'm kind of interested in following up on the analysis plan proposed there. i might be able to have clearer ideas about how category structure affects recall after a little more thinking


Jordan Gunn
  8:01 AM
First, thoughts on the effect of the task condition on primacy. Without considering the fitted parameters (which I think can't be taken too seriously due to the poor SPC fits), my intuition about the difference in primacy might have been that it builds support for the idea that the primacy effect is primarily an attentional phenomenon. Sederberg et al (2008) proposed that the primacy effect is driven by increased attention to initial items in a list. Increased initial item attention + stronger reinstatement of start-of-list context at the beginning of retrieval can interact to drive a primacy effect in a PFR curve. For example, with weaker attention to early items, reinstating start of list context has a lower probability of subsequently triggering recall of the list's first couple of items (because the stored association between start-of-list context and initial items is weaker). Since we interpret the distraction task as primarily interfering with attention, I kind of lean toward the former mechanism instead of the latter as an explanation for the effect of condition on primacy, but either way it's hard for me to imagine an experimental design that separates these two mechanisms so practically it might be a difference that makes no difference.


Jordan Gunn
  8:08 AM
As for the primacy/recency trade-off. I think CMR usually predicts a trade-off will happen. The way I think about it is that according to CMR, at the end of recall, you have the context from after processing the last item -- call it $c_end$. When you start recall, your contextual state is a blend of $c_last$ and $c_start$, with the relative weighting of the latter over the former decided by $beta_start$. So any increase in weighting of $c_start$ in your retrieval cue and support for initial study items has to be at the expensive of weighting for $c_end$ and support for terminal study items.


Jordan Gunn
  8:21 AM
did you (or anyone else) ever try the "simulate distraction as a study event" thing your proposal mentions? i don't expect it to improve fits to one condition, but it could make it easier for the model to generalize over different conditions (e.g. distraction vs no distraction).
8:25
only problem is that i don't see how this would explain the weakened primacy effect. the additional proposal you made that the distraction task weakens 'temporal binding' in general seems necessary to support that possibility. But I'm actually not sure about that. There's some possibility that weakening connections between a list's first item in context-to-feature memory and successive items according to the "distractions as study events" hypothesis can also inadvertently weaken retrievability of a list's initial items


Jordan Gunn
  9:06 AM
I don't really understand why the block structure is messing up fits so much, but my guess is that it makes it hard for the model to settle on a single configuration for parameters controlling temporal contiguity. Same-category adjacent items are probably much more tightly connected than different-category adjacent items but our model wants relatively static connections that only really vary in strength as a function of distance from start of list. Eventually, I'll try fitting Semantic CMR to this data instead to get a clearer idea of how mysterious these results are. The fancier semantics models seem to be able to recognize category differences pretty well on their own (though object words like "acorn" are suspiciously similar to names w/ homonyms like "Halle Berry"), and I can code up a simple category matrix to provide distances to the model, too.


Jordan Gunn
  9:14 AM
Your results finding weaker semantic clustering as a function of light/heavy distraction are super interesting as they imply that the semantic organization we normally see in free recall data is in part driven by encoding processes that can be disrupted. But since same-category items are temporally clustered during list study, I worry that the analysis can be explained in terms of weakened temporal organization as a function of light/heavy distraction. I think it might be possible to create a version of the analysis that controls for this possibility, though, or to study the question by fitting an applicable CMR variant to each condition and plotting the parameter value distributions relevant for semantic organization.


Jordan Gunn
  9:53 AM
So to summarize...
1) Two mechanisms enforce the primacy effect according to CMR -- increased attention to initial items and increased reinstatement of start-of-list context at the start of retrieval -- and it's hard to tease out which is most relevant here, especially while the model is performing so poorly. I think some simple simulation experiments where we manipulate the strength of each mechanism while holding other parameters at 'default' values and observe the impact on summary statistics might help us get a better intuition about this, though.
2) While we can be sure that reduced global attention can drive a diminished primacy effect in our heavy distraction condition according to CMR, it's mysterious how conceptualizing distraction as adding intervening dummy events to a list will influence primacy. Usually, increasing study list length reduces primacy and recency effects in a free recall task. Still, I'm unsure if that pattern holds when the extra list items aren't involved in the recall competition. I think it's worth checking out what CMR predicts here.
3) The poor fits to SPCs and CRPs we observe in the above figures, plus our reliance on model parameters for some of our theoretical inferences, makes me think it's essential to factor category/semantic features into our model before fitting. Along with making the model more helpful in interpreting our summary statistics, this might help us analyze semantic effects, too.
4) CMR does a reasonably good job of generalizing across list length conditions. If you fit the model to subjects studying and recalling lists with 20 items, it can do a reasonably good job of predicting subjects' performance on lists with 40 items. It'd be really cool to find a model specification that can do the same thing across inter-item distraction conditions. I think exploring the above ideas would help chart a course toward that, but in the short term, I think I will redo fits with semantic connections and see if the SPCs/CRPs are meaningfully improved.

## Saturday, July 9th

beckycutler
  11:31 PM
I’ll share these vector space models that might be useful to build in the semantic associations, they’re the ones I used for all semantic analyses. USE is the Google sentence encoder (512 features), I scraped wikipedia entries and used the DAN variant. Wiki2vec is the model developed by Neal (300 features).
Idk whether it will make a difference for the fits? but it will at least give us confidence that the behavioural, neural and modeling analyses are all based on the same conceptual models… let me know what you think


Jordan Gunn
  8:58 PM
My codebase is built to use a certain interface to distance metrics but since I already need to change it to support homemade category-based features, I'll aim to have it support stuff like in your CSVs too.


Jordan Gunn
  9:05 PM
I think I'm going to make a push to achieve 3 things relevant for this before Monday. First, I'll see if fitting across subjects instead of per subject improves the base (and other) models' ability to account for the SPC. This will effectively test my guess that it's the small trial count per subject/condition that's making the model struggle to fit. Whatever the outcome, second I'll try to improve my codebase so it can use pre-generated vectors like what you share. This will actually make a lot of my code faster along with helping clarify the role of category/semantic organization in all this. And finally, I'll make sure my figure generating code reliably generates figure labels and whatnot (unless you'd rather I exclude them?).