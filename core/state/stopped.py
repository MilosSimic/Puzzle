from state import State
from state_const import state_const
from retarting import Restarting
from resolved import Resolved
from uninstalled import Uninstalled

class Stopped(State):
	def __init__(self):
		super(self, State).__init__()

	def on_restart(self, context):
		context.state = Restarting()

		#add some methods if needed
		context.restart()

		context.state = Resolved()

	def on_unregister(self):
		context.state = Uninstalled()

		#if need something do it here
		context.unregister()

	def __str__(self):
		return repr(state_const.STOPPED)