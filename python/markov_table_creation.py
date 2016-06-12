#!/usr/bin/env python

# Functions in this module generate various tables 
# required by the text Markov chain generator

import pandas as pd
import re
import numpy as np

skip_punctuation = ['!', ',', '--', '.', ';', '?']


### N-GRAM CREATION TABLES ###

def create_first_word_table(text_array):
    # RETURNS: A pandas dataframe with unique words that appear as the
    # first word of a sentence and their probability

    # Determine frequency of each first word of a sentence

    text_series = pd.Series(text_array)

    # Find the word after each sentence punctuation
    mask = ( text_series
             .isin(['.', '!', '?'])
             .shift(1)
             .fillna(True)
            )

    first_words = ( text_series[mask]
                    .dropna()
                    .value_counts()
                    .to_frame()
                    .rename(columns={0:'prob'})
                   )

    # Normalize the frequency

    first_words['prob'] /= first_words.prob.sum()

    return first_words



def create_ngram_table(text_array, ngram_len, use_frequencies=True):
    # A wrapper function to generate a dataframe with n-gram probabilities
    
    # Determine the n-gram indicies
    ngram_indexes = _generate_ngram_indexes(len(text_array), ngram_len)

    # Create the dataframe of all n-grams and strip punctuation from word0
    word_cols = map(lambda x: 'word'+str(x), range(ngram_len))
    
    ngram_df = _generate_ngram_df(text_array, ngram_indexes, word_cols)
    
    ngram_df = _drop_first_word_punctuation(ngram_df, word_cols)
    
    # Calculate frequencies
    if use_frequencies:
        ngram_markov = _get_ngram_counts_weighted(ngram_df, word_cols)
    else:
        ngram_markov = _get_ngram_counts_unweighted(ngram_df, word_cols)
    
    # Calculate probabilities for the unique n-grams
    ngram_markov = _normalize_ngram_counts(ngram_markov, ngram_len, word_cols)
    
    return ngram_markov


### ACCESSORY TABLES ###
    
def _generate_ngram_indexes(len_text_array, ngram_len):
    # RETURNS: list of start/stop indices for each word
    # in the n-gram
    
    end_index = len_text_array - ngram_len + 1
    ngram_index_list = map(lambda x: (x, end_index+x), range(ngram_len))

    return ngram_index_list


def _generate_ngram_df(text_array, ngram_index_list, word_cols):
    # RETURNS: a pandas dataframe with a column (word0, word1, etc.)
    # for each word of the n-gram
    # NOTE: This dataframe contains non-unique values
    
    ngram_len = len(ngram_index_list)    

    ngram_df = pd.DataFrame(np.array( map(lambda x: text_array[x[0]:x[1]], 
                                          ngram_index_list) ).T,
                            columns=word_cols)
    
    return ngram_df


def _drop_first_word_punctuation(ngram_df, word_cols, skip_punctuation=skip_punctuation):
    # RETURNS: a pandas dataframe with the first and second n-gram word (word0, word1)
    # stripped of punctuation
    
    selected_cols = ['word0']
    #if 'word1' in word_cols:
    #    selected_cols += ['word1']

    mask = ( ngram_df[selected_cols]
             .isin(skip_punctuation)
             .pipe(np.invert)
             .all(axis=1)
            )
    
    return ngram_df[mask]


def _get_ngram_counts_weighted(ngram_df, word_cols):
    # RETURNS: a pandas dataframe with unique n-gram values as the
    # index and a column with frequency counts
    
    ngram_markov = ( ngram_df
                    .groupby(word_cols)
                    .size()
                    .to_frame()
                    .rename(columns={0:'freq'})
                   )
    
    return ngram_markov
    

def _get_ngram_counts_unweighted(ngram_df, word_cols):
    # RETURNS: a pandas dataframe with unique n-gram values set to 1
    #          i.e. every n-gram entry is weighted evenly
    
    ngram_markov = ( ngram_df
                     .drop_duplicates()
                     .assign(freq=1.0)
                     .set_index(word_cols)
                     .sort_index()
                   )
    
    return ngram_markov


def _normalize_ngram_counts(ngram_markov, ngram_len, word_cols):
    # RETURNS: a pandas dataframe with unique n-gram values as the
    # index and probabilities normalized with respect to the first word
    # of each n-gram

    # e.g. something like P(word1 | word0) or P(word1, word2, word3 | word0)

    ngram_markov['freq'] /= ( ngram_markov
                              .freq
                              .groupby(level=0)
                              .transform(sum)
                            )
    
    ngram_markov.rename(columns={'freq':'prob'}, inplace=True)
    
    return ngram_markov

