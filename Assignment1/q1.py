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

optionPrice = co.callOptionValuation(S,K)

print (optionPrice)

