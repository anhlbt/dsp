#!/usr/bin/env python
from __future__ import print_function

# Download transcripts of the GOP debates from the 2016 election

import requests
from bs4 import BeautifulSoup as bs
import os
import re
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')


transcript_directory = 'markov_transcripts'


def _get_debate_dataframe(url='http://www.presidency.ucsb.edu/debates.php'):
    # Get the table of all presidential debates from
    # http://www.presidency.ucsb.edu
    
    # Scrape the HTML
    session = requests.Session()
    html = session.get(url)
    soup = bs(html.text, 'lxml')
    
    
    # Find the table-data cells with debate information
    docdate = soup.find_all('td', attrs={'class':'docdate'})
    doctext = soup.find_all('td', attrs={'class':'doctext'})

    
    # Clean and put the cells into a dataframe
    dates = map(lambda x: x.get_text().strip(), docdate)
    dates = filter(lambda x: x != '', dates)

    titles = map(lambda x: re.sub(r"""\s+""", ' ', x.get_text()).strip(), doctext)

    urls = map(lambda x: x.find('a', href=True)['href'] 
                         if hasattr(x.find('a', href=True), '__getitem__') else '', 
               doctext)

    debate_data = pd.DataFrame({'date': dates, 
                                'title': titles, 
                                'url': urls})
    
    
    # Clean up dataframe formatting and columns
    debate_data['date'] = pd.to_datetime(debate_data.date)
    debate_data['year'] = debate_data.date.apply(lambda x: x.year)

    debate_data['primary'] = ( debate_data
                               .title
                               .str
                               .extract(r"""(Democratic|Republican)""", expand=False)
                               .fillna('')
                             )
    
    return debate_data



def _get_gop_primaries(debate_data):
    # Extract just this election's GOP primary data, remove undercard debates
    
    mask = ( (debate_data.year > 2012) & 
             (debate_data.primary == 'Republican') &
             (debate_data.title.str.contains('Undercard').pipe(np.invert))
           )

    gop_primary_data = debate_data.loc[mask]
    
    return gop_primary_data



def _get_debate_text(url):
    # Get transcript of a debate based on url
    
    # Scrape the HTML
    session = requests.Session()
    html = session.get(url)
    soup = bs(html.text, 'lxml')

    # The debate text is in a span of class displaytext
    debate_text = soup.find('span', attrs={'class':'displaytext'}).text.encode('utf-8').strip()
    
    return debate_text



def _write_transcript_to_file(filename, text, directory=transcript_directory):
    # Write the text of a debate transcript to a file
    
    if not os.path.exists(directory):
        os.mkdir(directory)
        
    # Save a string to a file
    
    filepath = '{}/{}'.format(directory,filename)
    with open(filepath, 'w') as fh:
        fh.write(text)
        
    return



def download_debate_data():
    # Wrapper function to determine urls for debate transcripts and download all to a file

    print('Scraping data...')

    # Get the dataframe of GOP debates from this year
    debate_data = _get_debate_dataframe()
    gop_primary_data = _get_gop_primaries(debate_data)


    # Create a filename to save the transcript text to
    gop_primary_data['filename'] = gop_primary_data.date.dt.strftime('%Y_%m_%d') + '_gop_debate.txt'


    # Scrape the corresponding URL for the transcript
    gop_primary_data['transcript'] = gop_primary_data.url.apply(lambda x: _get_debate_text(x))

    print('Writing data...')

    # Write the transcripts to files
    _ = gop_primary_data.apply(lambda x: _write_transcript_to_file(x.filename, x.transcript), axis=1)

    print('...Done.')

    return

