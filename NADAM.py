import GradientDescent as gd

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

def demo(
	test,
	tolerance = 0.01,
	x = 100,
	dx = 0.001,
	rate = 0.1,
	vertex = 0,
	beta = 0.9
	):
	
	f = open('NADAM.txt', 'a')
	f.write('NADAM'); f.close()

	velocity = 0
	t = 0
	while test(x) > vertex + tolerance or test(x) < vertex - tolerance:
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')

		gradient = gd.gradientDescent(test, [x], [0], dx)
		velocity = momentum(velocity, beta, gradient, rate)
		x -= beta * velocity + rate * gradient

		f = open('NADAM.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()

		t += 1
	
	print('\n\nNADAM')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
