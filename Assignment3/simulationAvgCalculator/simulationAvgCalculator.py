import pandas as pd
import numpy as np
import datetime as dt

class simulateAvgCalc:

#Calculate Hourly Average
    def simulationAvgHour(self, startDate ,endDate,theSimulation, simulationModelSize, hournumber):
#Generate the Simulation
        yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
#Cross Section of Simulation displaying only the hour choosen by the user 
        hourRangeAvg = theSimulation.xs(yearHourRange[hournumber], level='datetimeindex')
        print hourRangeAvg
#Calculating Hour Range Average for Simulation
        total = np.sum(hourRangeAvg)
#        print 'Sum is ', total.values
        hourAVG = total/simulationModelSize
#        print 'The Average is ', hourAVG
        return hourAVG.values;



#Calculate Daily Average
    def simulationAvgDay(self, startDate ,endDate,theSimulation, simulationModelSize, day):
# Dropping Upper Index of Simulation
        theSimulation.index = theSimulation.index.droplevel(0)
# Adding Day Index as a column for Slicing
        theSimulation['Day'] = theSimulation.index.dayofyear
# Now slicing Dataframe for the Given Day
        dayTimeIndexedresults = theSimulation.loc[theSimulation['Day'] == day]
#        print dayTimeIndexedresults
# Storing the Normal Distribution values of the Given Day in an array
        dayResults = dayTimeIndexedresults['y_t'].values
#        print dayResults
# Suming all the results to set up data for Average Calculations
        total = np.sum(dayResults)
#        print total
# Calculating the Day Average Results
        dayAVG = total/simulationModelSize
#        print dayAVG
        return dayAVG





#Calculate Weekly Average
    def simulationAvgWeek(self, startDate ,endDate,theSimulation, simulationModelSize, week):
# Dropping Upper Index of Simulation
        theSimulation.index = theSimulation.index.droplevel(0)
# Adding Day Index as a column for Slicing
        theSimulation['Week'] = theSimulation.index.weekofyear
# Now slicing Dataframe for the Given Day
        weekTimeIndexedresults = theSimulation.loc[theSimulation['Week'] == week]
#        print weekTimeIndexedresults
# Storing the Normal Distribution values of the Given Day in an array
        weekResults = weekTimeIndexedresults['y_t'].values
#        print weekResults
# Suming all the results to set up data for Average Calculations
        total = np.sum(weekResults)
#        print total
# Calculating the Day Average Results
        weekAVG = total/simulationModelSize
#        print weekAVG
        return weekAVG
    
        