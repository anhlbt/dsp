#!/usr/bin/env python

import pandas as pd
import warnings
import requests
from bs4 import BeautifulSoup as bs

# Misc parsers needed by beautifulsoup and pandas
# These don't explicitly need to be imported
# but they're a good test for the try loop
# that's used to determine if this function is used
import lxml
import html5lib

# A function to scrape the UPenn faculty web page for missing degrees

def get_degree(name):

    # Scrape the HTML
    session = requests.Session()
    theURL = 'http://www.med.upenn.edu/cceb/biostat/faculty.shtml'
    theHTML = session.get(theURL)

    # The faculty tables we want are in an iframe
    soup = bs(theHTML.text, 'lxml')
    iframes = [x.get('src') for x in soup.findAll('iframe')]

    # Grab data for all iframes and combine into a dataframe
    table = ( pd.concat( [ pd.read_html(x, header=0)[0]
                           for x in iframes ] )
              .reset_index(drop=True)
            )

    # Extract the degree from the table
    mask = table.Name.str.contains(name)

    if sum(mask) > 1:
        warnings.warn('Warning: More than one name match was found, returning first match.')

    degree = ( table.Name.loc[mask]
               .str
               .extract(r""".+\s*,\s*(.+)\s*""", 
                        expand=False)
               .values[0]
             )

    return degree
