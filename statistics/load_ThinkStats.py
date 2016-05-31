# coding: utf-8
import pandas as pd
import sys
import os
import re
import numpy as np

thinkstats_data = '/Volumes/Files/datascience_books/ThinkStats2/code'


def read_dct_file(dct_filename, columns=None):
    
    # Read the file and split on the linbreaks
    with open(dct_filename, 'r') as fh:
        dct_list = fh.read().split('\r\n')[1:-2]
        

    # Put the initial columns into a dataframe
    dct = pd.DataFrame([re.split(r"""\s+""", x.strip())[:3] for x in dct_list], 
                       columns=['column', 'type', 'variable'])
    
    # Map the types
    type_map = {'byt' : np.int, 
                'int' : np.int, 
                'lon' : np.int, 
                'flo' : np.float, 
                'dou' : np.float,
                'str' : np.object}
    
    dct['type'] = dct.type.apply(lambda x: type_map[x[:3]])
    

    # Determine starting and stopping column position
    dct['start'] = dct.column.str.extract(r"""_column\(([0-9]+)\)""", 
                                          expand=True).astype(np.int)
    dct['end'] = dct.start.shift(-1).fillna(0).astype(np.int)

    index_begin = 1
    dct[['start', 'end']] -= index_begin
    
    
    # Remove unused and unselect columns
    dct.drop(['column'], axis=1, inplace=True)

    # Drop additional columns
    if columns is not None:
        dct = dct.copy()[np.in1d(dct.variable, columns)]
    
    return dct



def read_dat_file(dat_file, dct):
        
    # Import the dictionary
    df = pd.read_fwf(dat_file, 
                 colspecs=dct[['start','end']].values.tolist(), 
                 names=dct.variable.values, 
                 compression='gzip')
    
    # Handle columns and formatting        
    for col in df.columns:
        try:
            df[col] = df[col].astype(dct.query('variable=="{}"'.format(col))['type'].values[0])
        except:
            pass
    
    
    return df



def load_survey_data(data_basename, columns=None, thinkstats_data=thinkstats_data):

    dct_file = os.sep.join([thinkstats_data, '{}.dct'.format(data_basename)])
    dat_file = os.sep.join([thinkstats_data, '{}.dat.gz'.format(data_basename)])

    dct = read_dct_file(dct_file, columns=columns)
    df = read_dat_file(dat_file, dct)

    return df



def load_FemPreg(drop_cols=False):

    if drop_cols:
        columns = np.array(['caseid', 'prglngth', 'outcome', 'pregordr', 
                            'birthord', 'birthwgt_lb', 'birthwgt_oz', 'agepreg', 'finalwgt'])
    else:
        columns = None


    df = load_survey_data('2002FemPreg', columns=columns)

    ## Clean up code adapted from ThinkStats' nsfg.CleanFemPreg routine ##
    # Put pregnancy age in years
    df.agepreg /= 100.0

    # birthwgt_lb contains at least one bogus value (51 lbs)
    # replace with NaN
    df.loc[df.birthwgt_lb > 20, 'birthwgt_lb'] = np.nan
    
    # replace 'not ascertained', 'refused', 'don't know' with NaN
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    
    if 'hpagelb' in df.columns:
        df.hpagelb.replace(na_vals, np.nan, inplace=True)

    if 'babysex' in df.columns:
        df.babysex.replace([7, 9], np.nan, inplace=True)
        
    if 'nbrnaliv' in df.columns:
        df.nbrnaliv.replace([9], np.nan, inplace=True)
        
    
    # birthweight is stored in two columns, lbs and oz.
    # convert to a single column in lb
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0

    return df


