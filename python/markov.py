#!/usr/bin/env python
from __future__ import print_function

import re
import sys
import os
import numpy as np
import pandas as pd
from scipy.stats import rv_discrete

from markov_table_creation import create_first_word_table, \
                                  create_ngram_table, \
                                  skip_punctuation


class MarkovTextGenerator(object):
    # Generates Markov text from a cleaned input text file

    # The design of the model is discussed in detail in the
    # markdown file for this assignment.
        
    def __init__(self, num_words, ngram_len=4):
        # Initialize the class with number of words
        # and length of ngrams to create
        
        self.num_words = num_words
        self.ngram_len = ngram_len
        
        
    def generate_ngrams(self, seed_text_filename):
        # Generate to pandas Series--one with the
        # probabilities of all the first words
        # of sentences and a second with the probabilities
        # of all unique n-grams.
        
        # Can use weighted or unweighted probabilities
        # but I decided to fix it to weighted
        use_frequencies = False
        
        text_array = read_corpus_file(seed_text_filename)
        
        self.ngrams = create_ngram_table(text_array, 
                                         self.ngram_len, 
                                         use_frequencies)
        self.first_words = create_first_word_table(text_array)
        
        return
    

    def generate_markov_text(self):
        
        markov_text_list = generate_markov_text_list(self.ngrams, 
                                                     self.first_words, 
                                                     self.num_words)

        self.markov_text = clean_markov_text(markov_text_list)
        
        return
        



def read_corpus_file(text_file):
    # RETURNS: a pandas Series based on the tokenized contents
    #          of the text file
    
    # TODO: Make this work better with large corpuses by
    #       converting to a generator that either:
    # 1. Reads data by lines (adding line breaks to my text data)
    # 2. Reads data from the file in chunks
    
    with open(text_file, 'r') as fh:
        text_string = fh.read()
        
    text_array = np.array(re.split(r"""\s+""", text_string))
    
    return text_array



def weighted_random_choice(distribution):
    # RETURNS: a sample from a weighted discrete distribution
    # For scipy's rv_discrete, the words need to be separated and
    # a numerical range needs to be inserted in their place
    
    if distribution.shape[0] == 1:
        # Handle the simple case of only one set of words
        random_words = distribution.index[0]
        
    else:
        
        if isinstance(distribution, pd.DataFrame):
            words = distribution.index
            numerical_dist = np.array([ np.arange(distribution.shape[0]), 
                                        distribution.squeeze().values ])

        # Create the discrete distribution
        my_distribution = rv_discrete(values=numerical_dist)

        # Sample from the distribution
        pos = my_distribution.rvs(size=1)
        
        random_words = words[pos][0]
    
    return random_words



def get_last_word(word_list, skip_punctuation=skip_punctuation):
    # RETURNS: the last word in the word list that is not punctuation
    # Probably will be one of the two last words, but this
    # will handle cases where there are multiple adjacent 
    # punctuation symbols. 
    
    # TODO: the first word of my cleaned text should
    # not to be punctuation but an error message would
    # be good to add
    
    pos = -1

    while True:
        last_word = word_list[pos]
        pos -= 1

        if not(last_word in skip_punctuation):
            break

    return last_word   



def generate_markov_text_list(ngram_markov, first_words, num_words, skip_punctuation=skip_punctuation):
    # RETURNS: a list of Markov text as long as (or slightly longer than)
    #          the specified number of words. Though punctuation was
    #          tokenized, it is not counted in the word length
    
    word_list = [weighted_random_choice(first_words)]
    len_word_list = 1

    while (len_word_list <= num_words):

        last_word = get_last_word(word_list)

        next_words = weighted_random_choice(ngram_markov.loc[last_word])

        word_list += list(next_words)

        len_word_list = sum(map(lambda x: x not in skip_punctuation, word_list))
        
    return word_list



def clean_markov_text(markov_text_list):
    # RETURNS: a cleaned string of Markov text

    markov_text = ' '.join(markov_text_list)

    # Replace adjacent punctuation marks with the first punctuation mark and clean spaces
    markov_text = re.sub(r'(( [!,;:\.\?]| --){2,})', lambda x: x.group(2), markov_text)
    markov_text = re.sub(r' ([!,;:\.\?])', lambda x: x.group(1), markov_text)
    markov_text = re.sub(r"""\s+""", ' ', markov_text)

    # Fix capitalization
    markov_text = re.sub(r"""([\.\?!] )(\w)""", 
                 lambda x: r"""{}{}""".format(x.group(1), x.group(2).capitalize()), markov_text)
    markov_text = markov_text[0].upper() + markov_text[1:]
    
    return markov_text



if __name__ == '__main__':
    
    # Create help message and check input arguments
    program_name = os.path.split(sys.argv[0])[-1]
    help_message = '\nUsage: {} {} {} [{}]\n'.format(program_name, 'input_text_file.txt', 
                                             'words_to_generate', 'ngram_size (default=4)')
    
    if (len(sys.argv) < 3) | (len(sys.argv) > 4):
        print(help_message)
        sys.exit(1)
        

    # Parse command line options

    if not os.path.exists(sys.argv[1]):
        print('\nThe file {} does not exist.\n'.format(sys.argv[1]))
        sys.exit(1)
    else:
        seed_text_filename = sys.argv[1]


    try:
        num_words = int(sys.argv[2])
    except:
        print('\nThe number of words to generate must be a number.\n')
        sys.exit(1)
    

    if len(sys.argv) == 4:
        try:
            ngram_len = int(sys.argv[3])
        except:
            print('\nThe n-gram length must be a number.\n')
            sys.exit(1)
    else:
        ngram_len = 4

    # Create the ngrams and print the result
    markov_generator = MarkovTextGenerator(num_words, ngram_len)

    markov_generator.generate_ngrams(seed_text_filename)
    markov_generator.generate_markov_text()

    print(markov_generator.markov_text)

