from copy import deepcopy
from numpy import tanh
import GradientDescent as gd
import Momentum as M
import NeuralNetwork as nn

def optimize(inputs, weights, outputs, iterations, rate, beta, theta):
	newWeights = deepcopy(weights)
	preVelocity = 0
	velocity = 0
	for row in range(len(newWeights)):
		for column in range(len(newWeights[row])):
			for n in range(iterations):
				gradient = gd.gradientDescent(nn.cost, [deepcopy(inputs), deepcopy(outputs), deepcopy(newWeights)], [row, column], 0.001) * rate
				velocity = M.momentum(velocity, beta, gradient, rate)

				newWeights[row][column] -= beta * velocity + rate * gradient

				beta = theta + (1-theta) * tanh(velocity - preVelocity)
				preVelocity = velocity
	return newWeights