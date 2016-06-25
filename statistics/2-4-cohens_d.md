
[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

This markdown file has been converted from a Jupyter notebook using [convert_notebooks_to_markdown.py](./convert_notebooks_to_markdown.py).

# Answer

Cohen's d for firstborn babies vs all others has been calculated for the difference between pregnancy length (`prglngth`) and total weight (`totalwgt`) for all pregnancies (`all`) and for only those determined to be full-term (> 27 weeks) (`full`). 

I decided to examine the difference between all pregnancies and only those that were full term based on Slack discussion about which group was used in the book.

All values determined for Cohen's d are less than 0.1 of their respective pooled standard deviations. Thus, these are small effect sizes. We can determine that there is little difference between pregnancy length and total weight for firstborn vs other babies, and this is true regardless of whether non-full term pregnancies are examined.





|      |   prglngth |   totalwgt |
|:-----|-----------:|-----------:|
| all  |      0.028 |      0.089 |
| full |      0.029 |      0.087 |


# Code



```python
from __future__ import print_function
import pandas as pd
import numpy as np

from tabulate import tabulate
from load_ThinkStats import load_FemPreg
```


Load the 2002 female pregnancy results. This uses a custom library I wrote called [`load_ThinkStats`](load_ThinkStats.py).



```python
df = load_FemPreg(True)
df.rename(columns={'totalwgt_lb':'totalwgt'}, inplace=True)
```


## Clean and bin the data into first born vs others

Drop any invalid (`na`) data and select only live births. Separate the birth data into two groups (first born and all others).



```python
df.dropna(subset=['birthord', 'prglngth', 'totalwgt'], inplace=True)
df = df.loc[df.outcome==1]

assert df.shape[0] == 9038
assert (df.outcome==1).all() == True

df['birthord'] = df.birthord.astype(np.int)
df['birthord_bin'] = pd.cut(df.birthord, [0,1, df.birthord.max()])
```


Print the bin for each birth order to ensure the groups are as expected.



```python
print(tabulate(df[['birthord_bin','birthord']]
                 .drop_duplicates()
                 .set_index('birthord_bin'), 
               headers=['birthord'],
               tablefmt='pipe')
      )
```


|         |   birthord |
|:--------|-----------:|
| (0, 1]  |          1 |
| (1, 10] |          2 |
| (1, 10] |          3 |
| (1, 10] |          4 |
| (1, 10] |          5 |
| (1, 10] |          6 |
| (1, 10] |          7 |
| (1, 10] |          8 |
| (1, 10] |          9 |
| (1, 10] |         10 |


## Calculate birth weight statistics

For each of the two groups (first born and all others), calculate the mean and variance pregnancy length and birthweight. Also determine the number of births in each of the two groups.

The above statistics were calculated separately for all pregnancies and for those determined to be full-term (longer than 27 weeks, as defined by the book).



```python
def create_stats(df, prglngth_min):
    # A function to do dataframe munging for 
    # all and full-term pregnancies
    
    if prglngth_min >= 27:
        term='full'
    else:
        term='all'
        
    return ( df[['birthord_bin', 'totalwgt', 'prglngth']]
             .query('prglngth > {}'.format(prglngth_min))
             .groupby('birthord_bin')
             .agg(['mean','var','count'])
             .assign(term=term)
             .set_index('term', append=True)
            )


stats = pd.concat([create_stats(df, -1), create_stats(df, 27)]).sort_index()
```


Normalize the counts to create percent of total.



```python
stats.loc[:,(slice(None), 'count')] /= ( stats.loc[:,(slice(None), 'count')]
                                         .sum(axis=0, level=1)
                                       )

stats = stats.rename(columns={'count':'pct'}).sort_index(axis=1)
```


View the statistics table.



```python
print(tabulate(stats,
               headers=map(lambda x: '_'.join(x), stats.columns.tolist()),
               tablefmt='pipe',
               floatfmt=".3f")
     )
```


|                     |   prglngth_mean |   prglngth_pct |   prglngth_var |   totalwgt_mean |   totalwgt_pct |   totalwgt_var |
|:--------------------|----------------:|---------------:|---------------:|----------------:|---------------:|---------------:|
| ('(0, 1]', 'all')   |          38.609 |          0.483 |          7.808 |           7.201 |          0.483 |          2.018 |
| ('(0, 1]', 'full')  |          38.723 |          0.483 |          5.997 |           7.238 |          0.483 |          1.827 |
| ('(1, 10]', 'all')  |          38.534 |          0.517 |          6.672 |           7.326 |          0.517 |          1.944 |
| ('(1, 10]', 'full') |          38.655 |          0.517 |          4.704 |           7.356 |          0.517 |          1.803 |


## Calculate Cohen's d

Use the statistics table to calculate Cohen's d for pregnancy length and birthweight for firstborn vs. all other babies.

Cohen's d is the difference in means between two groups divided by their pooled standard deviations:
$$d = \frac{\bar{x_1} - \bar{x_2}}{S}$$



```python
pooled_std = ( stats.xs('var', axis=1, level=1)
               .mul(stats.xs('pct', axis=1, level=1))
               .sum(axis=0, level=1)
              ).pipe(np.sqrt)

cohens_d = ( stats.xs('mean', axis=1, level=1)
             .diff(axis=0, periods=2)
             .dropna()
             .reset_index(level=0, drop=True)
             .abs()
            ).div(pooled_std)
```


View the table of Cohen's d values.



```python
print(tabulate(cohens_d,
               headers=cohens_d.columns.tolist(),
               tablefmt='pipe',
               floatfmt=".3f")
     )
```


|      |   prglngth |   totalwgt |
|:-----|-----------:|-----------:|
| all  |      0.028 |      0.089 |
| full |      0.029 |      0.087 |

