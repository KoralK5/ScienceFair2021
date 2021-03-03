import random; random.seed(1)
import snakeNN
import time
import os
from copy import deepcopy

def show(arr):
	for row in arr:
		print(''.join(row))

def putApple(arr):
	x, y = [], []
	for row in range(len(arr)):
		for col in range(len(arr[row])):
			if arr[row][col] == '⬛':
				x += [row]
				y += [col]
			elif arr[row][col] == '🍎':
				arr[row][col] = '⬛'

	point = random.randint(0, len(x)-1)

	arr[x[point]][y[point]] = '🍎'
	return arr

def go(arr, head, tail):
	if head[2] == 'W':
		try:
			if arr[head[0]-1][head[1]] == '🍎':
				arr[head[0]-1][head[1]] = '🟩'
				head[0] -= 1
				return putApple(arr), tail

			elif arr[head[0]-1][head[1]] == '🟩':
				return 0, 0

			else:
				arr[head[0]-1][head[1]] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
				
				tail = tail[1:]
				head[0] -= 1
				return arr, tail
		except:
			return 0, 0

	elif head[2] == 'S':
		try:
			if arr[head[0]+1][head[1]] == '🍎':
				arr[head[0]+1][head[1]] = '🟩'
				head[0] += 1
				return putApple(arr), tail

			elif arr[head[0]+1][head[1]] == '🟩':
				return 0, 0

			else:
				arr[head[0]+1][head[1]] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
				
				tail = tail[1:]
				head[0] += 1
				return arr, tail
		except:
			return 0, 0

	elif head[2] == 'A':
		try:
			if arr[head[0]][head[1]-1] == '🍎':
				arr[head[0]][head[1]-1] = '🟩'
				head[1] -= 1
				return putApple(arr), tail

			elif arr[head[0]][head[1]-1] == '🟩':
				return 0, 0

			else:
				arr[head[0]][head[1]-1] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
				
				tail = tail[1:]
				head[1] -= 1
				return arr, tail
		except:
			return 0, 0

	elif head[2] == 'D':
		try:
			if arr[head[0]][head[1]+1] == '🍎':
				arr[head[0]][head[1]+1] = '🟩'
				head[1] += 1
				return putApple(arr), tail

			elif arr[head[0]][head[1]+1] == '🟩':
				return 0, 0
				
			else:
				arr[head[0]][head[1]+1] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
			
				tail = tail[1:]
				head[1] += 1
				return arr, tail
		except:
			return 0, 0

def binarize(arr, head):
	inputs = []
	for row in range(len(arr)):
		for col in range(len(arr[row])):
			if arr[row][col] == '⬛':
				inputs += [0]
			elif [row, col] == [head[0], head[1]]:
				inputs += [2]
			elif arr[row][col] == '🟩':
				inputs += [1]
			elif arr[row][col] == '🍎':
				inputs += [10]
	return inputs

def play(weights):
	arr = [['⬛']*10 for row in range(10)]
	arr[4][4] = '🟩'
	arr[4][5] = '🟩'
	arr[4][6] = '🟩'
	arr[4][7] = '🟩'
	arr = putApple(arr)
	head, tail = [4,7,'D'], [[4,4,'D'],[4,5,'D'],[4,6,'D'],[4,7,'D']]
	ite, wait, score, prevScore = 0, 0, 0, 0
	while arr != 0 and wait < (score+1)*100:
		score = len(tail)
		print('Score:', score)
		show(arr)
		time.sleep(0.2)
		os.system('cls')

		if score == prevScore:
			wait += 1
		else:
			wait = 0
		
		ite += 1
		tail += [[head[0], head[1]]]
		head[2] = snakeNN.neuralNetwork(binarize(arr, head), weights)
		arr, tail = go(arr, head, tail)

		prevScore = score
	return score - 1/ite
