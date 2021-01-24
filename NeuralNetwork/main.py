from copy import deepcopy
import random
import NeuralNetwork as nn
import GradientDescent as GD
import Momentum as M
import Nesterov as NE
import NADAM as NA
import Debounce as D

random.seed(1)

dx = 0.001 #a hyperparameter
rate = 0.1 #a hyperparameter
beta = 0.9 #a hyperparameter
theta = 0.55 #a hyperparameter for Debounce
tolerance = 0.0001 #the tolerance for the location of the vertex to count
maxIter = 1000 #the maximum amount of iterations given to each model

iters = 50
optIter = 10
inputs = [1, 0, 1, 0]
outputs = [1, 1, 0, 1]
weights = [[random.uniform(0, 1) for row in range(len(inputs)+1)] for row in range(len(inputs))]

for row in range(iters):
	weights = GD.optimize(inputs, weights, outputs, optIter, rate)
	#weights = M.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = NE.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = NA.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = D.optimize(inputs, weights, outputs, optIter, rate, beta, theta)
	print('Iteration', row)
	print(nn.cost(inputs, outputs, weights), '\n')
