
[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

In 'Testing a Difference in Means', we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.

An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Power.

Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.

Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?

This markdown file has been converted from a Jupyter notebook using [convert_notebooks_to_markdown.py](./convert_notebooks_to_markdown.py).

# Answer

The p-values resulting from the two different models (permutation and resampling) are slightly--but not significantly--different. So in this case, I would say it does not matter which method is used. However, I can see the difference becoming more critical in cases where there are significant outliers or very small total population sizes. (Although resampling and permutation methods themselves may not be the best choice in these situations anyway.)

**NOTE:** I may not get time to do this before the assignment is due, but I suspect there may be an error in the calculation of `max_diff` for `totalwgt_lb` because the same value is produced for `actual`.



```python
print(tabulate(perm_stats,
               headers=perm_stats.columns.tolist(),
               tablefmt='pipe',
               floatfmt=".4f")
     )
```


|          |   prglngth |   totalwgt_lb |
|:---------|-----------:|--------------:|
| actual   |     0.0751 |        0.1248 |
| max_diff |     0.1617 |        0.1248 |
| p_value  |     0.1835 |        0.0001 |




```python
print(tabulate(resample_stats,
               headers=resample_stats.columns.tolist(),
               tablefmt='pipe',
               floatfmt=".4f")
     )
```


|          |   prglngth |   totalwgt_lb |
|:---------|-----------:|--------------:|
| actual   |     0.0751 |        0.1248 |
| max_diff |     0.1461 |        0.1248 |
| p_value  |     0.1833 |        0.0000 |


# Code



```python
from __future__ import print_function
import numpy as np
import scipy.stats as stats
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from tabulate import tabulate
from load_ThinkStats import load_FemPreg

%matplotlib inline
# %config InlineBackend.close_figures = False
```


Make this reproducible.



```python
np.random.seed(42)
```


## Import and clean data

Select only live births as before and group the data in to first vs other births.



```python
df = load_FemPreg(True)

df.dropna(subset=['birthord', 'prglngth', 'totalwgt_lb'], inplace=True)

df = df.loc[df.outcome == 1]

assert df.shape[0] == 9038
assert (df.outcome==1).all() == True

df['birthord'] = df.birthord.astype(np.int)
df['birthord_bin'] = pd.cut(df.birthord, [0, 1, df.birthord.max()])

df = df[['birthord_bin', 'prglngth', 'totalwgt_lb']]
df = df.sort_values('birthord_bin').reset_index(drop=True)
```


## Shuffle or permute data

Helper functions to either permute or resample a dataframe.



```python
def permute_data(df, column_sort='birthord_bin'):
    
    # Ensure we don't change the original data
    df = df.copy()
    
    # Shuffle the classifier column and reset values
    # This is the same as permuting the data
    df[column_sort] = np.random.permutation(df[column_sort])
    df.sort_values(column_sort, inplace=True)
    
    return df


def resample_data(df, column_sort='birthord_bin'):
    
    # Ensure we don't change the original data
    df = df.copy()
    
    # Need unique indexes
    df.reset_index(drop=True, inplace=True)
    
    # Determine group names and sizes
    freq_table = df[column_sort].value_counts().sort_index()
    m, n = freq_table.values
    m_name, n_name = freq_table.index

    # Select the rows randomly 
    m_data = df.loc[np.random.choice(df.index, m, replace=True)]
    n_data = df.loc[np.random.choice(df.index, n, replace=True)]
    
    # Set sort column value
    m_data = m_data.drop(column_sort, axis=1)
    n_data = n_data.drop(column_sort, axis=1)
    m_data[column_sort] = m_name
    n_data[column_sort] = n_name
    
    # Combine and return the new dataframe
    new_df = pd.concat([m_data, n_data], axis=0).reset_index(drop=True)
    assert new_df.shape[0] == df.shape[0]
    
    return new_df
```


Calculate the actual difference in means between first borns and all others.



```python
get_mean_diff = lambda df: ( df.groupby('birthord_bin')
                            .mean().diff().abs()
                            .dropna().reset_index(drop=True) )

actual = get_mean_diff(df)
```




```python
print(tabulate(actual,
               headers=actual.columns.tolist(),
               tablefmt='pipe',
               floatfmt=".4f")
     )
```


|        |   prglngth |   totalwgt_lb |
|-------:|-----------:|--------------:|
| 0.0000 |     0.0751 |        0.1248 |


Run 10000 permutations or samplings and calculate the absolute mean difference between the permuted/resampled birth order groups for birthweight and pregnancy length.



```python
niter = 10000

permutations = pd.concat( [ get_mean_diff(permute_data(df)) 
                            for _ in range(niter)
                          ]).reset_index(drop=True)

resamplings = pd.concat( [ get_mean_diff(resample_data(df)) 
                           for _ in range(niter)
                         ]).reset_index(drop=True)
```


Determine statistics on the 10000 trials of permutations and resamplings.



```python
def get_pvalue(df, actual=actual):
    return df.sub(actual.squeeze(), axis=1).ge(0.).sum() / np.float(df.shape[0])

def get_max_diff(df, actual=actual):
    return df.sub(actual.squeeze(), axis=1).abs().max()

perm_stats = pd.DataFrame({'p_value': get_pvalue(permutations), 
                           'actual':actual.squeeze(), 
                           'max_diff':get_max_diff(permutations)}).T

resample_stats = pd.DataFrame({'p_value': get_pvalue(resamplings), 
                           'actual':actual.squeeze(), 
                           'max_diff':get_max_diff(resamplings)}).T
```




```python
print(tabulate(perm_stats,
               headers=perm_stats.columns.tolist(),
               tablefmt='pipe',
               floatfmt=".4f")
     )
```


|          |   prglngth |   totalwgt_lb |
|:---------|-----------:|--------------:|
| actual   |     0.0751 |        0.1248 |
| max_diff |     0.1617 |        0.1248 |
| p_value  |     0.1835 |        0.0001 |




```python
print(tabulate(resample_stats,
               headers=resample_stats.columns.tolist(),
               tablefmt='pipe',
               floatfmt=".4f")
     )
```


|          |   prglngth |   totalwgt_lb |
|:---------|-----------:|--------------:|
| actual   |     0.0751 |        0.1248 |
| max_diff |     0.1461 |        0.1248 |
| p_value  |     0.1833 |        0.0000 |

