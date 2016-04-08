import pandas as pd
import datetime as dt
import numpy as np
from matplotlib.mathtext import List
class timeSeries:
    
#     Returns Time Series - Setup as a Controller for Future Modifications
    def getYearlyDataSeries(self,mu, sigma, startDate, endDate):

        timeSeries = self.__yearDataFrameCalcuation(startDate, endDate, mu, sigma)
        return timeSeries
        
#     Calculates timeseries and adds in Day - Weekly - Monthly Filter as Described
    def __yearDataFrameCalcuation(self, startDate, endDate, mu, sigma):
        
        yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')       
        y_t = np.random.normal(mu, sigma, len(yearHourRange))
#         Creating a dataframe with a length of number of hours in a year to map hour date range index
        ts = pd.DataFrame(y_t,  columns=['y_t'],index=yearHourRange)        
#         Creating Data Filters - Day - Week - Month   
        ts['Day'] = ts.index.dayofyear
        ts['Week No'] = ts.index.weekofyear
        ts['Month No'] = ts.index.month
        return ts
        