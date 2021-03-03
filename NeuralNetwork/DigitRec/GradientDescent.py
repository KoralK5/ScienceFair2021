import NeuralNetwork as nn
from copy import deepcopy

class Layer:
	def __init__(self, inputs, weights, outputs, dx):
		self.inputs = inputs
		self.weights = weights
		self.outputs = outputs
		self.dx = dx

	def adjustWeight(self, neuron, weight):
		newWeights = deepcopy(self.weights)
		newWeights[neuron][weight] += self.dx
		return (nn.layerCost(self.inputs, newWeights, self.outputs) - nn.layerCost(self.inputs, self.weights, self.outputs)) / self.dx

	def adjustNeuron(self, neuron):
		newInputs = deepcopy(self.inputs)
		newInputs[neuron] += self.dx
		return (nn.layerCost(newInputs, self.weights, self.outputs) - nn.layerCost(self.inputs, self.weights, self.outputs)) / self.dx
		
	def adjustLayer(self, rate):
		newWeights = deepcopy(self.weights)
		newInputs = deepcopy(self.inputs)
		for neuron in range(len(self.weights)):
			for weight in range(len(self.weights[neuron])):
				newWeights[neuron][weight] -= self.adjustWeight(neuron, weight) * rate
				
		for neuron in range(len(self.inputs)):
			newInputs[neuron] -= self.adjustNeuron(neuron) * rate
		return newWeights, newInputs

class Network:
	def __init__(self, inputs, weights, outputs, dx):
		self.inputs = inputs
		self.weights = weights
		self.outputs = outputs
		self.dx = dx

	def adjustWeight(self, layer, neuron, weight):
		newWeights = deepcopy(self.weights)
		newWeights[layer][neuron][weight] += self.dx
		return (nn.neuralNetworkCost(self.inputs, newWeights, self.outputs) - nn.neuralNetworkCost(self.inputs, self.weights, self.outputs)) / self.dx

	def adjustNeuron(self, layer, neuron):
		newInputs = deepcopy(self.inputs)
		newInputs[layer][neuron] += self.dx
		return (nn.neuralNetworkCost(newInputs, self.weights, self.outputs) - nn.neuralNetworkCost(self.inputs, self.weights, self.outputs)) / self.dx
		
	def adjustNetwork(self, rate):
		newWeights = deepcopy(self.weights)
		for layer in range(len(self.weights)):
			for neuron in range(len(self.weights[layer])):
				for weight in range(len(self.weights[layer][neuron])):
					newWeights[layer][neuron][weight] -= self.adjustWeight(layer, neuron, weight) * rate
		return newWeights

def backPropagation(inputs, weights, outputs, dx, rate):
	newWeights = deepcopy(weights)[::-1]
	newOutputs = deepcopy(outputs)

	inps = nn.neuralNetwork(inputs, weights)
	networkInputs = inps[-2::-1] + [deepcopy(inputs)]

	for currentLayer in range(len(networkInputs)):
		layer = Layer(networkInputs[currentLayer], newWeights[currentLayer], newOutputs, dx)
		newWeights[currentLayer], newOutputs = layer.adjustLayer(rate)
	return newWeights[::-1], inps[-1]
