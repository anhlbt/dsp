#!/usr/bin/env python

# A sampler for discrete, weighted distributions that is compatible 
# with text values

# Based on the class scipy.stats.rv_discrete
# http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.stats.rv_discrete.html


from scipy.stats import rv_discrete
import numpy as np
import pandas as pd


class rv_discrete_text(rv_discrete):
    
    def __init__(self, *args, **kwargs):
        
        # Update kwargs with any missing defaults since we want to use a
        # simplified function call with args/kwargs
        
        # Defaults from https://github.com/scipy/scipy/blob/v0.17.0/scipy/stats/_distn_infrastructure.py#L2641

        default_dict = dict(a=0, b=np.inf, name=None, badvalue=None,
                            moment_tol=1e-8, values=None, inc=1, longname=None,
                            shapes=None, extradoc=None, seed=None)

        default_keys = ['a', 'b', 'name', 'badvalue', 'moment_tol', 
                        'values', 'inc', 'longname', 'shapes', 
                        'extradoc', 'seed']

        # Remove any default keys that have been provided as args
        for pos in range(len(args)):
            del default_dict[default_keys[pos]]

        # And then update the dictionary
        for key in default_dict.keys():
            kwargs.setdefault(key, default_dict[key])


        
        # Setup distribution inputs so they are numeric, as required by rv_discrete
        if kwargs['values'] is not None:
            tmp_values = kwargs['values']

            # Handle dataframes and series
            if isinstance(tmp_values, pd.DataFrame):
                tmp_values = tmp_values.values.T
            elif isinstance(tmp_values, pd.Series):
                tmp_values = tmp_values.reset_index().values.T

            
            # Fix other dimensionality (if unambiguous)
            if ((tmp_values.shape[1] == 2) & (tmp_values.shape[0] != 2)):
                tmp_values = tmp_values.T

                
            # Determine if words were provided
            try:
                _ = tmp_values[0].astype(np.float)
            except:
                save_words = True
            else:
                save_words = False
                

            if save_words:
                # Preserve the words in the 'wk' attribute
                self.wk = tmp_values[0].copy()

                # Convert the words column to a numerical range
                tmp_values[0] = np.arange(tmp_values.shape[1])

            # update the values with numeric and dimensionality
            # corrected version of distribution
            kwargs['values'] = tmp_values

            
        # Finish setting up the distribution
        super(rv_discrete_text, self).__init__(*args, **kwargs)


    def rvs(self, *args, **kwargs):
        
        # Get the array of numerical samples
        numerical_samples = super(rv_discrete_text, self).rvs(*args, **kwargs)

        # Convert to word/text values if appropriate
        if hasattr(self, 'wk'):
            samples = np.array([self.wk[x] for x in numerical_samples])
        else:
            samples = numerical_samples
        
        return samples

