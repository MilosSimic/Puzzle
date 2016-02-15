from state import State
from state_const import state_const

class Starting(State):
	def __init__(self):
		super(self, State).__init__()

	def do_action(self, context):
		pass

	def __str__(self):
		return repr(state_const.STARTING)