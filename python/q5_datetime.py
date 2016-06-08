#!/usr/bin/env python
from __future__ import print_function
from datetime import datetime as dt


def calc_days(date_str, date_start, date_stop):
    return (dt.strptime(date_stop, date_str) - dt.strptime(date_start, date_str)).days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_str = '%m-%d-%Y'

print('Section 5a, Question 5, Part A:')
print('Calculate the days between {} and {}:'.format(date_start, date_stop))
print(calc_days(date_str, date_start, date_stop))
print('')

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_str = '%m%d%Y'

print('Section 5a, Question 5, Part B:')
print('Calculate the days between {} and {}:'.format(date_start, date_stop))
print(calc_days(date_str, date_start, date_stop))
print('')

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_str = '%d-%b-%Y'

print('Section 5a, Question 5, Part C:')
print('Calculate the days between {} and {}:'.format(date_start, date_stop))
print(calc_days(date_str, date_start, date_stop))
print('')

