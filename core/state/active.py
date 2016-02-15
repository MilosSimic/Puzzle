from state import State
from state_const import state_const
from stopping import Stopping
from stopped import Stopped
from uninstalled import Uninstalled

class Active(State):
	def __init__(self):
		super(self, State).__init__()

	def on_stop(self, context):
		context.state = Stopping()

		#release what you have
		context.stop()

		context.state = Stopped()

	def __str__(self):
		return repr(state_const.ACTIVE)