from copy import deepcopy
import GradientDescent as gd
import NeuralNetwork as nn

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

def optimize(inputs, weights, outputs, iterations, rate, beta):
	newWeights = deepcopy(weights)
	velocity = 0
	for row in range(len(newWeights)):
		for column in range(len(newWeights[row])):
			for n in range(iterations):
				gradient = gd.gradientDescent(nn.cost, [deepcopy(inputs), deepcopy(outputs), deepcopy(newWeights)], [row, column], 0.001) * rate
				velocity = momentum(velocity, beta, gradient, rate)
				
				newWeights[row][column] -= velocity
	return newWeights
