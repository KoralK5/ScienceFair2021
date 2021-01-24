import random
import NeuralNetwork as nn
import GradientDescent as GD
import Momentum as M
import Nesterov as NE
import NADAM as NA
import Debounce as D
from copy import deepcopy

random.seed(1)

dx = 0.001 #a hyperparameter
rate = 0.1 #a hyperparameter
beta = 0.9 #a hyperparameter
theta = 0.55 #a hyperparameter for Debounce
tolerance = 0.0001 #the tolerance for the location of the vertex to count
maxIter = 1000 #the maximum amount of iterations given to each model

iterations = 100
inputs = [1, 0, 1, 0]
outputs = [1, 1, 0, 1]
weights = [[random.uniform(0, 1) for row in range(len(inputs)+1)] for row in range(len(inputs))]

weights = GD.optimize(inputs, weights, outputs, iterations, rate)
#weights = M.optimize(inputs, weights, outputs, iterations, rate, beta)
#weights = NE.optimize(inputs, weights, outputs, iterations, rate, beta)
#weights = NA.optimize(inputs, weights, outputs, iterations, rate, beta)
#weights = D.optimize(inputs, weights, outputs, iterations, rate, beta, theta)

inputs, outputs = nn.neuralNetwork(inputs, weights)

for row in outputs:
	print(sum(row)/len(row))
