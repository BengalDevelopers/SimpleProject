class callOption:

	def debugGraph(self, Y, ycoordinateLabel, xcoordinateLabel):
		from plotModule.plotGraph import plotGraph
		pg = plotGraph()
		pg.plotGraphAgainstVariable(Y, ycoordinateLabel, xcoordinateLabel)	# Test Plot results on Graph
		return
	# Calculate Mean Value of Y	
	def callOptionValuation(self, stockPrice, strikeValue):
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
			
			# Since Y is 0 when S-K is false, and Y is 1 when S-K is true, multiplying the following:
			Y = differenceBetweenSAndK * comparatorResult
			# print(Y)
			
			#Generating Mean Value of Y
			mean = np.mean(Y)
			# print(mean)
			self.debugGraph(Y,"Y Co-ordinate Label", "X Co-ordinate Label");
			return mean
		else:
			#Returning Error if stockPrice Array Size is not 100
			return 0
	
	#Old For Loop Solution
	def callOptionValuationForLoop(self, stockPrice, strikeValue):
		import numpy as np
		S, K = stockPrice, strikeValue		
		Y = list()
		for x in np.nditer(S):
			if x > K:
				Y.append(x - K)
			else:
				Y.append(0)
		#print Y
		#Mean Value of Y = mean
		mean = np.mean(Y);
		#self.debugGraph(Y,"Y Co-ordinate Label", "X Co-ordinate Label");
		return mean
		
		