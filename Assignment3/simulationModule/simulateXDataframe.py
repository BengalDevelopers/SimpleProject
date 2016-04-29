import pandas as pd
import numpy as np
# DataFrame Simulator - Genertes X number of Dataframes and returns the dataframes in a list
class simulateXDataframe:
    
    def simulationModel(self, simulationModelSize, calculateTimeSeries):
        dynamicOnesArray = np.ones(simulationModelSize)
        dataframelist = {};
        i = 0;
        #Need to Replace with Vectorized Solution. Could not find any alternatives to For loop.
        for x in dynamicOnesArray:
            dataframelist[i] = calculateTimeSeries()
            i=i+1
        return dataframelist
    
