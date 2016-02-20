from core.excp.lifecycle import LifecycleException
from state_const import state_const

class State(object):
	def __init__(self):
		pass

	def on_start(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_stop(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_restart(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

	def on_unregister(self, context):
		raise LifecycleException("Lifecycle valiation exception!")

class Starting(State):
	def __init__(self):
		super(Starting, self).__init__()

	def on_start(self, context):
		#do some dirty work before activate plugin
		context.start()
		context.state = Active()

	def __str__(self):
		return repr(state_const.STARTING)

class Active(State):
	def __init__(self):
		super(Active, self).__init__()

	def on_stop(self, context):
		context.state = Stopping()
		context.state.on_stop(context)

	def __str__(self):
		return repr(state_const.ACTIVE)

class Resolved(State):
	def __init__(self):
		super(Resolved, self).__init__()

	def on_start(self, context):
		context.state = Starting()
		context.state.on_start(context)

	def on_unregister(self, context):
		context.state = Uninstalled()
		context.state.on_unregister(context)

	def __str__(self):
		return repr(state_const.RESOLVED)

class Restarting(State):
	def __init__(self):
		super(Restarting, self).__init__()

	def on_restart(self, context):
		#add some methods if needed
		context.restart()
		context.state = Resolved()

	def __str__(self):
		return repr(state_const.RESTARTING)

class Stopped(State):
	def __init__(self):
		super(Stopped, self).__init__()

	def on_restart(self, context):
		context.state = Restarting()
		context.state.on_restart(context)

	def on_unregister(self):
		context.state = Uninstalled()
		context.state.on_unregister(context)

	def __str__(self):
		return repr(state_const.STOPPED)

class Stopping(State):
	def __init__(self):
		super(Stopping, self).__init__()

	def on_stop(self, context):
		#release what you have
		context.stop()
		context.state = Stopped()

	def __str__(self):
		return repr(state_const.STOPPING)

class Uninstalled(State):
	def __init__(self):
		super(Uninstalled, self).__init__()

	def on_unregister(self, context):
		#if need something do it here
		context.unregister()

	def __str__(self):
		return repr(state_const.UNINSTALLED)