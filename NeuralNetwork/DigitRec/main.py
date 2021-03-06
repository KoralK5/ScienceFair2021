from copy import deepcopy
import time
import random; random.seed(1)
import numpy as np
import NeuralNetwork as nn
import GradientDescent as GD
import Momentum as M
import Nesterov as NE
import NADAM as NA
import Debounce as D
print('Imports Sucessfull')

def grab(path):
	trainingData = open(path, 'r+').read().split("\n")
	trainingData = trainingData[1:len(trainingData)-1]

	trainingData = np.array([[int(col) for col in row.split(',')] for row in trainingData])

	trainingInputs = [row/255 for row in trainingData.transpose()[1:len(trainingData) + 1].transpose()]
	trainingInputs = np.array([np.array(i) for i in trainingInputs])

	trainingOutputs = trainingData.transpose()[0]
	trainingOutputs = list(trainingOutputs)
	for k in range(len(trainingOutputs)):
		tmp = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
		tmp[trainingOutputs[k]] = 1
		trainingOutputs[k] = deepcopy(tmp)
	trainingOutputs = np.array(trainingOutputs)

	return trainingInputs, trainingOutputs

path = 'D:\\Users\\Koral Kulacoglu\\Coding\\python\\AI\\ScienceFair21\\NeuralNetwork\\Data\\'
dataPath = f'{path}\\train.csv'

inputsD, outputsD = grab(dataPath)

print('Data Formatted')

dx = 0.001
rate = 0.1
beta = 0.9
scale = 0.1
layerData = [16, 16, len(outputsD[0])]

weights = nn.generateWeights(layerData, len(inputsD[0]))

print('Weights Initialized')
print('Training...')

open(f'{path}scores.csv', 'r+').truncate(0)
start = time.time()

num, cost, t = 0, 0, 32347
for inp in range(len(outputsD)):
	inputs = inputsD[0]
	outputs = outputsD[0]

	inputsD = inputsD[1:]
	outputsD = outputsD[1:]

	weights, newOutputs = GD.backPropagation(inputs, weights, outputs, dx, rate)
	# weights, newOutputs = M.backPropagation(inputs, weights, outputs, dx, rate, beta)
	# weights, newOutputs = NE.backPropagation(inputs, weights, outputs, dx, rate, beta)
	# weights, newOutputs = NA.backPropagation(inputs, weights, outputs, dx, rate, beta)
	# weights, newOutputs = D.backPropagation(inputs, weights, outputs, dx, rate, beta, scale)

	cost += nn.neuralNetworkCost(inputs, weights, outputs)
	t = int(32347 - time.time() + start)
	if t < 0:
		break

	if not (inp+1)%10:
		print('\n\nNetwork:', num+1)
		print(f'Time: {t}s')
		print('Cost:', cost/10)
		print('\nPred:', newOutputs)
		print('Real:', outputs)

		f = open(f'{path}scores.csv', 'a')
		f.write(f'\n{cost/10}'); f.close()
		cost = 0

	#np.save(f'{path}GDweights.npy', np.array(weights, dtype=object))
	num += 1

print('Final Cost:', cost)
print('Iterations:', num)
