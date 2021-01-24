from copy import deepcopy
import GradientDescent as gd
import Momentum as M
import NeuralNetwork as nn

def optimize(inputs, weights, outputs, iterations, rate, beta):
	newWeights = deepcopy(weights)
	velocity = 0
	for row in range(len(newWeights)):
		for column in range(len(newWeights[row])):
			for n in range(iterations):
				gradient = gd.gradientDescent(nn.cost, [deepcopy(inputs), deepcopy(outputs), deepcopy(newWeights)], [row, column], 0.001) * rate
				velocity = M.momentum(velocity, beta, gradient, rate)
				
				newWeights[row][column] -= beta * velocity + rate * gradient
	return newWeights
