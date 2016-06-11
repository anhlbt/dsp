#!/usr/bin/env python
from __future__ import print_function

from advanced_python_cleaning import faculty, pretty_print_dict
import numpy as np


print(r"""

Q6.  Create a dictionary in the below format:

  faculty_dict = { 'Ellenberg': [\
                    ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                    ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                                ],
                   'Li': [\
                    ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                    ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                    ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                          ]
                 }


Print the first 3 key and value pairs of the dictionary:

""")

# Dictionary comprehension method
# faculty_dict = { x:y.values.tolist()
#                    for x,y in 
#                    faculty[['last_name', 'degree', 'title', 'email']]
#                    .set_index('last_name')
#                    .groupby(level=0)
#                 }

# Pandas-esque method
faculty_dict = ( faculty[['last_name', 'degree', 'title', 'email']]
                 .set_index('last_name')
                 .groupby(level=0)
                 .apply(lambda x: x
                                  .values
                                  .tolist())
                 .to_dict()
               )

print(pretty_print_dict(faculty_dict, num_items=3))




print(r"""

Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:


  professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                    ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                    ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                    ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                      ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                     }

Print the first 3 key and value pairs of the dictionary:

""")

# Dictionary comprehension method
# professor_dict = { x:y.squeeze().tolist()
#                      for x,y in 
#                      faculty[['last_name', 'first_name', 'degree', 'title', 'email']]
#                      .set_index(['first_name','last_name'])
#                      .groupby(level=[0,1])
#                   }

# Pandas-esque method
professor_dict = ( faculty[['first_name', 'last_name', 'degree', 'title', 'email']]
                   .set_index(['first_name', 'last_name'])
                   .groupby(level=[0,1])
                   .apply(lambda x: x
                                    .values
                                    .squeeze()
                                    .tolist())
                   .to_dict()                 
                  )

print(pretty_print_dict(professor_dict, num_items=3))




print(r"""

Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.

""")


last_name_sort = lambda x: x[1]

key_list = sorted(professor_dict, key=last_name_sort)

print(pretty_print_dict(professor_dict, key_list=key_list, num_items=3))



