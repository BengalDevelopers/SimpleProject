import pandas as pd
import datetime as dt
class timeAverageCalc:
    
    def dailyAverage(self, YearlytimeSeries, startDate, endDate):

        dailyAvg = YearlytimeSeries.groupby(['Day'])['y_t'].mean()
        print('The Daily Average of the Following Time Series is')
        print(dailyAvg)
        return dailyAvg
    
    def weeklyAverage(self, YearlytimeSeries, startDate, endDate):
        weeklyAvg = YearlytimeSeries.groupby(['Week No'])['y_t'].mean()
        print('The Weekly Average of the Following Time Series is')
        print(weeklyAvg)
        return weeklyAvg

    def monthlyAverage(self, YearlytimeSeries, startDate, endDate):
        monthlyAvg = YearlytimeSeries.groupby(['Month No'])['y_t'].mean()
        print('The Monthyl Average of the Following Time Series is')
        print(monthlyAvg)
        return monthlyAvg