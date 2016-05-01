import pandas as pd
import numpy as np
# DataFrame Simulator - Genertes X number of Dataframes and returns the dataframes in a list
class simulateXDataframe:
    
    def simulationModel(self, simulationModelSize, yearHourRange, mu, sigma):
        dynamicOnesArray = np.ones(simulationModelSize)
        dataframelist = {};
        i = 0;
        from timeSeriesModule.timeSeries import timeSeries
        ts = timeSeries()
#        Need to Replace with Vectorized Solution. Could not find any alternatives to For loop.
        for x in dynamicOnesArray:
            dataframelist[i] = ts.getYearlyDataSeries(yearHourRange, mu, sigma)
            i=i+1
        return dataframelist

