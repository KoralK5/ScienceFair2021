from copy import deepcopy
from PIL import Image
import numpy as np
import NeuralNetwork as nn

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

path = 'path\\'

inputs, outputs = grab(f'{path}test.csv')
weightsGD = getWeights(f'{path}GDweights.npy')
weightsM = getWeights(f'{path}Mweights.npy')
weightsNE = getWeights(f'{path}NEweights.npy')
weightsNA = getWeights(f'{path}NAweights.npy')
weightsD = getWeights(f'{path}Dweights.npy')

num = 0
for row in range(len(outputs)):
	newOutputsGD = nn.neuralNetwork(inputs[row], weightsGD)[-1]
	newOutputsM = nn.neuralNetwork(inputs[row], weightsM)[-1]
	newOutputsNE = nn.neuralNetwork(inputs[row], weightsNE)[-1]
	newOutputsNA = nn.neuralNetwork(inputs[row], weightsNA)[-1]
	newOutputsD = nn.neuralNetwork(inputs[row], weightsD)[-1]

	real = list(outputs[row]).index([1])
	predGD = list(newOutputsGD).index(max(list(newOutputsGD)))
	predM = list(newOutputsM).index(max(list(newOutputsM)))
	predNE = list(newOutputsNE).index(max(list(newOutputsNE)))
	predNA = list(newOutputsNA).index(max(list(newOutputsNA)))
	predD = list(newOutputsD).index(max(list(newOutputsD)))

	input('\n- ')
	print(f'Real: {real}\n')

	print('      Guess | Certainty')
	print(f'GD:       {predGD} | {int(max(list(newOutputsGD))*100)}%')
	print(f'M :       {predM} | {int(max(list(newOutputsM))*100)}%')
	print(f'NE:       {predNE} | {int(max(list(newOutputsNE))*100)}%')
	print(f'NA:       {predNA} | {int(max(list(newOutputsNA))*100)}%')
	print(f'D :       {predD} | {int(max(list(newOutputsD))*100)}%')
