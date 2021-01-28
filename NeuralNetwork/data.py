def format(path):
	from PIL import Image, ImageOps
	yes = f'{path}yes'
	no = f'{path}no'
	test = f'{path}pred'

	inputs = []
	outputs = []

	full, num = True, 0
	while full:
		try:
			inputs += ImageOps.grayscale(Image.open(f'{yes}\\y{num}.jpg')).getdata()
			outputs += [[1]]
		except:
			full = False
		num += 1

	full, num = True, 0
	while full:
		try:
			inputs += ImageOps.grayscale(Image.open(f'{no}\\no{num}.jpg')).getdata()
			outputs += [[0]]
		except:
			full = False
		num += 1
	return inputs, outputs
	
