import random
import NeuralNetwork as nn
import GradientDescent as GD
from copy import deepcopy

def optimize(inputs, weights, outputs, iterations, rate):
	newWeights = deepcopy(weights)
	for row in range(len(newWeights)):
		for column in range(len(newWeights[row])):
			for n in range(iterations):
				newWeights[row][column] -= GD.gradientDescent(nn.cost, [deepcopy(inputs), deepcopy(outputs), deepcopy(newWeights)], [row, column], 0.001) * rate
	return newWeights

random.seed(1)

rate = 1
iterations = 100
inputs = [1, 0, 1]
outputs = [1, 1, 0]
weights = [[random.uniform(0, 1) for row in range(4)] for row in range(len(inputs))]

weights = optimize(inputs, weights, outputs, iterations, rate)

inputs, outputs = nn.neuralNetwork(inputs, weights)

for row in outputs:
	print(sum(row)/len(row))
