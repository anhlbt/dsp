#!/usr/bin/env python
from __future__ import print_function

from inspect import getmembers, isfunction
import re


# Script to check that the outputs of my functions produce
# results that are identical to the docstrings provided in the function.

import q6_strings as q6
import q7_lists as q7

test_mod_dict = {'q6':q6, 'q7':q7}


for mod_name, mod in test_mod_dict.iteritems():

    # Get a list of all functions defined in the module
    func_list = [func for name, func in getmembers(mod) if isfunction(func)]

    for func in func_list:

        # Scrape the tests and answers for each function from the function's docstring
        test_answer_list = re.findall(r""">>>\s*(.+)\s*\n\s*(.+)\s*""", func.__doc__)
        
        # Evaluate each test to ensure it produces the correct answer
        # otherwise print an error message
        for test, answer in test_answer_list:

            test_command = '.'.join([mod_name, test])

            eval_test = eval(test_command)

            eval_answer = eval(answer)

            try:
                assert eval_test == eval_answer

            except AssertionError as aerror:

                aerror.args += (' '.join([test_command, ' != ', answer]),)
                raise

            else:

                print('Passed: {}:'.format(test_command))
                print('        {} == {}'.format(eval_test, eval_answer))
                print('')

print('All functions passed.')
