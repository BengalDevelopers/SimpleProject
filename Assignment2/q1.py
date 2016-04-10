import numpy as np

#Class to generate mean
from callOptionModule.callOption import callOption
from iniparse.config import Undefined

#########Global Variables#############
# Setting mean(mu) 0, standard deviation(sigma) 1
mu, sigma = 0, 1 

# Generating 100 random numbers  with mean and standard deviation as 0, 1 respectively.
S = np.random.normal(mu, sigma, 100); 

#Defining Strike Value k
K = 0.5
ts = 0

# 	Setting Start Date and End Date for the Time Series
startDate = '01/01/2016'
endDate = '31/12/2016'

# Get Mean Value of callOption or putOption 
def calculateCall():
	co = callOption()
	
	#Selector Function for callOption using Vectorized Function
	returnVariable = co.whatOption(S,K,'put');
	
	#Return Variable Printer if called
	try:
		if isinstance(returnVariable, basestring):
			optionPrice = Undefined
			print (returnVariable);
			
		else:
			optionPrice = returnVariable
			print (optionPrice)
	except:
		pass
	
# Year Time Series with Hourly - Daily - Weekly -Monthly Breakdown
def calculateTimeSeries():
	from timeSeriesModule.timeSeries import timeSeries
	import pandas as pd

	yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
	y_t = np.random.normal(mu, sigma, len(yearHourRange))	
# 	Creating Instance of timeSeries Class
	ts = timeSeries()
# 	Creating Date Range

	timeSeries = ts.getYearlyDataSeries(y_t,yearHourRange)
# 	Printing Results to be returned
# 	print(timeSeries)
	return timeSeries
	


	
# def calculate Daily Average of Y_T

def calculateDailyAverage(YearlytimeSeries, startDate, endDate):
	from timeSeriesModule.timeAverageCalc import timeAverageCalc
	avgYT =  timeAverageCalc()
	dailyAverage = avgYT.dailyAverage(YearlytimeSeries, startDate, endDate)
	return dailyAverage
# def calculate Daily Average of Y_T

def calculateWeeklyAverage(YearlytimeSeries, startDate, endDate):
	from timeSeriesModule.timeAverageCalc import timeAverageCalc
	avgYT =  timeAverageCalc()
	weeklyAverage = avgYT.weeklyAverage(YearlytimeSeries, startDate, endDate)
	return weeklyAverage
	
# def calculate Daily Average of Y_T

def calculateMontlyAverage(YearlytimeSeries, startDate, endDate):
	from timeSeriesModule.timeAverageCalc import timeAverageCalc
	avgYT =  timeAverageCalc()
	monthlyAverage = avgYT.monthlyAverage(YearlytimeSeries, startDate, endDate)
	return monthlyAverage
			

#Assignment1 Task 1	
calculateCall()

#Assignment2 Task 2
YearlytimeSeries = calculateTimeSeries()


print('The Yearly time Series is as follows: ');
print(YearlytimeSeries)


#Assignment2 Task 3

#calculate Daily Averages of Y_T
dailyAvg = calculateDailyAverage(YearlytimeSeries, startDate, endDate)

#calculate Weekly Averages of Y_T
weekylAvg = calculateWeeklyAverage(YearlytimeSeries, startDate, endDate)

#calculate Monthly Averages of Y_T
monthlyAvg = calculateMontlyAverage(YearlytimeSeries, startDate, endDate)




	