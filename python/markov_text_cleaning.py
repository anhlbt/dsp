#!/usr/bin/env python

import re
import string
import numpy as np
from glob import glob1
# from ast import literal_eval

from markov_text_contractions import contractions
from markov_text_download import transcript_directory

# output_directory = 'markov_input'


sentence_characters = '.?!,;-'
non_sentence_characters = '"#$%&\'()*+-/:<=>@[\\]^_`{|}~'

sentence_regex = re.compile('([{}]+)'.format(re.escape(sentence_characters)))
non_sentence_regex = re.compile('[{}]'.format(re.escape(non_sentence_characters)))



### ACCESSORY FUNCTIONS ###

def spaceout_sentence_punctuation(text_string, sentence_regex=sentence_regex):
    # Add space before and after sentence punctuation so it can be tokenized
    return re.sub(r"""([\.!\?])""", r' \1 ', text_string)


def split_string_into_array(text_string):
    # Split cleaned text string into an array
    return np.array(re.split(r"""\s+""", text_string))



### PRIMARY CLEANING FUNCTIONS ###

def import_text_from_files(transcript_directory=transcript_directory):
    # RETURNS: an uncleanted text string of Trump's debate transcript text

    # Generate a list of all debate transcripts
    filelist = glob1(transcript_directory, '*.txt')

    sound_effects_regex = re.compile(r"""(\[[a-z ]+\]|\(APPLAUSE\))""")
    key_regex = re.compile(r"""\[?[A-Z \']+\]?\s*?:""")

    # Iterate through all the text files, read them, and split out Trump's text
    text_string = ''

    for filename in filelist:
        filestring = '{}/{}'.format(transcript_directory, filename)
        
        with open(filestring, 'r') as fh:
            transcript_text = ' ' + fh.read() + ' '
            
        # Remove audience sound effects (booing, cheering, etc.)
        transcript_text = re.sub(sound_effects_regex, '', transcript_text)
        # transcript_text = re.sub(r"""\(APPLAUSE\)""", '', transcript_text)
        
        # Get the keys and the text they correspond to
        keys = map(lambda x: re.sub(r"""[ \[\]:]+""", '', x), re.findall(key_regex, transcript_text))
        split_text = re.split(key_regex, transcript_text)[1:]
        
        # Ensure the number of keys match the number of text snippets
        assert len(keys) == len(split_text)
        
        # Get just Donald Trump's text
        text_list = filter(lambda x: 'TRUMP' in x[0], zip(keys, split_text))
        
        # Join onto existing text
        text_string += ' '.join(map(lambda x: x[1], text_list)) + ' '

    return text_string


def clean_text(text_string):
    # RETURNS: a cleaned string of text data, with sentence punctuation in-tact

    # Convert to lower case and clean begginning/end of string
    text_string = text_string.lower()

    # Convert contractions
    for key in contractions.keys():
        text_string = text_string.replace(key, contractions[key])

    # # Strip long period/parentheticals before parsing into sentences
    text_string = re.sub(r"""(\.){2,}""", '\1', text_string)
    text_string = re.sub(r"""(-){2,}""", '\1', text_string)

    # Strip unwanted punctuation
    text_string = re.sub(non_sentence_regex, '', text_string)

    # Add spaces before/after punctuation that will be retained.
    text_string = spaceout_sentence_punctuation(text_string)

    # Strip numbers
    text_string = re.sub(r"""[0-9]+""", '', text_string)

    # Strip extra spaces
    text_string = re.sub(r"""\s+""", ' ', text_string, flags=re.MULTILINE).strip()

    # Capitalize "I"
    text_string = re.sub(r""" i """, ' I ', text_string)

    return text_string