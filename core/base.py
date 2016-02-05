from state import State
from excp import LifecycleException, NotImplementedException

class Plugin(object):
	def __init__(self, name, description, version, author, image=None):
		self.name = name
		self.description = description
		self.version = version
		self.author = author
		self.image = image
		self.state = State.RESOLVED
		
	def activate(self, **kwargs):
		self.on_start()

	def on_start(self):
		if self.state == State.RESOLVED:
			self.state = State.STARTING

			#do some dirty work before activate plugin
			self.start()

			self.state = State.ACTIVE
		else:
			raise LifecycleException('Lifecycle valiation exception!')

	def start(self):
		pass

	def on_stop(self):
		if self.state == State.ACTIVE:
			self.state = State.STOPPIMG

			#release what you have
			self.stop()

			self.state = State.STOPPED
		else:
			raise LifecycleException('Lifecycle valiation exception!')

	def stop(self):
		pass

	def call(self, **kwargs):
		raise NotImplementedException("Don't be lazy, implement plugin :D!")

	def restart(self):
		pass

	def on_restart(self):
		self.on_stop()

		#add some methods if needed
		self.restart()
		self.state = state.RESOLVED

		self.on_start()
