import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import minimize

if __name__ == "__main__":
	# Function to minimize
	def func(x):
	    return x**4 + 5*x**3 - 2*x**2 + x + 1
	# call to minimize function
	s = minimize(func,5)

	# array of x values that are defined on function
	xspace = np.linspace(-100,100,1000)

	# Plots the function and minimum
	plt.plot(xspace, func(xspace), label='f(x)')
	plt.scatter(s.x[0], func(s.x[0]), color='r', label=f'minimum (x = {func(s.x[0]):.2f}))')
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.xlim(-10,0)
	plt.ylim(-100, 3)
	plt.legend()
	plt.show()