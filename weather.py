import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your .dat file
file_path = 'weather.dat'

# Use pandas' read_csv() function to read the file
#Pythin engine used because of regex
NJ_Morristown_2002_06 = pd.read_csv(file_path, sep=r'(?:\s+|\*)+', engine='python')

class Weather:
    def __init__(self, data):
        self.data = data
    
    #Prints all days in month of data with max and min temperature
    def AllDays_MinMaxAvg(self):
        print('The Max, Min and Avg temperatures for each day are:')
        print(self.data.loc[:, ['Dy','MxT', 'MnT','AvT']])

    #Prints the day number that had the highet max temperature
    def Warmest_Day(self):
        print('The day with the maximum temperature was day:')
        row = self.data['MxT'].idxmax()
        print(self.data.loc[row, 'Dy'])

    #Prints the day number that had the lowest min temperature
    def Coolest_Day(self):
        print('The day with the maximum temperature was day:')
        #print(self.data['MxT'].max())
        row = self.data['MnT'].idxmin()
        print(self.data.loc[row, 'Dy'])

    #Prints the day number that had the smallest difference between min and max temperature
    def SmallestTempDiff_Day(self):
        minColumn = self.data['MnT']
        maxColumn = self.data['MxT']
        diffColumn = maxColumn - minColumn
        print('The day with the smallest temperature difference was day:')
        row = diffColumn.idxmin()
        print(self.data.loc[row, 'Dy'])

    #Plots the average temperature through the month
    def PlotAverageTemperature(self):
        self.data.plot(x='Dy', y='AvT', kind='line')
        plt.xlabel('Day of Month')
        plt.ylabel('Average Temp (F)')
        plt.title('Average Temperature over Month')
        #ax.set_xticks(self.data['Dy'])
        plt.show()


w1 = Weather(NJ_Morristown_2002_06)
w1.AllDays_MinMaxAvg()
w1.Warmest_Day()
w1.Coolest_Day()
w1.SmallestTempDiff_Day()
w1.PlotAverageTemperature()