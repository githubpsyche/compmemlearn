![[general - specify and optimize Report Templates Workflow]]

It looks like everything in the flow chart from [[general - specify and optimize Report Templates Workflow]] is working and I primarily need to work on remaining kinks impacting the pdf. How do I reproduce that error? Run quarto preview again? Do I have the corresponding notebook? I should probably reproduce the report files. Then quarto preview. Then debug. 

0. Make sure Murdock 1962 report is generated correctly from the template.✅
1. Reproduce error where quarto can't find `'../../reports/subjectwise_model_evaluation/reports/subjectwise_model_evaluation/results/individual_Murdock1962.pdf'.`)

The individual_Murdock1962.pdf figure is pointed to in cell 8 where I also try to generate a table of fitting results. I use an Asis thing to point to it. But the figure is generated in cell 8 and properly stored in that location. Right? Yes. 

Since it searches for this figure, we know Quarto is able to find the notebook located at a similar position...

Other errors:
```
WARNING: Unable to resolve crossref @fig-MurdOkaFits
WARNING: Unable to resolve crossref @fig-MurdOkaSummary
WARNING: Unable to resolve crossref @fig-Murd62Summary
WARNING: Unable to resolve crossref @fig-LohnasFits
```

The path is wrong. Repeats check for `reports/subjectwise_model_evaluation` twice. The path genuinely doesn't exist. So now the question is how to get the path to the figure to the correct location.

Is the erroneous pathing in the notebook? Perhaps. It looks like quarto assumes that the path is defined relative to the location of the notebook. This would explain this error, anyway. The only reason I switched is because I worried that papermill wouldn't handle the matter correctly.

This seems to solve it based on initial tests using the template notebook. I have to make sure the solution generalizes to the entire pipeline.

Once that succeeds, the next problem is just formatting. Also, this doesn't quite work if assets aren't transferred back to the main repo, as I won't be able to sync to Overleaf.

This is more than a small problem given how `asis` seems to work in Quarto. Implies I should generate reports directly inside the project repository. But then how do I make sure results are stored in the appropriate location? Absolute pathing.

I'm close to a final solution to this. But my current files name the absolute path in my local system for variables like `results_path` and `data_path`. Both `_dispatch.sh` and `_dual_store_parametrize.py` have this issue. And I haven't updated `_single_store_parametrize.py` yet. 

If I'm always going to run these files in the root of compmemlearn, then this isn't a big problem...

`TARGET_PATH` and `PARAMETER_SCRIPT` are the relevant variables in `dispatch.sh`. `PARAMETER_SCRIPT` is only accessed within `_dispatch.sh` to locate `_dual_store_parametrize.py` and `_single_store_parametrize.py`. So I can use relative pathing for that. `TARGET_PATH` is not passed as a variable to the report template. So I think I can use relative pathing there, too. 

`DATA_PATH` has to be defined relative to target path, but this is not too hard and makes no problems for remote execution. Ok, so I finally have a system that generates reports inside a project folder using a report template.

Okay, so now what? I want a quick way to add generated reports to the draft.

It would...detect all the notebooks in the project folder and add them to the draft if they are not already in the draft. But I should figure out a definite report template before I bother with that.

Honestly, maybe I'll just generate the ipynbs, make sure the figures look good, and add them at will manually. Fuck it. They will need context anyway.

Focus. The reason I had problem with arxiv is because I changed it to ignore `/sections` and use top-level heading formatting on second-level headings instead. That doesn't seem to work anymore and the default srreport template is fine, so I'm going to use that.

