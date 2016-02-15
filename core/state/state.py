from ..excp import LifecycleException

class State(object):
	def __init__(self):
		pass

	def do_action(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_start(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_stop(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_restart(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_unregister(self, context):
		raise LifecycleException("Lifecycle valiation exception!")