from state import State
from state_const import state_const
from starting import Starting
from active import Active

class Resolved(State):
	def __init__(self):
		super(self, State).__init__()

	def on_start(self, context):
		context.state = Starting()

		#do some dirty work before activate plugin
		context.start()

		context.state = Active()

	def on_unregister(self):
		context.state = Uninstalled()

		#if need something do it here
		context.unregister()

	def __str__(self):
		return repr(state_const.RESOLVED)