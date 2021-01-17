import GradientDescent as gd

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

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
	
	f = open('Momentum.txt', 'a')
	f.write('Momentum'); f.close()
	
	velocity = 0
	for t in range(1, maxIter + 1):
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')

		gradient = gd.gradientDescent(test, [x], [0], dx)
		velocity = momentum(velocity, beta, gradient, rate)
		x -= velocity

		f = open('Momentum.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()

		if abs(vertex - test(x)) < tolerance:
			break

	print('\n\nMOMENTUM')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
