#!/usr/bin/env python

import pandas as pd
import re

strip_sp = lambda x: x.strip()

# Add period whenever next character is a capital or a space
clean_degrees = lambda x: re.sub(r"""(\w+?)(?=[ A-Z])""", r'\1.', x+' ').strip()

# Import the data and strip unused spaces
faculty = pd.read_csv('faculty.csv',
                      names=['name', 'degree', 'title', 'email'],
                      skiprows=[0],
                      converters = {'name' : strip_sp, 'degree' : clean_degrees,
                                    'title': strip_sp, 'email'  : strip_sp})

# Add missing degree
faculty.loc[faculty['name'] == 'Russell Takeshi Shinohara', 'degree'] = 'Ph.D.'

# Remove department name from title
faculty['title'] = faculty['title'].str.extract(r"""((?:(?:Assistant|Associate) )?Professor)""", expand=True)

# Determine email domain
faculty['email_domain'] = faculty.email.str.extract(r"""@(.+)""", expand=True)

# Extract first and last name:
# 1. Skip first initial if only listed as single letter
# 2. Also skip any nicknames in parenthesis
faculty[['first_name','last_name']] = ( faculty['name'].str
                                        .extract(r"""(?:[A-Z]\. )?(.+?)(?: \(?([\w.]+)\)?)? (.+)""", 
                                                 expand=True)
                                        .fillna('')
                                        [[0,2]]
                                       )