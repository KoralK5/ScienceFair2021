def change(l, i, x):
	if len(i) > 1:
		change(l[i[0]], i[1:len(i)], x)
	else:
		l[i[0]] += x

def gradientDescent(func, args, pos, dx):
	nArgs = args[:]
	change(nArgs, pos, dx)
	return (func(*nArgs) - func(*args)) / dx

def demo(
	test,
	tolerance = 0.01,
	x = 100,
	dx = 0.001, 
	rate = 0.1,
	vertex = 0
	):

	f = open('GradientDescent.txt', 'a')
	f.write('Gradient Descent'); f.close()

	adjust = 0
	t = 0
	while test(x) > vertex + tolerance or test(x) < vertex - tolerance:
		print(f'\nx: {x}\nf(x): {test(x)}\najustment: {adjust}')

		adjust = gradientDescent(test, [x], [0], dx)
		x -= adjust * rate
		
		f = open('GradientDescent.txt', 'a')
		f.write(f'\n{test(x)}'); f.close()
		
		t += 1

	print('\n\nGRADIENT DESCENT')
	print(f'Local Minimum: {test(x)}')
	print(f'Iterations: {t}')

	return test(x), t

if __name__ == '__main__':
	demo()
