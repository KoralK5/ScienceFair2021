import random
import snakeNN
import time
import os
import keyboard
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
			if arr[head[0]-1%10][head[1]] == '🍎':
				arr[head[0]-1%10][head[1]] = '🟩'
				head[0] -= 1
				return putApple(arr), tail

			elif arr[head[0]-1%10][head[1]] == '🟩':
				return 0, 0

			else:
				arr[head[0]-1%10][head[1]] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
				
				tail = tail[1:]
				head[0] -= 1
				return arr, tail
		except:
			return 0, 0

	elif head[2] == 'S':
		try:
			if arr[(head[0]+1)%10][head[1]] == '🍎':
				arr[(head[0]+1)%10][head[1]] = '🟩'
				head[0] += 1
				return putApple(arr), tail

			elif arr[(head[0]+1)%10][head[1]] == '🟩':
				return 0, 0

			else:
				arr[(head[0]+1)%10][head[1]] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
				
				tail = tail[1:]
				head[0] += 1
				return arr, tail
		except:
			return 0, 0

	elif head[2] == 'A':
		try:
			if arr[head[0]][(head[1]-1)%10] == '🍎':
				arr[head[0]][(head[1]-1)%10] = '🟩'
				head[1] -= 1
				return putApple(arr), tail

			elif arr[head[0]][(head[1]-1)%10] == '🟩':
				return 0, 0

			else:
				arr[head[0]][(head[1]-1)%10] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
				
				tail = tail[1:]
				head[1] -= 1
				return arr, tail
		except:
			return 0, 0

	elif head[2] == 'D':
		try:
			if arr[head[0]][(head[1]+1)%10] == '🍎':
				arr[head[0]][(head[1]+1)%10] = '🟩'
				head[1] += 1
				return putApple(arr), tail

			elif arr[head[0]][(head[1]+1)%10] == '🟩':
				return 0, 0
				
			else:
				arr[head[0]][(head[1]+1)%10] = '🟩'
				arr[tail[0][0]][tail[0][1]] = '⬛'
			
				tail = tail[1:]
				head[1] += 1
				return arr, tail
		except:
			return 0, 0

def binarize(arr, head, tail):
	inputs = []
	for row in range(len(arr)):
		for col in range(len(arr[row])):
			if arr[row][col] == '⬛':
				inputs += [0]

			elif arr[row][col] == '🟩':
				inputs += [0.5]

			elif arr[row][col] == '🍎':
				inputs += [10]
				apple = [row, col]
	
			elif [row, col] == [head[0], head[1]]:
				inputs += [2]
			
			elif [row, col] == [tail[0][0], tail[0][1]]:
				inputs += [1]

	inputs += [abs(head[0]%10 - apple[0]) + abs(head[1]%10 - apple[1])]

	return inputs

def points(arr, head):
	for row in range(len(arr)):
		for col in range(len(arr[row])):
			if arr[row][col] == '🍎':
				return (10 - abs(head[0]%10-row) + 10 - abs(head[1]%10-col))/20

def play(weights, inp, net, t, costBatch, disp):
	arr = [['⬛']*10 for row in range(10)]
	arr[4][4] = '🟩'
	arr[4][5] = '🟩'
	arr[4][6] = '🟩'
	arr[4][7] = '🟩'
	arr = putApple(arr)
	head, tail = [4,7,'D'], [[4,4],[4,5],[4,6],[4,7]]
	ite, wait, score, prevScore, speed = 0, 0, 0, 0, 0
	while arr != 0 and wait < (len(tail)-3)*10:
		score = len(tail)-4 + points(arr, head)

		if disp:
			print('Generation:', inp)
			print('Network:', net)
			print(f'Time: {t}s')

			print('\nBest:', max(costBatch))
			print('Score:', score)

			show(arr)
			if keyboard.is_pressed('s'):
				speed = abs(speed-1)
			time.sleep(speed)

			os.system('cls')

		if score == prevScore:
			wait += 1
		else:
			wait = 0
		
		ite += 1
		tail += [[head[0], head[1]]]
		head[2] = snakeNN.neuralNetwork(binarize(arr, head, tail), weights)
		arr, tail = go(arr, head, tail)

		prevScore = score
	return score
