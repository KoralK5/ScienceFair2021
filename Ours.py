import GradientDescent as gd

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

def demo(
	test,
	tolerance = 0.01,
	velocity = 0, 
	beta = 0.9, 
	dx = 0.001, 
	x = 100, 
	rate = 0.1
	):
	
	f = open('Ours.txt', 'a')
	f.write('Ours'); f.close()

	t = 0
	while test(x) > 0+tolerance or test(x) < 0-tolerance:
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')

		if abs(velocity) < 1:
			velocity *= 0.1

		gradient = gd.gradientDescent(test, [x], [0], dx)
		velocity = momentum(velocity, beta, gradient, rate)
		x -= beta * velocity + rate * gradient
		t += 1

		f = open('Ours.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()
	
	print('\n\nOurs')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
