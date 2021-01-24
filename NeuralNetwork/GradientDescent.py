from copy import deepcopy

def change(l, i, x):
	if len(i) > 1:
		change(l[i[0]], i[1:len(i)], x)
	else:
		l[i[0]] += x

def gradientDescent(func, args, pos, dx):
	nArgs = deepcopy(args)
	change(nArgs[2], pos, dx)
	return (func(*nArgs) - func(*args)) / dx
