### 2022-06-15 Batch Processing
One is streamlining the batch execution process. I want to be able to clone a repo on ACCRE, load python, pip install requirements, and execute a configured bat file, then sync the result back to github using git. Why do I want to do that? I mean, I already have a flow that requires just as much manual work.

No, the real problem is that I'm missing a flow for doing this locally. I don't have SLURM locally, but sometimes I'm just as interested in re-rendering results that already exist on my own computer. This is relevant for ICMR as well, since I'm trying to update my results section.

**What would be your first step on this?** My understanding from exploring the issue before is just that I have to match directory structures and update the bat file with an extra line per operation. Do it right, some lines will fail when run locally, other lines will fail when run on ACCRE, and the outputs will nonetheless be consistent between execution locations.