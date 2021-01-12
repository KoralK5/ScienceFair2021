from time import time
import GradientDescent
import Momentum
import NADAM
import Nesterov
	
tolerance = 0.00001

input('Gradient Descent')
start1 = time(); GradientDescent.demo(tolerance); end1 = time()
print(f'time: {end1-start1}s\n\n')

input('Momentum')
start2 = time(); Momentum.demo(tolerance); end2 = time()
print(f'time: {end2-start2}s\n\n')

input('Nesterov')
start3 = time(); Nesterov.demo(tolerance); end3 = time()
print(f'time: {end3-start3}s\n\n')

input('NADAM')
start4 = time(); NADAM.demo(tolerance); end4 = time()
print(f'time: {end4-start4}s\n\n')
