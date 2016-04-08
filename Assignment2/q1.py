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
# 	Setting Start Date and End Date for the Time Series
	startDate = '01/01/2016'
	endDate = '31/12/2016'	
# 	Creating Instance of timeSeries Class
	ts = timeSeries()
# 	Sending Parameters to time series Generator
	timeSeries = ts.getYearlyDataSeries(mu, sigma,startDate, endDate)
# 	Printing Returned Results
	print(timeSeries)



#Functions to Call for Checking Assignments

#Assignment1 Task 1	
calculateCall()

#Assignment2 Task 2
calculateTimeSeries()
	