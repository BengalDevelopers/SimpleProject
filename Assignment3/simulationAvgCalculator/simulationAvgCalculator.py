import pandas as pd
import numpy as np
import datetime as dt

class simulateAvgCalc:
    
    def simulationAvgHour(self, startDate ,endDate,theSimulation, simulationModelSize, hournumber):
#Generate the Simulation
        yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
#Slicing Each Simulation by Upper Index of the Yearly Hour Number.
        hourRangeAvg = theSimulation.xs(yearHourRange[hournumber], level='datetimeindex')
        print hourRangeAvg
#Calculating Hour Range Average for Simulation
        total = np.sum(hourRangeAvg)
#        print 'Sum is ', total.values
        hourAVGHr = total/simulationModelSize
#        print 'The Average is ', hourAVG
        return hourAVGHr.values;
    
    
        