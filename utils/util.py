
def clear(file):
		return file.split('.')[0]

def eliminate(file):
	start= ('.', '_')
	end = ('.pyc')

	if not file.startswith(start) and not file.endswith(end):
		return file