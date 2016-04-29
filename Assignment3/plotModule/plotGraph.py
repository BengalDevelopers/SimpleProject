class plotGraph:
	def plotGraphAgainstVariable(self, Y, yLabel, xLabel):
		import matplotlib.pyplot as plt		
		plt.plot(Y)
		plt.ylabel(yLabel)
		plt.xlabel(xLabel)
		plt.show()