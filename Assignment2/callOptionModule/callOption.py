class callOption:

	def debugGraph(self, Y, ycoordinateLabel, xcoordinateLabel):
		from plotModule.plotGraph import plotGraph
		pg = plotGraph()
		pg.plotGraphAgainstVariable(Y, ycoordinateLabel, xcoordinateLabel)	# Test Plot results on Graph
		return
	
	#Option Selector Function. Chooses which value to return based on user input
	def whatOption(self, stockPrice, strikeValue, option):
		callOption = 'Call';
		putOption = 'Put';
		if option.lower() == callOption.lower():
			print('Working Call Function');	 
			callValue = self.__callOptionValuation(stockPrice, strikeValue);
			return callValue;
		elif option.lower() == putOption.lower():
			print('Put Option Called');
			putValue = self.__putOptionValuation(stockPrice, strikeValue);
			return putValue;
		else:
			print('Option Not Found');
			return 0;	
		
	# Calculate Mean Value of Y	-- call option
	def __callOptionValuation(self, stockPrice, strikeValue):
		import numpy as np	
		# Vectorizing Stock Price - Array Size is 100
		S = np.array(stockPrice)
		# Vectorizing Strike Value - Single Value Array
		K = np.array(strikeValue)
		print(S.size)
		# Checking Input Size and its Validity
		if S.size == 100:	
			# Converting Single Value array to match Expected Size of Stock Prices
			K = np.repeat(K, 100)
			#Now Comparing Stock Price with Strike Value and Generating Boolean Based Results
			comparatorResult = S > K
			# print(comparatorResult)
			
			#Now Finding the Differnece between each Stock Price value with Strike Value
			differenceBetweenSAndK = S - K
			
			# Since callOption is 0 when S-K is false, and Y is 1 when S-K is true, multiplying the following:
			callOption = differenceBetweenSAndK * comparatorResult
			# print(callOption)
			
			#Generating Mean Value of Y
			mean = np.mean(callOption)
			# print(mean)
			#self.debugGraph(callOption,"callOption", "X Co-ordinate Label");
			return mean
		else:
			#Returning Error if stockPrice Array Size is not 100
			return 'error'
	
	def __putOptionValuation(self, stockPrice, strikeValue):
		import numpy as np	
		# Vectorizing Stock Price - Array Size is 100
		S = np.array(stockPrice)
		
		# Vectorizing Strike Value - Single Value Array
		K = np.array(strikeValue)
		# Checking Input Size and its Validity
		if S.size == 100:
			# Converting Single Value array to match Expected Size of Stock Prices
			K = np.repeat(K, 100)
# 			print(S)
# 			print(K)
			#Now Comparing Stock Price with Strike Value and Generating Boolean Based Results
			comparatorResult = K > S
# 			print(comparatorResult)
			#Now Finding the Differnece between Strike Value and Each Stock Price Value
			differenceBetweenKAndS = K - S
			
			#Since Y is 0 when S = K or S < K, hence multiplying the comparatorResult with differenceBetweenKAndS
			putOption = differenceBetweenKAndS * comparatorResult
			#print(putOption)
			
			mean = np.mean(putOption)
			#print(mean)			
			return mean;
		else:
			return 'error101'
		
		
		
		