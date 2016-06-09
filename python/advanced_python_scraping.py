#!/usr/bin/env python

import pandas as pd
import warnings
import requests
from bs4 import BeautifulSoup as bs

# Misc parsers needed by beautifulsoup and pandas at run-time
# These don't explicitly need to be imported
# but they're a good test for the try loop
# that's used to determine if this function is used
import lxml
import html5lib



def get_faculty_info(theURL='http://www.med.upenn.edu/cceb/biostat/faculty.shtml'):
    # A function to scrape the UPenn faculty web page and return a pandas dataframe

    # Scrape the HTML
    session = requests.Session()
    theHTML = session.get(theURL)

    # The faculty tables we want are in an iframe
    soup = bs(theHTML.text, 'lxml')
    iframes = [x.get('src') for x in soup.findAll('iframe')]

    # Grab data for all iframes and combine into a dataframe
    faculty_table = ( pd.concat( [ pd.read_html(x, header=0)[0]
                                   for x in iframes ] )
                      .reset_index(drop=True)
                    )

    return faculty_table



def get_degree(faculty_name, faculty_table):
    # A function to return the degree for a specified name
    # Tries to use permissive name matching, although this could be improved

    # Extract the location of the dsired degree from the table
    mask = faculty_table.Name.str.contains(faculty_name)


    if sum(mask) == 0:
        warnings.warn('Warning: No matches were found, returning empty string.')
        return ''


    if sum(mask) > 1:
        warnings.warn('Warning: More than one name match was found, returning first match.')

        
    degree = ( faculty_table.Name.loc[mask]
               .str
               .extract(r""".+\s*,\s*(.+)\s*""", 
                        expand=False)
               .values[0]
             )

    return degree

