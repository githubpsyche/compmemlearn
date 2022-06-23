## Goal-Submodule Project Structure
I want to be able to use a single vault across my projects. This way, I can take advantage of relationships between projects, work on drafts/ideas without switching between vaults, etc.

At the same time, by separating projects into submodules instead of just using a simple subdirectory for different projects, I can develop within compmemlearn, but pass Sean specific draft repos. Isolation without separation.

On the coding side, I want to be able to work on projects within compmemlearn. VSCode's workspace feature supports this to some extent; but I want to be able to programmatically generate project assets in the relevant project subdirectory. That doesn't really require nested project structure either, but whatevs. It means I don't have to duplicate things like datasets, code, and other assets just because they belong to a different project.

Git cloning for ACCRE simulations and other operations gets simpler w/ submodule project structure (though I have to use commands I've never used before).

0. Develop plans, writings, and literature reviews in projects subdirectory in compmemlearn.
1. Code analysis functions and reproducible/extendable workflows ("report templates") in library subdirectory in compmemlearn.
2. Pass audience-focused analysis outcomes and writings to submodules stored in projects subdirectory in compmemlearn
3. Compile selected writings and analysis outcomes in submodules into tex file(s) and pdf(s) using quarto and sync the repository with overleaf
4. Upon submission, just copy the relevant compmemlearn library subdirectory into the repo and instruct readers to `pip install -e` the product.