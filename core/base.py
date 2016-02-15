from utils import State
from excp import LifecycleException, NotImplementedException

class Plugin(object):
	def __init__(self, name, description, version, author, image=None):
		self.name = name
		self.description = description
		self.version = version
		self.author = author
		self.image = image
		self.state = State.RESOLVED

	def on_start(self):
		if self.state == State.RESOLVED:
			self.state = State.STARTING

			#first check the policy if valiation occur thrrow PolicyException
			#Define your own policy, if needed
			self.policy_check()

			#do some dirty work before activate plugin
			self.start()

			self.state = State.ACTIVE
		else:
			raise LifecycleException("Lifecycle valiation exception!")

	def start(self):
		pass

	def policy_check(self):
		pass

	def on_stop(self):
		if self.state == State.ACTIVE:
			self.state = State.STOPPIMG

			#release what you have
			self.stop()

			self.state = State.STOPPED
		else:
			raise LifecycleException("Lifecycle valiation exception!")

	def stop(self):
		pass

	def call(self, **kwargs):
		raise NotImplementedException("Don't be lazy, implement plugin :D!")

	def restart(self):
		pass

	def on_restart(self):
		if self.state == State.STOPPED:
			self.state = State.RESTARTING

			#add some methods if needed
			self.restart()

			self.state = State.RESOLVED
		else:
			raise LifecycleException('Lifecycle valiation exception!')

	def unregister(self):
		pass

	def on_unregister(self):
		if self.state in [State.STOPPED, State.RESOLVED, State.INSTALLED]:
			#if need something do it here
			self.unregister()
		else:
			raise LifecycleException('Lifecycle valiation exception!')


	def info(self):
		return "Name {}, Author, Version {}".format(self.name, self.author, self.version)

	def __str__(self):
		return repr(self.name)
