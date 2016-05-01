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

#Simulation - How to Items to Simulate
simulationModelSize = 1000

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
def calculateTimeSeries(startDate, endDate):
# 	Creating Date Range
    import pandas as pd
    from timeSeriesModule.timeSeries import timeSeries
    yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
    #Creating Instance of timeSeries Class
    ts = timeSeries()
    timeSeries = ts.getYearlyDataSeries(yearHourRange, mu, sigma)
    #Printing Results to be returned
    #print(timeSeries)
    return timeSeries
	
#calculate Daily Average of Y_T
def calculateDailyAverage(YearlytimeSeries, startDate, endDate):
	from timeSeriesModule.timeAverageCalc import timeAverageCalc
	avgYT =  timeAverageCalc()
	dailyAverage = avgYT.dailyAverage(YearlytimeSeries, startDate, endDate)
	return dailyAverage

#def calculate Weekly Average of Y_T
def calculateWeeklyAverage(YearlytimeSeries, startDate, endDate):
	from timeSeriesModule.timeAverageCalc import timeAverageCalc
	avgYT =  timeAverageCalc()
	weeklyAverage = avgYT.weeklyAverage(YearlytimeSeries, startDate, endDate)
	return weeklyAverage
	
# def calculate Monthly Average of Y_T
def calculateMontlyAverage(YearlytimeSeries, startDate, endDate):
	from timeSeriesModule.timeAverageCalc import timeAverageCalc
	avgYT =  timeAverageCalc()
	monthlyAverage = avgYT.monthlyAverage(YearlytimeSeries, startDate, endDate)
	return monthlyAverage
			

#Assignment1 Task 1	
##calculateCall()

#Assignment2 Task 2
##YearlytimeSeries = calculateTimeSeries(startDate, endDate)


##print('The Yearly time Series is as follows: ');
##print(YearlytimeSeries)


#Assignment2 Task 3

#calculate Daily Averages of Y_T
#dailyAvg = calculateDailyAverage(YearlytimeSeries, startDate, endDate)

#calculate Weekly Averages of Y_T
#weekylAvg = calculateWeeklyAverage(YearlytimeSeries, startDate, endDate)

#calculate Monthly Averages of Y_T
#monthlyAvg = calculateMontlyAverage(YearlytimeSeries, startDate, endDate)

#Assignment3 Task 1
    

#Assignment3 Task 1 - Using Foor Loop
def simulateTS(simulationModelSize, startDate, endDate):
    import pandas as pd
    yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
    from simulationModule.simulateXDataframe import simulateXDataframe
    sm = simulateXDataframe()
    DFList = sm.simulationModel(simulationModelSize, yearHourRange, mu, sigma)
    return DFList

############For Testing Performance of For Loop Solution to Generate N Number of TS###########
def testSimulateTSPerformance():
    import time
    start_time = time.time()
    simulatedDataFrameList = simulateTS(simulationModelSize, startDate, endDate)
    print("--- %s seconds --- For Loop" % (time.time() - start_time))
    print("Total Time Series")
    print(len(simulatedDataFrameList))
    print(simulatedDataFrameList)

#simulatedTSList = simulateTS(simulationModelSize, startDate, endDate)
#print(len(simulatedTSList))
#print(simulatedTSList)

#testSimulateTSPerformance()


#Assignment3 Task 1 - Using Cython
def simulationTSCython(startDate, endDate, simulationModelSize):
    from cIntegration.cIntegrationModeler import cIntegrationModeler
    import pandas as pd
    sm = cIntegrationModeler()
    yearHourRange = pd.date_range(start=startDate, end=endDate, freq='H')
#    print(yearHourRange.ndim)
#    print(yearHourRange)
    TSList = sm.multiDataFrameGeneratorFunc(yearHourRange, simulationModelSize, mu, sigma)
    return TSList


###########For Testing Performance of For Cython Function to Generate N Number of TS###########
def testSimulateTSCythonPerformance():
    import time
    start_time = time.time()
    simulatedTSList = simulationTSCython(startDate, endDate, simulationModelSize)
    print("--- %s seconds --- Cython" % (time.time() - start_time))
    print("Total Time Series")
    print(len(simulatedTSList))
    print(simulatedTSList)
    

testSimulateTSCythonPerformance()
# simulatedTSList = simulationTSCython(startDate, endDate, simulationModelSize)
#print(simulatedTSList)