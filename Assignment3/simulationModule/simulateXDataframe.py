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
        dynamicOnesArray = np.empty([3,N], dtype = int)
        #Loop Size Dictated by Simulation Array Size
        dynamicSimulationArray =[]
        dynamicSimulationArray = np.ones(simulationModelSize + 1)
        # Setting Up Date Time Index for Dataframe
        yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
        result = []
        y_t = np.random.normal(mu, sigma, len(yearHourRange))  
        df1 = pd.DataFrame()
        
        for x in dynamicSimulationArray:
            y_t = np.random.normal(mu, sigma, len(yearHourRange))  
            dynamicOnesArray.fill(i)
#            print dynamicOnesArray
            df = pd.DataFrame(y_t,  columns=['y_t', 'year'], index = [dynamicOnesArray, yearHourRange])
            result.append(df)
            i = i + 1
        df1 =  pd.concat(result)
        df1.rename(columns={'': 'A'}, inplace=True) 
        print df1
        return df1
#    
#    def some_function(self, x, p, yearHourRange, mu, sigma):
#        y_t = np.random.normal(mu, sigma, len(yearHourRange))
#        return x    
#            