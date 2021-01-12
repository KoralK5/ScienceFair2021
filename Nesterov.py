import GradientDescent as gd

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

def demo(
	test,
	tolerance = 0.001, 
	velocity = 0,
	beta = 0.9,
	dx = 0.001, 
	x = 100, 
	rate = 0.1
	):

	f = open('Nesterov.txt', 'a')
	f.write('Nesterov'); f.close()

	t = 0
	while test(x) > 7 + tolerance:
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')
		
		gradient = gd.gradientDescent(test, [x - velocity], [0], dx)
		velocity = momentum(velocity, beta, gradient, rate)
		x -= rate * velocity
		t += 1
		
		f = open('Nesterov.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()
	
	print('\n\nNESTEROV')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
