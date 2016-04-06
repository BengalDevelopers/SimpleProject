import numpy as np

#Class to generate mean
from callOptionModule.callOption import callOption
from iniparse.config import Undefined

co = callOption()
# Setting mean(mu) 0, standard deviation(sigma) 1
mu, sigma = 0, 1 

# Generating 100 random numbers  with mean and standard deviation as 0, 1 respectively.
S = np.random.normal(mu, sigma, 100); 

#Defining Strike Value k
K = 0.5


#Selector Function for callOption using Vectorized Function

returnVariable = co.whatOption(S,K,'put');


if isinstance(returnVariable, basestring):
	optionPrice = Undefined
	print (returnVariable);
	
else:
	optionPrice = returnVariable
	print (optionPrice)