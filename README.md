# compmemlearn
> a demonstrative python library for computational memory science


What is computational memory science and how do you do it? This library and its documentation aim to help track and make useful my best grasp of that question, outlining a reusable workflow for identifying worthwhile research questions given the context of pre-existing work; collecting, preparing, and visualizing relevant data; applying incisive statistical analyses; and communicating results to the broader research community. 

I'm still early on in my career, so to start this library won't be worth much, and the understanding of computational memory science that it reflects will likely be amateurish and even ineffective. In practice, this repository mainly exists to help me avoid forgetting lessons or re-writing code across my efforts on similar research projects. Over time though, I hope evolve into a collection of tools, demonstrations, and tutorials valuable for building acquaintance with the field's research practices and/or bootstrapping any associated projects. At the very least I hope it will help my collaborators better understand what I'm up to!

## Using as a Library

The library demoed in this repository can be used for your projects! To do that, just clone this repository and `cd` to it in your environment. You can then perform an *editable* installation of the library using the command:

`pip install -e .`

The period is important there. Once you do this, you'll be able to use your cloned compmemlearn repo as a regular Python library in the same environment.

## Exploring the Documentation
The [documentation](`https://githubpsyche.github.io/compmemlearn/`) for this project includes the collection of demonstrations and tutorials comprising the educational content of this project. It also tracks the library of Python functions and classes usable if you install the `compmemlearn` library.

## Repository Organization
This project is built using nbdev, a system for exploratory programming. Jupyter Notebooks located in the project's `notebooks` subdirectory represent the "source code" of the project's library and documentation while a collection of tools provided by `nbdev` exports relevant content to library scripts in `compmemlearn/` and documentation html in `docs/`.

Because I also use this repository as a home for development of ongoing research projects, a `workspace/` subdirectory contains works-in-progress notebooks excluded from the main project documentation and a `reports/` subdirectory contains work reporting milestones and outcomes of specific research projects. They also represent useful illustrations of how I work through the research process, but I won't as carefully organize files there for consumption within the context of this library.
