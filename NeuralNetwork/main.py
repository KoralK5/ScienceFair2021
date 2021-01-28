from copy import deepcopy
import random
import NeuralNetwork as nn
import GradientDescent as GD
import Momentum as M
import Nesterov as NE
import NADAM as NA
import Debounce as D

random.seed(1)

iters = 52
optIter = 1
inputs = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
outputs = [1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
weights = [[random.uniform(0, 1) for row in range(len(inputs)+1)] for row in range(len(inputs))]
dx = 0.001
rate = 1
beta = 0.9
theta = 10000
scale = 0.1

path = 'directory'

open(f'{path}scores.txt', 'r+').truncate(0)

for row in range(iters):
	weights = GD.optimize(inputs, weights, outputs, optIter, rate)
	#weights = M.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = NE.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = NA.optimize(inputs, weights, outputs, optIter, rate, beta)
	#weights = D.optimize(inputs, weights, outputs, optIter, rate, beta, theta, scale)
	
	cost = nn.cost(inputs, outputs, weights)
	print('Iteration', row+1)
	print('Cost:', cost, '\n')

	f = open(f'{path}scores.txt', 'a')
	f.write(f'\n{cost}'); f.close()

print('Final Cost:', cost)
