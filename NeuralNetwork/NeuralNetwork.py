import numpy as np
from copy import deepcopy

def generateWeights(layerData, inputQuantity):
	layerDepthLimit = len(layerData)
	augmentedLayerData = [inputQuantity] + deepcopy(layerData)
	return [np.random.rand(layerData[layerDepth], augmentedLayerData[layerDepth] + 1)/2 for layerDepth in range(layerDepthLimit)]

def layer(inputs, weights):
	biasedInputs = np.append(np.array(inputs), 1)
	neuronInputs = np.repeat(np.array([biasedInputs]), len(weights), axis = 0)
	weightedInputs = neuronInputs * np.array(weights)
	output = np.tanh(np.sum(weightedInputs, axis = 1))
	return output

def neuralNetwork(inputs, weights):
	outputs = []
	layerInputs = deepcopy(inputs)
	for layerWeights in weights:
		layerInputs = layer(layerInputs, layerWeights)
		outputs.append(deepcopy(layerInputs))
	return outputs

def layerCost(inputs, weights, outputs):
	neuronErrors = (outputs - layer(inputs, weights)) ** 2
	return np.sum(neuronErrors)
		
def neuralNetworkCost(inputs, weights, outputs):
	neuronErrors = (outputs - neuralNetwork(inputs, weights)[-1]) ** 2
	return np.sum(neuronErrors)
