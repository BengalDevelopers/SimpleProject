class callOption:

	def debugGraph(self, Y, ycoordinateLabel, xcoordinateLabel):
		from plotModule.plotGraph import plotGraph
		pg = plotGraph()
		pg.plotGraphAgainstVariable(Y, ycoordinateLabel, xcoordinateLabel)	# Test Plot results on Graph
		return
		
	def callOptionValuation(self, stockPrice, strikeValue):
		import numpy as np
		S, K = stockPrice, strikeValue		
		Y = list()
		for x in np.nditer(S):
			if x > K:
				Y.append(x - K)
			else:
				Y.append(0)
		# print np.size(Y) 
		#print Y
		#Mean Value of Y = mean
		mean = np.mean(Y);
		#self.debugGraph(Y,"Y Co-ordinate Label", "X Co-ordinate Label");
		return mean
		
		