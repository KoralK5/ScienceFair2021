import GradientDescent as gd

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

def demo(
	tolerance = 0.001, 
	velocity = 0, 
	beta = 0.9, 
	dx = 0.001, 
	x = 100, 
	rate = 0.1
	):
	
	def test(x):
		return x ** 2 + 7
	
	t = 0
	while test(x) > 7 + tolerance:
		print(f'\nx: {x}\nf(x): {test(x)}\nvelocity: {velocity}')

		gradient = gd.gradientDescent(test, [x], [0], dx)
		velocity = momentum(velocity, beta, gradient, rate)
		x -= rate * velocity
		t += 1

		f = open('results.txt', 'a')
		f.write(f'\n{test(x)}')
		f.close()

	print(f'\n\nLocal Minimum: {test(x)}')
	print(f'Iterations: {t}')

if __name__ == '__main__':
	demo()
