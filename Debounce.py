import GradientDescent as gd
import Momentum as M
from numpy import tanh

def sign(x):
	try:
		return x / abs(x)
		
	except:
		return 0

def demo(
	test,
	tolerance = 0.01,
	maxIter = 1000,
	x = 100,
	dx = 0.001,
	rate = 0.1,
	vertex = 0,
	beta = 0.9, 
	theta = 1
	):
	
	f = open('Debounce.txt', 'a')
	f.write('Debounce'); f.close()

	velocity, preVelocity = 0, 0
	for t in range(1, maxIter + 1):
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')

		gradient = gd.gradientDescent(test, [x], [0], dx)
		velocity = M.momentum(velocity, beta, gradient, rate)
		x -= beta * velocity + rate * gradient
		velocity = velocity * (1 - 0.9 * (sign(abs(velocity - preVelocity)) / 2 + 0.5))
		
		preVelocity = velocity

		f = open('Debounce.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()
		
		if abs(vertex - test(x)) < tolerance:
			break
	
	print('\n\nDebounce')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
