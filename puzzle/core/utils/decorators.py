from threading import Thread

class JobProcess(Thread):
	def __init__(self, f, id, context):
		super(JobProcess, self).__init__()
		self.context = context
		self.id = id
		self.f = f
		self.daemon = True

	def run(self):
		self.f(self.context, self.id)

def restrict_init(wait_time=5):
	def init(f):
		def wrapper(*args, **kwargs):
			id = args[1]
			context = args[0]

			job = JobProcess(f, id, context)
			job.start()
			job.join(wait_time)

			if job.is_alive():
				#job.terminate()
				raise RuntimeError('Plugin initialisation take too much time!')
		return wrapper
	return init

def restrict_proxy(active=False):
	def proxy(f):
		def wrap(*args, **kwargs):
			id = args[1]
			instance = args[0]
			plugin = instance.table.values()[id]

			if active:
				if not plugin:
					instance.activate(id)

			return f(*args, **kwargs)
			
		return wrap
	return restrict_proxy