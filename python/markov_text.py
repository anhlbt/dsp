#!/usr/bin/env python
import markov_text_download as mtxtdown

import markov_text_cleaning as mtxtclean


# Download the transcript data if necessary
# Set download_data to False to prevent
# constant pinging of website
download_data = False

if download_data:
    mtxtdown.download_debate_data()
    
trump_text = mtxtclean.import_text_from_files()

trump_text = mtxtclean.clean_text(trump_text)

with open('markov_trump_gop_debate_transcripts.txt', 'w') as fh:
    fh.write(trump_text)

print trump_text
