from copy import deepcopy
from ast import literal_eval
import numpy as np
import NeuralNetwork as nn

path = 'path\\'

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

def getWeights(path):
	with open(path, 'rb') as f:
		path = np.load(f, allow_pickle=True)
	return path

inputs, outputs = grab(f'{path}test.csv')
weights = getWeights(f'{path}weights.npy')

dx = 0.001
rate = 0.1
beta = 0.9
scale = 0.1
num = 0

for row in range(len(outputs)):
	newOutputs = nn.neuralNetwork(inputs[row], weights)[-1]

	real = list(outputs[row]).index([1])
	pred = list(newOutputs).index(max(list(newOutputs)))
	input('- ')
	print('Real:', real)
	print('\nPred:', pred)
	print(newOutputs)

	if pred == real:
		num += 1

print(num/row)
