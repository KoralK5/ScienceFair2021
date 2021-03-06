from copy import deepcopy
import time
import random
import numpy as np
import os
import keyboard
import snakeNN as nn
import snakeNNgame as game
print('Imports Sucessfull')

path = 'D:\\Users\\Koral Kulacoglu\\Coding\\python\\AI\\ScienceFair21\\NeuralNetwork\\Games\\Snake\\snakeData\\'
dataPath = f'{path}\\train.csv'

changeAmount = 500000
mutationAmount = 100
decimal = 100
batch = 5
layerData = [80, 40, 20, 4]

weights = nn.generateWeights(layerData, 10*10+1)

print('Weights Initialized')
print('Training...')

open(f'{path}snakeScores.csv', 'r+').truncate(0)

start, inp, speed, disp = time.time(), 0, 0, 0
while True:
	changeAmount -= int(changeAmount*0.1) + 1000
	inp += 1

	if batch < 100:
		batch += 1

	weightsBatch = [[]]
	costBatch = [0]
	
	for net in range(batch):
		netWeights = nn.mutate(weights, changeAmount, mutationAmount, decimal)
		t = int(time.time() - start)
		
		if keyboard.is_pressed('p'):
			disp = abs(disp-1)

		costBatch.append(game.play(netWeights, inp, net, t, costBatch, disp))
		weightsBatch.append(netWeights)

	os.system('cls')
	
	f = open(f'{path}snakeScores.csv', 'a')
	f.write(f'\n{max(costBatch)}'); f.close()

	weights = weightsBatch[costBatch.index(max(costBatch))]
	np.save(f'{path}genWeights.npy', np.array(weights, dtype=object))

	print('Generation:', inp)
	print('Network:', inp*(net+1))
	print(f'Time: {t}s')
	print('Best:', max(costBatch))
