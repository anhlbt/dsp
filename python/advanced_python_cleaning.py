#!/usr/bin/env python

import pandas as pd
import re


try:
    from advanced_python_scraping import get_faculty_info, get_degree

except:
    scrape_webpage = False

else:
    scrape_webpage = True


# Data import and cleaning

## Add period whenever next character is a capital or space
## using a positive lookahead assertion to determine the next character.
clean_degrees = lambda x: re.sub(r"""(\w)(?=[ A-Z])""", r'\1.', x+' ').strip()


## Import the data and strip extra spaces
faculty = pd.read_csv('faculty.csv',
                      names=['name', 'degree', 'title', 'email'],
                      skiprows=[0],
                      skipinitialspace=True,
                      converters = {'degree' : clean_degrees})


## Add missing degree

if not scrape_webpage:
    # This can be done the easy way
    Russell_Takesh_Shinohara_degree = 'Ph.D.'

else:
    # Or by scraping the UPenn faculty webpage using requests and beautifulsoup4 for fun
    faculty_table = get_faculty_info()
    Russell_Takesh_Shinohara_degree = get_degree('Russell Takeshi Shinohara', faculty_table)

    # Clean the degree name for good measure
    Russell_Takesh_Shinohara_degree = clean_degrees( Russell_Takesh_Shinohara_degree )


faculty.loc[faculty['name'] == 'Russell Takeshi Shinohara', 'degree'] = Russell_Takesh_Shinohara_degree


## Remove department name from title
faculty['title'] = faculty['title'].str.extract(r"""((?:Assistant |Associate )?Professor)""", expand=False)


## Determine email domain
faculty['email_domain'] = faculty.email.str.extract(r"""@(.+)""", expand=False)


## Extract first and last name:
## 1. Skip first initial if only listed as single letter
## 2. Also skip any nicknames in parenthesis or middle names
faculty[['first_name','last_name']] = ( faculty['name']
                                        .str
                                        .extract(r"""(?:[A-Z]\.? )?(.+?)(?: \(?([\w.]+)\)?)? (.+)""", 
                                                 expand=True)
                                        .fillna('')
                                        [[0,2]]
                                       )



############################################



# Accessory formatting functions

## A function to print lists in a nice format for markdown
pretty_print_list = lambda the_list: '[' + ',  \n '.join(the_list) +']'


## A function to print dictionaries in a nice format for markdown
def pretty_print_dict(the_dict, num_items=None, key_list=None):

    # Handle the case where a subset of the keys is printed
    if key_list is None:
        key_list = the_dict.keys()

    if num_items is not None:
        key_list = key_list[:num_items]

    # Set uniform spacing for all keys
    max_key_len = max([len(str(key)) for key in key_list])

    print_string = ''

    # Print each entry with appropriate prefix/suffix
    for num, key in enumerate(key_list):
        if num < num_items:

            if num == 0:
                prefix = '>> {'
            else:
                prefix = ' '

            if num == (num_items - 1):
                suffix = '}'
            else:
                suffix = ',  \n'

            print_string += '{}{} : {}{}'.format(prefix, str(key).ljust(max_key_len), the_dict[key], suffix)

        else:
            break

    return print_string