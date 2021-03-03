from copy import deepcopy
import matplotlib.pyplot as plt; plt.gray()
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
	return np.load(path, allow_pickle=True)

path = 'D:\\Users\\Koral Kulacoglu\\Coding\\python\\AI\\ScienceFair21\\NeuralNetwork\\Data\\'

inputs, outputs = grab(f'{path}test.csv')
weightsGD = getWeights(f'{path}GDweights.npy')
weightsM = getWeights(f'{path}Mweights.npy')
weightsNE = getWeights(f'{path}NEweights.npy')
weightsNA = getWeights(f'{path}NAweights.npy')
weightsD = getWeights(f'{path}Dweights.npy')
# weightsD = getWeights(f'{path}weights.npy')

num = 0
GDscore, Mscore, NEscore, NAscore, Dscore = 0, 0, 0, 0, 0
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
	
	if predGD == real:
		GDscore += 1
	if predM == real:
		Mscore += 1
	if predNE == real:
		NEscore += 1
	if predNA == real:
		NAscore += 1
	if predD == real:
		Dscore += 1

	print(f'\n'*100, f'Real: {real}\n')

	print('                    Guess | Certainty | Score')
	print('                    --------------------------')
	print(f'Gradient Descent:     {predGD}   |    {int(max(list(newOutputsGD))*100)}%    |  {int(GDscore/(row+1)*100)}%')
	print(f'Momentum:             {predM}   |    {int(max(list(newOutputsM))*100)}%    |  {int(Mscore/(row+1)*100)}%')
	print(f'Nesterov:             {predNE}   |    {int(max(list(newOutputsNE))*100)}%    |  {int(NEscore/(row+1)*100)}%')
	print(f'NADAM:                {predNA}   |    {int(max(list(newOutputsNA))*100)}%    |  {int(NAscore/(row+1)*100)}%')
	print(f'Debounce:             {predD}   |    {int(max(list(newOutputsD))*100)}%    |  {int(Dscore/(row+1)*100)}%')
	
	img = np.array([col*255 for col in inputs[row]])
	img = img.reshape(28, 28)
	plt.imshow(img)
	plt.show(block=False)
	plt.pause(2)
	plt.close()
