from state import *
from excp import LifecycleException, NotImplementedException

class Plugin(object):
	def __init__(self, name, description, version, author, image=None):
		self.name = name
		self.description = description
		self.version = version
		self.author = author
		self.image = image
		self.state = Resolved()

	def start(self):
		#first check the policy if valiation occur thrrow PolicyException
		#Define your own policy, if needed
		self.policy_check()

		#rest of start goes here :D


	def policy_check(self):
		pass

	def stop(self):
		pass

	def call(self, **kwargs):
		raise NotImplementedException("Don't be lazy, implement plugin :D!")

	def restart(self):
		pass

	def unregister(self):
		pass

	def info(self):
		return "Name {}, Author, Version {}".format(self.name, self.author, self.version)

	def __str__(self):
		return repr(self.name)
