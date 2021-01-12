import numpy as np

def sumAct(x, b):
	return sum(x) + b

def neuron(inputs, weights, bias, actFunc, args):
	return actFunc(np.array(input) * np.array(weights), bias, *args)

def layer(neuronFunc, args, compType = 'Sequential'):
	if compType == 'Sequential':
		returns = []
		for arg in args:
			returns.append(neuronFunc(*arg))
		return returns
		