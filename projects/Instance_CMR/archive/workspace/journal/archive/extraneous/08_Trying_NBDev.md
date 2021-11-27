# Trying nbdev
`nbdev` is a library that allows you to develop a python library in Jupyter Notebooks, putting all your code, tests and documentation in one place. It may be a bit much for my purposes, but I think developing projects this way is at least good practice and might teach me discipline useful for bigger projects later on. 

In particular, I want to get more responsible about the structure of my code. Even though the central goal of my scientific projects is a set of reported findings, my code should be written as a reusable, maintainable and readable library that can form the foundation of further work. Aspects of `nbdev` are designed to enforce these good habits.

The big question I still need to work out about `nbdev` is how friendly it is when it comes to script editing. I wrote the initial exemplar model in a simple script, and it was a great way to focus my attention on singular units of my code. If I finish some part of my library and then edit the produced script, will it sync the results with my notebook or just yell at me? Similarly, if I create different versions of the same function or class, will it too aggressively sync my old code, or otherwise create problems? 

I think the key thing is that I have to take version control seriously as an idea and get comfortable with not keeping old code in a current repo if it's literally old code. The repository history will still keep track of my old versions!

Similarly, it's probably okay to distinguish my notes from my library, even when engaged in literate programming. There's a time and place for self-obsessed ruminating, but not in the middle of my code; instead, it probably is better after all to focus the text I include in my notebooks on explaining/documenting instead of just figuring things out, something the files in this directory can handle. 

Let's try it out and see how clunky the experience is.