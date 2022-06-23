## Goal-Pass All Fitting Results to Sean

I asked what conditions I'd set for sending ICMR results to Sean. They were...
1. Janky Murdock1962 results
2. Janky Lohnas2014 results
3. Logsumexp_CMR Strategy
4. Improving robustness of parameter search

But I mostly decided these were false barriers and that I should send updated results and draft to Sean within the draft first.

But I will focus on cleaning up my subjectwise fit report template so that their outputs can be readily integrated into an arbitrary paper draft. Main mystery is how to report stuff I was previously just passing as print statements.

From there, steps will be to produce the corresponding submodule structure and update quarto render and associated documents to accommodate generated reports.

And then I just focus on the write-up. And then I focus on the extension(s).

Okay, so what now? Let's try quarto render on an arbitrary notebook and start sculpting? Sure.

Ugh, that doesn't quite work. Okay, I'll eyeball it a bit.

```
#| echo: false
#| output: asis
```

Just add this to each cell template at first. Ok, then what?

I need to support the papermill workflow even locally so I can efficiently regenerate reports.
,
What does that require? Existing code depends on SBATCH therefore is not usable here.

Seems instead I reed to call Python directly with the appropriate arguments. Fine. 

To make it easier, I'll synchronize the directory structure. Probably with a git clone. That way I can `pip install -e` and maybe avoid some bits of bullshit. So in the short term, I'll design the script for my local structure.

But to test...I need a structure. Okay.

I'll write it out like the cookiecutter readme. Establish the submodules. Then I'll work out where reports will go..? Do I want them right in the icmr repo? Or in a general spot? Do I want it all in the vault? Yeah. I want figures but not csvs etc.

Anything that could be a pandas df can go into data. Notebooks and figures can be in the vault. Just one copy across vault. 

How do I establish submodules? Just use git add. 

Ok, that's done. Now to set up the vault, I guess. 

Then there's the file reorganization. Pool notes from each repo here.