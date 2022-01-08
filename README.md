# compmemlearn
> a demonstrative python library for computational memory science, but in practice Jordan's working repo for modeling stuff

## Using as a Library

The library demoed in this repository can be used for your projects! To do that, just clone this repository and `cd` to it in your environment. You can then perform an *editable* installation of the library using the command:

`pip install -e .`

The period is important there. Once you do this, you'll be able to use your cloned compmemlearn repo as a regular Python library in the same environment.

## Exploring the Documentation
The [documentation](`https://githubpsyche.github.io/compmemlearn/`) for this project includes the collection of demonstrations and tutorials comprising the educational content of this project. It also tracks the library of Python functions and classes usable if you install the `compmemlearn` library.

## Repository Organization
This project is built using nbdev, a system for exploratory programming. Jupyter Notebooks located in the project's `notebooks` subdirectory represent the "source code" of the project's library and documentation while a collection of tools provided by `nbdev` exports relevant content to library scripts in `compmemlearn/` and documentation html in `docs/`.

Because I also use this repository as a home for development of ongoing research projects, a `workspace/` subdirectory contains works-in-progress notebooks excluded from the main project documentation and a `reports/` subdirectory contains work reporting milestones and outcomes of specific research projects. They also represent useful illustrations of how I work through the research process, but I won't as carefully organize files there for consumption within the context of this library.
