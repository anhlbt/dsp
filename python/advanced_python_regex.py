#!/usr/bin/env python
from __future__ import print_function

import pandas as pd
from advanced_python_cleaning import faculty, pretty_print_list

try:
    # Print the tables with markdown syntax if possible
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

degrees = ( degrees
            .value_counts()
            .to_frame()
            .rename(columns={0:'count'})
          )

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

num_unique_titles = faculty.title.nunique()

faculty_titles = ( faculty
                   .title
                   .value_counts()
                   .to_frame()
                   .rename(columns={'title':'count'})
                 )

print('>> There are {} different faculty titles.\n'.format(num_unique_titles))

if use_tabulate:
    title_table = tabulate(faculty_titles, 
                           headers=faculty_titles.columns,
                           tablefmt='pipe')
else:
    title_table = faculty_titles

print('>> {}\n'.format(title_table))



### Q3. Search for email addresses and put them in a list. Print the list of email addresses.

print('\nQ3. Search for email addresses and put them in a list. Print the list of email addresses.\n')

email_list_str = pretty_print_list(faculty.email.tolist())

print('>> {}\n'.format(email_list_str))



### Q4. Find how many different email domains there are.  Print the list of unique email domains.

print('\nQ4. Find how many different email domains there are.  Print the list of unique email domains.\n')

num_unique_domains = faculty.email_domain.nunique()

unique_domains_str = pretty_print_list(faculty.email_domain.unique())

print('>> There are {} different email domains.\n'.format(num_unique_domains))

print('>> {}\n'.format(unique_domains_str))

