import imp

module_types = { imp.PY_SOURCE: 'source', 
				imp.PY_COMPILED: 'compiled', 
				imp.C_EXTENSION: 'extension', 
				imp.PY_RESOURCE: 'resource', 
				imp.PKG_DIRECTORY: 'package',}

def clear(file):
		return file.split('.')

def eliminate(file):
	start= ('.', '_')
	end = ('.pyc')

	if not file.startswith(start) and not file.endswith(end):
		return file

PY_EXT = 'py'