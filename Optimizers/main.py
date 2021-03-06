#internal libraries
import GradientDescent
import Momentum
import Nesterov
import NADAM
import Debounce

#a function to compare optimizers 
def run(params):
	from time import time

	open('GradientDescent.txt', 'r+').truncate(0)
	open('Momentum.txt', 'r+').truncate(0)
	open('Nesterov.txt', 'r+').truncate(0)
	open('NADAM.txt', 'r+').truncate(0)
	open('Debounce.txt', 'r+').truncate(0)

	input('-> GRADIENT DESCENT <-')
	start1 = time(); x1, t1 = GradientDescent.demo(*params); end1 = time()
	print(f'time: {end1 - start1}s\n\n')

	input('-> MOMENTUM <-')
	start2 = time(); x2, t2 = Momentum.demo(*params, beta); end2 = time()
	print(f'time: {end2 - start2}s\n\n')

	input('-> NESTEROV <-')
	start3 = time(); x3, t3 = Nesterov.demo(*params, beta); end3 = time()
	print(f'time: {end3 - start3}s\n\n')

	input('-> NADAM <-')
	start4 = time(); x4, t4 = NADAM.demo(*params, beta); end4 = time()
	print(f'time: {end4 - start4}s\n\n')

	input('-> Debounce <-')
	start5 = time(); x5, t5 = Debounce.demo(*params, beta, theta); end5 = time()
	print(f'time: {end5 - start5}s\n\n')

	print('\n'*100,'            STATS\n        ~~~~~~~~~~~~~~~')
	print('\n\nGRADIENT DESCENT')
	print(f'Local Minimum: {x1}')
	print(f'Time: {end1 - start1}s')
	print(f'Iterations: {t1}')

	print('\n\nMOMENTUM')
	print(f'Local Minimum: {x2}')
	print(f'Time: {end2 - start2}s')
	print(f'Iterations: {t2}')

	print('\n\nNESTEROV')
	print(f'Local Minimum: {x3}')
	print(f'Time: {end3 - start3}s')
	print(f'Iterations: {t3}')

	print('\n\nNADAM')
	print(f'Local Minimum: {x4}')
	print(f'Time: {end4 - start4}s')
	print(f'Iterations: {t4}')

	print('\n\nDebounce')
	print(f'Local Minimum: {x5}')
	print(f'Time: {end5 - start5}s')
	print(f'Iterations: {t5}')

def plot(GD, MO, NE, NA, DE):
	from matplotlib import pyplot as plt

	plt.fill_between(range(len(GD)), GD, alpha=0.7, linewidth=3, label='Gradient Descent', color='b')
	plt.fill_between(range(len(MO)), MO, alpha=0.7, linewidth=3, label='Momentum', color='r') 
	plt.fill_between(range(len(NE)), NE, alpha=0.7, linewidth=3, label='Nesterov', color='orange') 
	plt.fill_between(range(len(NA)), NA, alpha=0.7, linewidth=3, label='NADAM', color='g') 
	plt.fill_between(range(len(DE)), DE, alpha=0.7, linewidth=3, label='Debounce', color='m')

	plt.title('NN Optimizer Comparison')
	plt.xlabel('Iteration')
	plt.ylabel('Error')
	
	plt.legend()
	plt.show()

#a function limited to one variable
def test(x):
	return x**2

x = 0.912 #the starting point of the function
minimum = 0 #the vertex of the function

dx = 0.001 #a hyperparameter
rate = 0.1 #a hyperparameter
beta = 0.9 #a hyperparameter
theta = 0.55 #a hyperparameter for Debounce
tolerance = 0.0001 #the tolerance for the location of the vertex to count
maxIter = 1000 #the maximum amount of iterations given to each model

#running the tests
params = (test, tolerance, maxIter, x, dx, rate, minimum)
run(params)

#reading the data
GD = [float(row) for row in open('GradientDescent.txt').read().split('\n')[1:]]
MO = [float(row) for row in open('Momentum.txt').read().split('\n')[1:]]
NE = [float(row) for row in open('Nesterov.txt').read().split('\n')[1:]]
NA = [float(row) for row in open('NADAM.txt').read().split('\n')[1:]]
DE = [float(row) for row in open('Debounce.txt').read().split('\n')[1:]]

plot(GD, MO, NE, NA, DE)
