import numpy as np

def change(l, i, x):
	if len(i) > 1:
	    change(l[i[0]], i[1:len(i)], x)
	else:
		l[i[0]] += x

def gradientDecent(func, args, pos, dx):
	nArgs = args[:]
	change(nArgs, pos, dx)
	return func(*nArgs) - func(*args)

if __name__ == '__main__':
	def test(x):
		return x**2 + 5

	rate = 0.1
	dx = 0.01
	a = 10

	for t in range(10000):
		adjust = gradientDecent(test, [a], [0], dx)
		print(adjust, a, test(a))
		a -= adjust * rate
