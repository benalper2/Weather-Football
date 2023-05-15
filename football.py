import pandas as pd

# Specify the path to your .dat file
file_path = 'football.dat'

# Use pandas' read_csv() function to read the file
#Pythin engine used because of regex
Football_PremierLeague_2001_2 = pd.read_csv(file_path, sep=r'(?:\s+|\-)+', engine='python')

class Football:
    def __init__(self, data):
        self.data = data

        #Prints the name of the team that had the smallest difference between goals scored for and against them
    def SmallestGoalDiff(self):
        forColumn = self.data['F']
        againstColumn = self.data['A']
        diffColumn = abs(forColumn - againstColumn)
        print('The team with the smallest difference between goals scored for and against them was:')
        row = diffColumn.idxmin()
        print(self.data.loc[row, 'Team'])

f1 = Football(Football_PremierLeague_2001_2)
f1.SmallestGoalDiff()