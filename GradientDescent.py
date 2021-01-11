import numpy as np

def change(l, i, x):
	if len(i) > 1:
	    change(l[i[0]], i[1:len(i)], x)
	else:
		l[i[0]] += x

def cost(func, args, targets):
	outputs = np.array(func(*args))
	targets = np.array(targets)
	error = (outputs - targets) ** 2
	return np.sum(error)

def gradientDescent(func, args, targets, h, position):
	#print(args)
	cost1 = cost(func, args, targets)
	newArgs = list(args)[:]
	change(newArgs, position, h)
	newArgs = tuple(newArgs)
	#print(newArgs)
	cost2 = cost(func, newArgs, targets)
	#print(cost1, cost2)
	return (cost1 - cost2) / h

def test(x, a):
	return x ** 2 + a * x

a = 0.001
t = 150
h = 0.1
w = 2

for x in range(100):
	print(w, test(10, w))
	w += gradientDescent(test, (10, w), 150, h, [1]) * a
