import GradientDescent as gd

def momentum(velocity, beta, gradient, rate):
	return beta * velocity + gradient * rate

if __name__ == '__main__':
	def test(x):
		return x ** 2 + 7
	
	velocity = 0
	beta = 0.9
	dx = 0.001
	a = 100
	rate = 0.1

	for t in range(1000):
		print(a, test(a), velocity)

		gradient = gd.gradientDescent(test, [a], [0], dx)
		velocity = momentum(velocity, beta, gradient, rate)
		a -= rate * velocity

		f = open('results.txt', 'a')
		f.write(f'\n{test(a)}')
		f.close()
