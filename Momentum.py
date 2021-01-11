import numpy as np
import sympy as sym

def test(x, a):
	return x ** 2 - a * x

def derivative(x, a):
	return sym.diff(x ** 2 - a * x)

def momentum(predw, beta, rate, a):
	global weight

	dw = derivative(weight, a)
	
	predw = beta * predw + (1-beta)*dw

	return weight - rate * predw

if __name__ == '__main__':
	weight = 1000
	a = 2000
	rate = 0.1
	beta = 0.9
	predw = 0

	for t in range(100):
		print(weight, test(weight, a))
		weight = momentum(weight, beta, rate, a)
