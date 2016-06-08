#!/usr/bin/env python
from __future__ import print_function

from advanced_python_cleaning import faculty, pretty_print_list

csv_file_name = 'emails.csv'

faculty.email.to_csv(csv_file_name, header=False, index=False)


print('\nQ5. Write email addresses from Part I to csv file.\n')

print('>> The first ten lines of the email.csv file are:\n')

with open(csv_file_name, 'r') as fh:
	the_list = [x.strip() for x in fh.readlines()[:10]]
	
print('>> {}\n'.format(pretty_print_list(the_list)))


