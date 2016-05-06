import pandas as pd
import numpy as np
import datetime as dt

class simulateAvgCalc:

#Calculate Hourly Average
    def simulationAvgHour(self, startDate ,endDate,theSimulation, simulationModelSize, hour):
        ##Generate the Simulation
        yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
##Cross Section of Simulation displaying only the hour choosen by the user 
        z = len(yearHourRange)
        if(hour <= z):
            hourRangeAvg = theSimulation.xs(yearHourRange[hour], level='datetimeindex')
    ##        print hourRangeAvg
    ##Calculating Hour Range Average for Simulation
            hourResults = hourRangeAvg['y_t'].values
    #        print hourResults
            total = np.sum(hourResults)
    ##        print 'Sum is ', total.values
            hourAVG = (total/simulationModelSize)
    #        print 'The Average is ', hourAVG.values
        else:
            hourAVG = None
        return hourAVG;



#Calculate Daily Average
    def simulationAvgDay(self, startDate, endDate, theSimulation, simulationModelSize, day):
        theSimulation = theSimulation.copy()
        index = 'Day';
# Dropping Upper Index of Simulation
        theSimulation.index = theSimulation.index.droplevel(0)
# Adding Day Index as a column for Slicing
        theSimulation[index] = theSimulation.index.dayofyear
# Now slicing Dataframe for the Given Day
        z = theSimulation.index.dayofyear
# Checking if the input Day Provided is a Valid Day within the Simulated DataFrame
        if(day <= np.max(z)):
            dayAVG = self.__calculateAverageCommon(index, day, theSimulation, simulationModelSize) 
        else:
            dayAVG = None
        return dayAVG



#Calculate Weekly Average
    def simulationAvgWeek(self, startDate ,endDate, theSimulation, simulationModelSize, week):
        index = 'Week';
        theSimulation = theSimulation.copy()
# Dropping Upper Index of Simulation
        theSimulation.index = theSimulation.index.droplevel(0)
# Adding Day Index as a column for Slicing
        theSimulation[index] = theSimulation.index.weekofyear
        z = theSimulation.index.weekofyear
#        print z
# Checking if the input Week Provided is a Valid Week within the Simulated DataFrame
        if(week <= np.max(z)):
            weekAVG = self.__calculateAverageCommon(index, week, theSimulation, simulationModelSize) 
        else:
            weekAVG = None
        return weekAVG
    
#Calculate Monthly Average
    def simulationAvgMonth(self, startDate ,endDate, theSimulation, simulationModelSize, month):
        theSimulation = theSimulation.copy()
        index = 'Month'
# Dropping Upper Index of Simulation
        theSimulation.index = theSimulation.index.droplevel(0)
# Adding Monthly Index as a column for Slicing
        theSimulation[index] = theSimulation.index.month
        z = theSimulation.index.month
#        print z
# Checking if the input Month Provided is a Valid Month within the Simulated DataFrame
        if(month <= np.max(z)):
            monthAVG = self.__calculateAverageCommon(index, month, theSimulation, simulationModelSize) 
        else:
            monthAVG = None
        return monthAVG
    
    
# Internal Function to calculate the Average 
    def __calculateAverageCommon(self, index, indexValue, theSimulation, simulationModelSize):
        timeIndexedresults = theSimulation.loc[theSimulation[index] == indexValue]
#        print timeIndexedresults
# Storing the Normal Distribution values of the Given Day in an array
        results = timeIndexedresults['y_t'].values
#        print results
#        print len(results)
# Suming all the results to set up data for Average Calculations
        total = np.sum(results)
#            print total
# Calculating the Day Average Results
        AVG = total/simulationModelSize
        return AVG