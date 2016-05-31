
[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?


```python
import pandas as pd
import numpy as np
from tabulate import tabulate
```

Load the 2002 female pregnancy results. This uses a custom library I wrote called `load_ThinkStats`.


```python
from load_ThinkStats import load_FemPreg
df = load_FemPreg(True)
```

## Clean and bin the data into first born vs others

Drop any invalid (na) data and separate the birthdata into two groups (first born and all others).


```python
df.dropna(subset=['birthord'], inplace=True)
df['birthord'] = df.birthord.astype(np.int)

df['birthord_bin'] = pd.cut(df.birthord, [0,1, df.birthord.max()])
```

Print the bin for each birth order to ensure the groups are as expected.


```python
print(tabulate(df[['birthord_bin','birthord']].drop_duplicates().set_index('birthord_bin'), 
               headers=['birthord'],
               tablefmt='pipe',
               floatfmt=".3f")
      )
```

|         |   birthord |
|:--------|-----------:|
| (0, 1]  |      1.000 |
| (1, 10] |      2.000 |
| (1, 10] |      3.000 |
| (1, 10] |      4.000 |
| (1, 10] |      5.000 |
| (1, 10] |      6.000 |
| (1, 10] |      7.000 |
| (1, 10] |      8.000 |
| (1, 10] |      9.000 |
| (1, 10] |     10.000 |


## Calculate birth weight statistics

For each of the two bins (first born and all others), calculate the mean and variance birthweight. Also determine the number of births in each of the two groups.


```python
stats = ( df[['birthord_bin', 'totalwgt_lb']]
          .groupby('birthord_bin')
          .agg(['mean','var','count'])
         )
```

Calculate the normalized counts (i.e. percent of total).


```python
stats[('totalwgt_lb','count_norm')] = ( stats[('totalwgt_lb','count')]
                                        .div(stats[('totalwgt_lb','count')].sum())
                                       )
```

View the statistics table.


```python
print(tabulate(stats,
      headers=[x[1] for x in stats.columns.tolist()],
      tablefmt='pipe',
      floatfmt=".3f")
     )
```

|         |   mean |   var |    count |   count_norm |
|:--------|-------:|------:|---------:|-------------:|
| (0, 1]  |  7.201 | 2.018 | 4363.000 |        0.483 |
| (1, 10] |  7.326 | 1.944 | 4675.000 |        0.517 |


## Calculate Cohen's d

Use the statistics table to calculate Cohen's d for birthweight for firstborn vs. all other babies.


```python
pooled_var = (stats[('totalwgt_lb','var')] * stats[('totalwgt_lb','count_norm')]).sum()

cohens_d = (stats[('totalwgt_lb','mean')].diff().dropna() / np.sqrt(pooled_var)).values[0]
print(cohens_d)

# COMPARE TO 0.029 FOR PREGNANCY LENGTH
```

    0.088672363332

