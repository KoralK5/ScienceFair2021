import GradientDescent as gd

def momentum(velocity, beta, func, args, position, dx):
	return beta * velocity + gd.gradientDescent(func, args, position, dx)

if __name__ == '__main__':
	def test(x):
		return x ** 2 + 7
	
	velocity = 0
	beta = 0.9
	dx = 0.001
	a = 10
	rate = 0.1

	for t in range(100000):
		print(a, test(a), velocity)
		velocity = momentum(velocity, beta, test, [a], [0], dx)
		a -= rate * velocity
