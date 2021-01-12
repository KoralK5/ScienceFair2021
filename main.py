from time import time
import GradientDescent
import Momentum
import Nesterov
import NADAM

def test(x):
	return x**2 + 7 + x

def stats():
	print('\n'*100,'            STATS\n       ~~~~~~~~~~~~~~~~~')
	print('\n\nGRADIENT DESCENT')
	print(f'Local Minimum: {x1}')
	print(f'Time: {end1-start1}s')
	print(f'Iterations: {t1}')

	print('\n\nMOMENTUM')
	print(f'Local Minimum: {x2}')
	print(f'Time: {end2-start2}s')
	print(f'Iterations: {t2}')

	print('\n\nNESTEROV')
	print(f'Local Minimum: {x3}')
	print(f'Time: {end3-start3}s')
	print(f'Iterations: {t3}')

	print('\n\nNADAM')
	print(f'Local Minimum: {x4}')
	print(f'Time: {end4-start4}s')
	print(f'Iterations: {t4}')

input('-> GRADIENT DESCENT <-')
start1 = time(); x1, t1 = GradientDescent.demo(test); end1 = time()
print(f'time: {end1-start1}s\n\n')

input('-> MOMENTUM <-')
start2 = time(); x2, t2 = Momentum.demo(test); end2 = time()
print(f'time: {end2-start2}s\n\n')

input('-> NESTEROV <-')
start3 = time(); x3, t3 = Nesterov.demo(test); end3 = time()
print(f'time: {end3-start3}s\n\n')

input('-> NADAM <-')
start4 = time(); x4, t4 = NADAM.demo(test); end4 = time()
print(f'time: {end4-start4}s\n\n')

stats()
