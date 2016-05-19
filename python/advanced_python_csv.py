#!/usr/bin/env python

import os
from advanced_python_cleaning import faculty

faculty.email.to_csv('../emails.csv', header=False, index=False)

print('\nQ5. Write email addresses from Part I to csv file.\n')

print('\nFirst ten lines of the email.csv file:\n')

os.system('head ../emails.csv')

