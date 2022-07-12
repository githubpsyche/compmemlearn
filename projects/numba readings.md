Numba is often used as a core package so its dependencies are kept to an absolute minimum, however, extra packages can be installed as follows to provide additional functionality:

-   `scipy` - enables support for compiling `numpy.linalg` functions.
    
-   `colorama` - enables support for color highlighting in backtraces/error messages.
    
-   `pyyaml` - enables configuration of Numba via a YAML config file.
    
-   `icc_rt` - allows the use of the Intel SVML (high performance short vector math library, x86_64 only). Installation instructions are in the [performance tips](https://numba.readthedocs.io/en/stable/user/performance-tips.html#intel-svml).

> This suggests that I might be able to improve my numba experience with improved error feedback and maybe maybe even speedier code.

As a side note, if compilation time is an issue, Numba JIT supports [on-disk caching](https://numba.readthedocs.io/en/stable/reference/jit-compilation.html#jit-decorator-cache) of compiled functions and also has an [Ahead-Of-Time](https://numba.readthedocs.io/en/stable/reference/aot-compilation.html#aot-compilation) compilation mode.

If true, _nogil_ tries to release the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock "(in Python v3.10)") inside the compiled function. The GIL will only be released if Numba can compile the function in [nopython mode](https://numba.readthedocs.io/en/stable/glossary.html#term-nopython-mode), otherwise a compilation warning will be printed.

> When should I use nogil mode? Always? Sometimes?

> I like the idea of maybe having a library wide setting I can change that will turn nopython mode on or off but this doesn't wuite seem to be the goal.

The _error_model_ option controls the divide-by-zero behavior. Setting it to ‘python’ causes divide-by-zero to raise exception like CPython. Setting it to ‘numpy’ causes divide-by-zero to set the result to _+/-inf_ or _nan_.

> I'm probably unfamiliar because I'm still using numpy inside numba.

If True, `boundscheck` enables bounds checking for array indices. Out of bounds accesses will raise IndexError. The default is to not do bounds checking. If bounds checking is disabled, out of bounds accesses can produce garbage results or segfaults. However, enabling bounds checking will slow down typical functions, so it is recommended to only use this flag for debugging. You can also set the NUMBA_BOUNDSCHECK environment variable to 0 or 1 to globally override this flag.

> This is good to keep in mind. Also reminds me that env variable is the recommended way to control compilation.

Guvectorize: Generalized version of [`numba.vectorize()`](https://numba.readthedocs.io/en/stable/reference/jit-compilation.html#numba.vectorize "numba.vectorize"). While [`numba.vectorize()`](https://numba.readthedocs.io/en/stable/reference/jit-compilation.html#numba.vectorize "numba.vectorize") will produce a simple ufunc whose core functionality (the function you are decorating) operates on scalar operands and returns a scalar value, [`numba.guvectorize()`](https://numba.readthedocs.io/en/stable/reference/jit-compilation.html#numba.guvectorize "numba.guvectorize") allows you to create a [Numpy ufunc](http://docs.scipy.org/doc/numpy/reference/ufuncs.html) whose core function takes array arguments of various dimensions.

