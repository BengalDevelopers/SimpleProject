
import datetime as dt
import pandas as pd
class timeSeries:
    
#     Returns Time Series - Setup as a Controller for Future Modifications
    def getYearlyDataSeries(self,y_t, yearHourRange):
        timeSeries = self.__yearDataFrameCalcuation(yearHourRange, y_t)
        return timeSeries
        
#     Calculates timeseries and adds in Day - Weekly - Monthly Filter as Described
    def __yearDataFrameCalcuation(self, yearHourRange, y_t):

#         Creating a dataframe with a length of number of hours in a year to map hour date range index
        ts = pd.DataFrame(y_t,  columns=['y_t'],index=yearHourRange)        
#         Creating Data Filters - Day - Week - Month   
        ts['Day'] = ts.index.dayofyear
        ts['Week No'] = ts.index.weekofyear
        ts['Month No'] = ts.index.month
        return ts

