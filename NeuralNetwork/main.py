from copy import deepcopy
import random
import NeuralNetwork as nn
import GradientDescent as GD
import Momentum as M
import Nesterov as NE
import NADAM as NA
import Debounce as D

random.seed(1)

iters = 50
optIter = 10
inputs = [1, 0, 1, 0]
outputs = [1, 1, 0, 1]
weights = [[random.uniform(0, 1) for row in range(len(inputs)+1)] for row in range(len(inputs))]

dx = 0.001
rate = 0.1
beta = 0.9
theta = 0.55

for row in range(iters):
	weights = GD.optimize(inputs, weights, outputs, optIter, rate)
	#weights = M.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = NE.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = NA.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = D.optimize(inputs, weights, outputs, optIter, rate, beta, theta)
	print('Iteration', row+1)
	print('Cost:', nn.cost(inputs, outputs, weights), '\n')

print('Final Cost:', nn.cost(inputs, outputs, weights))

#Gradient Descent Final Cost: 0.0012331873647288651
#Momentum Final Cost: 0.00230511868475897
#Nesterov Final Cost: 0.00230452251251315
#NADAM Final Cost: 0.0021185030798304937
#Debounce Final Cost: 0.0052760176928349336
