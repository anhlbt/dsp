#!/usr/bin/env python

from advanced_python_cleaning import faculty

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
""")


faculty_dict = dict([(x,y.drop('last_name', axis=1).values.tolist())
                      for x,y in 
                      faculty[['last_name', 'degree', 'title', 'email']]
                      .groupby('last_name')])

print(dict([(key, faculty_dict[key]) for key in faculty_dict.keys()[:3]]))



print(r"""
Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:


	professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
	                  ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                	  ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                 	  ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                      ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                     }
""")


professor_dict = dict([(x,y.drop(['last_name', 'first_name'], axis=1).values.tolist())
                        for x,y in 
                        faculty[['last_name', 'first_name', 'degree', 'title', 'email']]
                        .groupby(['first_name', 'last_name'])])

print(dict([(key, professor_dict[key]) for key in professor_dict.keys()[:3]]))


print('\nQ8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.\n')


last_name_sort = lambda x: x[1]

print(dict([(key, professor_dict[key]) 
            for key in sorted(professor_dict, key=last_name_sort)[:3]]))
