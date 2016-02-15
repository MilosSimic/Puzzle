
def proxy(f):
	def wrap(*args, **kwargs):
		id = args[1]
		instance = args[0]
		plugin = instance.table.values()[id]

		if not plugin:
			instance.activate(id)

		return f(*args, **kwargs)
		
	return wrap

def notify(**params):
	def decor(f):
		def wrap(*args, **kwargs):
			instance = args[0]
			f(*args, **kwargs)

			instance.observable.notify(**params)

		return wrap
	return decor