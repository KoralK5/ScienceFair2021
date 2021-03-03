from copy import deepcopy
import time
import random; random.seed(1)
import numpy as np
import os
import snakeNN as nn
import snakeNNgame as game
print('Imports Sucessfull')

path = 'D:\\Users\\Koral Kulacoglu\\Coding\\python\\AI\\ScienceFair21\\NeuralNetwork\\Games\\Snake\\snakeData\\'
dataPath = f'{path}\\train.csv'

changeAmount = 50
mutationAmount = 50
decimal = 100
batch = 25
layerData = [16, 16, 4]

weights = nn.generateWeights(layerData, 10*10)

print('Weights Initialized')
print('Training...')

open(f'{path}snakeScores.csv', 'r+').truncate(0)

start, inp = time.time(), 0
while True:
	inp += 1
	weightsBatch, costBatch = [], []
	for net in range(batch):
		netWeights = deepcopy(weights)
		netWeights = nn.mutate(netWeights, changeAmount, mutationAmount, decimal)

		costBatch.append(game.play(netWeights))
		weightsBatch.append(netWeights)
		
		t = int(time.time() - start)
		print('\n\nGeneration:', inp)
		print('Network:', net)
		print(f'Time: {t}s')
		print('Lifespan:', costBatch[-1])
		print('Best:', max(costBatch))
		time.sleep(1)
		os.system('cls')

	f = open(f'{path}snakeScores.csv', 'a')
	f.write(f'\n{max(costBatch)}'); f.close()

	weights = weightsBatch[costBatch.index(max(costBatch))]
	np.save(f'{path}genWeights.npy', np.array(weights, dtype=object))
