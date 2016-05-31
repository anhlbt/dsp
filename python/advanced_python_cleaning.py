#!/usr/bin/env python

import pandas as pd
import re

# Accessory printing functions

## A function to print lists in a nice format for markdown
pretty_print_list = lambda the_list: '[' + ',\n '.join(the_list) +']'


## A function to print dictionaries in a nice format for markdown
def pretty_print_dict(the_dict, num_items=3, key_list=None):

    if key_list is None:
        key_list = the_dict.keys()

    if num_items is None:
        num_items = len(key_list)

    key_list = key_list[:num_items]

    max_key_len = max([len(str(key)) for key in key_list])

    print_string = ''

    for num, key in enumerate(key_list):
        if num < num_items:

            if num == 0:
                prefix = '>> {'
            else:
                prefix = ' '

            if num == (num_items - 1):
                suffix = '}'
            else:
                suffix = ',\n'

            print_string += '{}{} : {}{}'.format(prefix, str(key).ljust(max_key_len), the_dict[key], suffix)

        else:
            break

    return print_string


# Data import and cleaning

## Remove spaces from the ends of entries
strip_sp = lambda x: x.strip()


## Add period whenever next character is a capital or a space
clean_degrees = lambda x: re.sub(r"""(\w+?)(?=[ A-Z])""", r'\1.', x+' ').strip()


## Import the data and strip unused spaces
faculty = pd.read_csv('faculty.csv',
                      names=['name', 'degree', 'title', 'email'],
                      skiprows=[0],
                      converters = {'name' : strip_sp, 'degree' : clean_degrees,
                                    'title': strip_sp, 'email'  : strip_sp})


## Add missing degree
faculty.loc[faculty['name'] == 'Russell Takeshi Shinohara', 'degree'] = 'Ph.D.'


## Remove department name from title
faculty['title'] = faculty['title'].str.extract(r"""((?:(?:Assistant|Associate) )?Professor)""", expand=True)


## Determine email domain
faculty['email_domain'] = faculty.email.str.extract(r"""@(.+)""", expand=True)


## Extract first and last name:
## 1. Skip first initial if only listed as single letter
## 2. Also skip any nicknames in parenthesis
faculty[['first_name','last_name']] = ( faculty['name'].str
                                        .extract(r"""(?:[A-Z]\. )?(.+?)(?: \(?([\w.]+)\)?)? (.+)""", 
                                                 expand=True)
                                        .fillna('')
                                        [[0,2]]
                                       )