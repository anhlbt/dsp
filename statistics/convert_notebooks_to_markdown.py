#!/usr/bin/env python

# Convert all Jupyter notebooks to markdown files
import nbconvert
import os
import re
import sys


# Base file names of the files to convert

file_list = ['2-4-cohens_d', 
             '3-1-actual_biased', 
             '4-2-random_dist', 
             '5-1-blue_men',
             '6-1-household_income', 
             '7-1-weight_vs_age',
             '8-2-sampling_dist',
             '8-3-scoring',
             '9-2-resampling']


# Read the data, clean it, and write it

for fil in file_list:

    nb_file = '{}.ipynb'.format(fil)

    md_file = '{}.md'.format(fil)
    
    if os.path.exists(nb_file):

        print('Found notebook \'{}\'...'.format(nb_file))
        
        # Read the notebook and resources
        md_str, md_res = nbconvert.export_markdown(nb_file)

        if sys.version_info[0] == 2:
            md_str = md_str.encode('utf8')

        # Get the base64 encoded images
        md_figs = md_res['outputs']

        # Strip spaces before any output markdown tables
        md_str = re.sub(r"""(?<=\n)    \|""", '|', md_str)

        # Add directory and remove 'png' label from figure references
        if len(md_figs.keys()) > 0:

            if not os.path.exists(fil):
                os.mkdir(fil)

            md_str = re.sub(r"""\[png\]\(""", r'[]({}/'.format(fil), md_str)

            print('     Writing images to directory \'{}\''.format(fil))
            
            # Write the figures
            for key in md_figs.keys():
                with open('{}/{}'.format(fil, key), 'wb') as fh:
                    fh.write(md_figs[key])


        # Write the markdown file
        print('     Writing markdown file \'{}\''.format(md_file))

        with open(md_file, 'w') as fh:
            fh.write(md_str)

        print('     Done.\n')

