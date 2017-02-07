from puzzle.core.excp.lifecycle import LifecycleException
from state_const import state_const

class State(object):
	def __init__(self, context):
		self.context = context

	def on_start(self):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_stop(self):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_restart(self):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_unregister(self):
		raise LifecycleException("Lifecycle valiation exception!")

class Starting(State):
	def __init__(self, context):
		super(Starting, self).__init__(context)

	def on_start(self):
		#do some dirty work before activate plugin
		self.context.start()
		self.context.state = Active(self.context)

	def __str__(self):
		return repr(state_const.STARTING)

class Active(State):
	def __init__(self, context):
		super(Active, self).__init__(context)

	def on_stop(self):
		self.context.state = Stopping(self.context)
		self.context.state.on_stop()

	def __str__(self):
		return repr(state_const.ACTIVE)

class Resolved(State):
	def __init__(self, context):
		super(Resolved, self).__init__(context)

	def on_start(self):
		self.context.state = Starting(self.context)
		self.context.state.on_start()

	def on_unregister(self):
		self.context.state = Uninstalled(self.context)
		self.context.state.on_unregister()

	def __str__(self):
		return repr(state_const.RESOLVED)

class Restarting(State):
	def __init__(self, context):
		super(Restarting, self).__init__(context)

	def on_restart(self):
		#add some methods if needed
		self.context.restart()
		self.context.state = Resolved(self.context)

	def __str__(self):
		return repr(state_const.RESTARTING)

class Stopped(State):
	def __init__(self, context):
		super(Stopped, self).__init__(context)

	def on_restart(self):
		self.context.state = Restarting(self.context)
		self.context.state.on_restart()

	def on_unregister(self):
		self.context.state = Uninstalled(self.context)
		self.context.state.on_unregister()

	def __str__(self):
		return repr(state_const.STOPPED)

class Stopping(State):
	def __init__(self, context):
		super(Stopping, self).__init__(context)

	def on_stop(self):
		#release what you have
		self.context.stop()
		self.context.state = Stopped(self.context)

	def __str__(self):
		return repr(state_const.STOPPING)

class Uninstalled(State):
	def __init__(self, context):
		super(Uninstalled, self).__init__(context)

	def on_unregister(self):
		#if need something do it here
		self.context.unregister()

	def __str__(self):
		return repr(state_const.UNINSTALLED)