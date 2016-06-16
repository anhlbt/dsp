
[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)



Suppose that you draw a sample with size `n = 10` from an exponential distribution with `lambda = 2`. Simulate this experiment 1000 times and plot the sampling distribution of the estimate `L`. Compute the standard error of the estimate and the 90% confidence interval.

Repeat the experiment with a few different values of n and make a plot of standard error versus n.

This markdown file has been converted from a Jupyter notebook using [convert_notebooks_to_markdown.py](./convert_notebooks_to_markdown.py).

# - [ ] Finish this question

# Answer



```python
print('ANSWER GOES HERE.')
```


ANSWER GOES HERE.


# Code



```python
import numpy as np
import scipy.stats as stats

import matplotlib.pyplot as plt
import seaborn as sns

from tabulate import tabulate
from load_ThinkStats import load_FemPreg

%matplotlib inline
# %config InlineBackend.close_figures = False
```

