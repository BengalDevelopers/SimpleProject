class timeSeries:
#     Returns Time Series - Setup as a Controller for Future Modifications
    def getYearlyDataSeries(self, yearHourRange, mu, sigma):
        import numpy as np
        import pandas as pd
        import datetime as dt
        y_t = np.random.normal(mu, sigma, len(yearHourRange))
        timeSeries = self.yearDataFrameCalcuation(yearHourRange, y_t)
        timeSeries = self.multiIndexTimeSeries(timeSeries)
        timeSeries.index = pd.to_datetime(timeSeries.index)
        return timeSeries
        
#     Calculates timeseries and adds in Day - Weekly - Monthly Filter as Described
    def yearDataFrameCalcuation(self, yearHourRange, y_t):   
        import pandas as pd
        import datetime as dt
#       Creating a dataframe with a length of number of hours in a year to map hour date range index
        ts = pd.DataFrame(y_t,  columns=['y_t'],index=yearHourRange)  
        return ts
    
    def multiIndexTimeSeries(self, ts):
        import pandas as pd
        import datetime as dt
#       Creating Data Filters - Day - Week - Month   
        ts['Day'] = ts.index.dayofyear
        ts['Week No'] = ts.index.weekofyear
        ts['Month No'] = ts.index.month
        return ts
        

