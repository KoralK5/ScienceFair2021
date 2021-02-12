from copy import deepcopy
from ast import literal_eval
import numpy as np
import NeuralNetwork as nn

path = 'D:\\Users\\Koral Kulacoglu\\Coding\\python\\AI\\ScienceFair21\\NeuralNetwork\\'

def grab(path):
	trainingData = open(path, 'r').read()
	trainingData = trainingData.split("\n")
	trainingData = trainingData[1:len(trainingData)-1]

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

	#print('Real:', real)
	#print('\nPred:', pred)

	if real == pred:
		num += 1

print(num/row)
