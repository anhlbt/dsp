#!/usr/bin/env python

import pandas as pd
from advanced_python_cleaning import faculty, pretty_print_list

try:
    from tabulate import tabulate
except:
    use_tabulate = False
else:
    use_tabulate = True


### Q1. Find how many different degrees there are, and their 
#       frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

print('\nQ1. Find how many different degrees there are, and their frequencies.\n')

# Split multiple degress up and flatten into series
degrees = faculty.degree.apply(lambda x: x.split(' ')).values
degrees = pd.Series(sum(degrees, []))

print('>> There are {} different degrees.\n'.format(degrees.nunique()))

degrees = degrees.value_counts().to_frame().rename(columns={0:'count'})

if use_tabulate:
    degree_table = tabulate(degrees, 
                            headers=degrees.columns,
                            tablefmt='pipe')
else:
    degree_table = degrees

print('>> {}\n'.format(degree_table))



### Q2. Find how many different titles there are, and their 
#       frequencies:  Ex:  Assistant Professor, Professor

print('\nQ2. Find how many different titles there are, and their frequencies.\n')

faculty_titles = faculty.title.value_counts()
faculty_titles = faculty_titles.to_frame().rename(columns={0:'count'})

print('>> There are {} different faculty titles.\n'.format(faculty.title.nunique()))

if use_tabulate:
    title_table = tabulate(faculty_titles, 
                           headers=faculty_titles.columns,
                           tablefmt='pipe')
else:
    title_table = faculty_titles

print('>> {}\n'.format(title_table))



### Q3. Search for email addresses and put them in a list. Print the list of email addresses.

print('\nQ3. Search for email addresses and put them in a list. Print the list of email addresses.\n')

print('>> {}\n'.format(pretty_print_list(list(faculty.email))))



### Q4. Find how many different email domains there are.  Print the list of unique email domains.

print('\nQ4. Find how many different email domains there are.  Print the list of unique email domains.\n')

print('>> There are {} different email domains.\n'.format(faculty.email_domain.nunique()))

print('>> {}\n'.format(pretty_print_list(faculty.email_domain.unique())))

