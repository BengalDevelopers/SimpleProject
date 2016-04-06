import numpy as np

#Class to generate mean
from callOptionModule.callOption import callOption

co = callOption()
# Setting mean(mu) 0, standard deviation(sigma) 1
mu, sigma = 0, 1 

# Generating 100 random numbers  with mean and standard deviation as 0, 1 respectively.
S = np.random.normal(mu, sigma, 100); 

#Defining Strike Value k
K = 0.5

#Getting optionPrice using Vectorized Function
optionPrice = co.callOptionValuation(S,K)

#Getting optionPrice using For Loop 
optionPrice = co.callOptionValuationForLoop(S,K)


if optionPrice != 0:
	print (optionPrice)
else:
	print ('Error in Input Array');
