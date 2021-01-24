import numpy as np
import copy as cp

def cost(inputs, outputs, weights):
	return sum((np.array(outputs) - np.array(layer(inputs, weights))) ** 2)

def sumAct(x):
	return np.tanh(sum(x))

def ReLU(x):
	return np.tanh(max(list(x) + [0]))

def adjustWeight(inputs, outputs, weights, addWeight, pos):
	newWeights = cp.deepcopy(weights)
	newWeights[pos[0]][pos[1]] += addWeight
	cost1 = cost(inputs, outputs, weights)
	cost2 = cost(inputs, outputs, newWeights)
	return (cost2 - cost1) / addWeight

def adjustInput(inputs, outputs, weights, addInput, pos):
	newInputs = cp.deepcopy(inputs)
	newInputs[pos] += addInput
	cost1 = cost(inputs, outputs, weights)
	cost2 = cost(newInputs, outputs, weights)
	return (cost2 - cost1) / addInput

def adjustLayer(inputs, outputs, weights, addInput, addWeight):
	inputAdjust, weightAdjust = [], []
	for neuronNumber in range(len(weights)):
		weightAdjust.append(adjustWeight(inputs, outputs, weights, addWeight, neuronNumber))
		inputAdjust.append(adjustInput(inputs, outputs, weights, addInput, neuronNumber))
	return inputAdjust, weightAdjust

def backPropagation(inputs, initialOutputs, weights, addInput, addWeight):
	outputs = np.array(initialOutputs)
	neuronOutputs = neuralNetwork()

def neuron(inputs, weights):
	biasedInputs = cp.deepcopy(list(inputs)) + [1]
	return sumAct(np.array(biasedInputs) * np.array(weights))

def layer(inputs, weights):
	outputs = []
	for weight in weights:
		outputs.append(neuron(inputs, weight))
	return outputs

def neuralNetwork(initialInputs, weights):
	neuronOutputs = []	
	inputs = cp.deepcopy(initialInputs)

	for weight in weights:
		inputs = np.array(layer(inputs, weight))
		neuronOutputs.append(inputs)
	return inputs, np.array(neuronOutputs)
