#!/usr/bin/env python
# The football.csv file contains the results from the English Premier League. 
# The columns labeled 'Goals' and 'Goals Allowed' contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in 'for' and 'against' goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.



# The first answer uses the csv library and a class, since the provided functions mentioned 'self'
# To execute this answer, import the class:
# >>> from q8_parsing import football_parser
# >>> fb = football_parser('football.csv')

# The above will automatically print the answer. Alternatively: 
# >>> print('The team with the minimum difference between goals for and against is {}.'.format(fb.minteam))

import csv
import numpy as np

class football_parser(object):

    def __init__(self, filepath=None):
        self.teams = None
        self.goals = None
        self.minpos = None
        self.minteam = None

        if filepath is not None:
            self.read_data(filepath)
            self.get_team()

        return


    def read_data(self, filepath):
        
        goals = list()
        teams = list()

        with open(filepath, 'r') as fh:
            csv_data = csv.reader(fh, delimiter=',')
            for row in csv_data:
                if row[0] != 'Team':
                    teams.append(row[0])
                    goals.append([int(row[5]), int(row[6])])

        self.teams = teams
        self.goals = np.array(goals)

        return


    def get_team(self):

        self.minpos = np.argmin( np.abs( self.goals[:,0] - self.goals[:,1] ) )
        self.minteam = self.teams[self.minpos]

        print('Class Method: The team with the minimum difference between goals for and against is {}.'.format(self.minteam))

        return



# Here is a second answer that uses Pandas
# To execute this answer, run this script from the command line: 
# >>> ./q8_parsing

if __name__ == '__main__':

    import pandas as pd

    data = pd.read_csv('football.csv', sep=',', usecols=[0,5,6], skiprows=[0],
                        names=['team','goals','goals_against'])

    minpos = (data.goals - data.goals_against).abs().argmin()
    minteam = data.iloc[minpos]['team']

    print('Pandas Method: The team with the minimum difference between goals for and against is {}.'.format(minteam))

