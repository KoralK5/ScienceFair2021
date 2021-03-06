import GradientDescent as gd
import Momentum as M

def demo(
	test,
	tolerance = 0.01,
	maxIter = 1000,
	x = 100,
	dx = 0.001,
	rate = 0.1,
	vertex = 0,
	beta = 0.9
	):

	f = open('Nesterov.txt', 'a')
	f.write('Nesterov'); f.close()

	velocity = 0
	for t in range(1, maxIter + 1):
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')
		
		gradient = gd.gradientDescent(test, [x - velocity], [0], dx)
		velocity = M.momentum(velocity, beta, gradient, rate)
		x -= velocity
		
		f = open('Nesterov.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()

		if abs(vertex - test(x)) < tolerance:
			break
	
	print('\n\nNESTEROV')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
