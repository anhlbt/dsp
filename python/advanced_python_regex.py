#!/usr/bin/env python

import pandas as pd

from advanced_python_cleaning import faculty

### Q1. Find how many different degrees there are, and their 
#       frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

print('\nQ1. Find how many different degrees there are, and their frequencies.\n')

# Split multiple degress up and flatten into series
degrees = faculty.degree.apply(lambda x: x.split(' ')).values
degrees = pd.Series(sum(degrees, []))

print(degrees.nunique())

print(degrees.value_counts())

### Q2. Find how many different titles there are, and their 
#       frequencies:  Ex:  Assistant Professor, Professor

print('\nQ2. Find how many different titles there are, and their frequencies.\n')

print(faculty.title.value_counts())

### Q3. Search for email addresses and put them in a list. Print the list of email addresses.

print('\nQ3. Search for email addresses and put them in a list. Print the list of email addresses.\n')

print(list(faculty.email))

### Q4. Find how many different email domains there are.  Print the list of unique email domains.

print('\nQ4. Find how many different email domains there are.  Print the list of unique email domains.\n')

print(faculty.email_domain.nunique())

print(faculty.email_domain.unique())

print('\n')
