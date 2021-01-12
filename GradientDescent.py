def change(l, i, x):
	if len(i) > 1:
		change(l[i[0]], i[1:len(i)], x)
	else:
		l[i[0]] += x

def gradientDescent(func, args, pos, dx):
	nArgs = args[:]
	change(nArgs, pos, dx)
	return (func(*nArgs) - func(*args)) / dx

if __name__ == '__main__':
	def test(x):
		return (x)**2 + 7
	rate = 0.1
	dx = 0.001
	a = 100

	for t in range(1000):
		adjust = gradientDescent(test, [a], [0], dx)
		a -= adjust * rate
		print(a, test(a), adjust)

		f = open('results.txt', 'a')
		f.write(f'\n{test(a)}')
		f.close()
