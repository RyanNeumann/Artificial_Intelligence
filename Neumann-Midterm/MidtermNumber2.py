# Created by: Ryan Neumann


import numpy as np


class MidtermNumber2:


	N = 0  #Starting approximation
	d = 1 -  input('Please enter a confidence level(Between 0.00 and 1.00 ex. For 95% enter 0.95!): ') #For 95% confidence level
	e = d
	it = 0 #Starting it counter
	
	
	
	g = ((8 / e ** 2) * np.log((4 * (((2 * N) ** 10) + 1)) / d)) 	
	
	while  N <= g:
		
		N += 1
		g = ((8 / e ** 2) * np.log((4 * (((2 * N) ** 10) + 1)) / d))
		it += 1
		
	confidence = 100 - (d * 100) 
			
	print "You would need a sample size of exactly: " + str(N) + " to have a " + str(confidence) + "% confidence level that your generalization error is at most " + str(e)
