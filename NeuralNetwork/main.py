from copy import deepcopy
import random; random.seed(1)
import numpy as np
import NeuralNetwork2 as nn
import GradientDescent2 as GD
import Momentum as M
import Nesterov as NE
import NADAM as NA
import Debounce as D
print('Imports Sucessfull')

def grab(path):
	trainingDataFile = open(path, 'r')
	trainingData = trainingDataFile.read()
	trainingData = trainingData.split("\n")
	trainingData = trainingData[1:len(trainingData) - 32000]

	for j in range(len(trainingData)):
		trainingData[j] = trainingData[j].split(",")
	for x in range(len(trainingData)):
		for y in range(len(trainingData[x])):
			trainingData[x][y] = int(trainingData[x][y])
	trainingData = np.array(trainingData)

	trainingInputs = trainingData.transpose()[1:len(trainingData) + 1].transpose()
	trainingInputs = np.array([np.array(i) for i in trainingInputs])

	trainingOutputs = trainingData.transpose()[0]
	trainingOutputs = list(trainingOutputs)
	for k in range(len(trainingOutputs)):
		tmp = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		tmp[trainingOutputs[k]] = 1
		trainingOutputs[k] = deepcopy(tmp)
	trainingOutputs = np.array(trainingOutputs)

	return trainingInputs, trainingOutputs

path = str(input('Path: '))
dataPath = f'{path}\\train.csv'

inputsD, outputsD = grab(dataPath)
print('Data Formatted')

iters = 1
dx = 0.001
rate = 0.1
beta = 0.9
theta = 1000
scale = 0.1
layerData = [1, 16, 16, len(outputsD[0])]

weights = nn.generateWeights(layerData, len(inputsD[0]))

print('Weights Initialized')

open(f'{path}scores.txt', 'r+').truncate(0)
for row in range(iters):
	print('\nIteration:', row+1, '\n\n')
	for inp in range(len(outputsD)):
		inputs = inputsD[inp]
		outputs = outputsD[inp]
		
		# netCorrect = GD.Network(inputs, weights, outputs, dx)
		# weights = netCorrect.adjustNetwork(rate)

		weights = GD.backPropagation(inputs, weights, outputs, dx, rate)
		#weights = M.optimize(inputs, weights, outputs, rate, dx, beta)
		#weights = NE.optimize(inputs, weights, outputs, rate, dx, beta)
		#weights = NA.optimize(inputs, weights, outputs, rate, dx, beta)
		#weights = D.optimize(inputs, weights, outputs, rate, dx, beta, scale)
		
		cost = nn.neuralNetworkCost(inputs, weights, outputs)
		
		print('\nExample:', inp+1)
		print('Cost:', cost)

		f = open(f'{path}scores.txt', 'a')
		f.write(f'\n{cost}'); f.close()

		open(f'{path}weights.txt', 'r+').truncate(0)
		f = open(f'{path}weights.txt', 'a')
		f.write(f'{list(weights)}'); f.close()

	print('Final Cost:', cost)
