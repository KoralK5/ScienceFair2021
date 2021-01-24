from copy import deepcopy
import NeuralNetwork as nn

def change(l, i, x):
	if len(i) > 1:
		change(l[i[0]], i[1:len(i)], x)
	else:
		l[i[0]] += x

def gradientDescent(func, args, pos, dx):
	nArgs = deepcopy(args)
	change(nArgs[2], pos, dx)
	return (func(*nArgs) - func(*args)) / dx

def optimize(inputs, weights, outputs, iterations, rate):
	newWeights = deepcopy(weights)
	for row in range(len(newWeights)):
		for column in range(len(newWeights[row])):
			for n in range(iterations):
				newWeights[row][column] -= gradientDescent(nn.cost, [deepcopy(inputs), deepcopy(outputs), deepcopy(newWeights)], [row, column], 0.001) * rate
	return newWeights
