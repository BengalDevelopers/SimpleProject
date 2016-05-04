import pandas as pd
import numpy as np
import datetime as dt
# DataFrame Simulator - Genertes X number of Dataframes and returns the dataframes in a list
class simulateXDataframe:
    
    def simulationModel(self, startDate, endDate, simulationModelSize):
        mu = 0
        sigma = 1    
        N = 8761
        i = 0
        #Variables Required to Generate Index for Simulation
        dataframelist = {};
        dynamicOnesArray = np.empty(N, dtype = int)
        #Loop Size Dictated by Simulation Array Size
        dynamicSimulationArray =[]
        dynamicSimulationArray = np.ones(simulationModelSize + 1)
        # Setting Up Date Time Index for Dataframe
        yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
        result = []
        df1 = pd.DataFrame()
        arrays = [yearHourRange]
#        df = pd.Series((y_t,dynamicOnesArray),  columns=['y_t', 'index'], index = index)
        for x in dynamicSimulationArray:
#           Normal Distribution for Dataframe
            y_t = np.random.normal(mu, sigma, len(yearHourRange))  
#           Filling Current Simulation Index
            dynamicOnesArray.fill(i)
#           Generating Variables to create Multi-index for Dataframe
            arrays = [np.array(dynamicOnesArray), yearHourRange]
            tupleslist = list(zip(*arrays))
#           Generating Multi-index for DataFrame
            index = pd.MultiIndex.from_tuples(tupleslist, names=['sim no', 'datetimeindex'])
#           Now Creating the Dataframe with the Created Multi-Index
            df = pd.DataFrame(y_t,  columns=['y_t'], index = index)
#            Appending df to a list
            result.append(df)
            i = i + 1
        df1 =  pd.concat(result)
        return df1
#    
#    def some_function(self, x, p, yearHourRange, mu, sigma):
#        y_t = np.random.normal(mu, sigma, len(yearHourRange))
#        return x    
#            