from utils import State, proxy
from inspect import getmembers, isclass
from base import Plugin
from uuid import uuid1
from excp import LifecycleException
from loader import PluginLoader

class PluginTable(object):
	def __init__(self, observable, plugins_dir):
		self.table = {}
		self.observable = observable
		self.loader = PluginLoader(plugins_dir)

	def activate(self, id):
		'''
		throws:
			IndexError if plugin doesn't exists
		'''

		plugin = self.table.values()[id]
		if isclass(plugin):
			plugin = plugin()

			key = self.table.keys()[id]
			self.table[key] = plugin

			self.start_plugin(id)

	def activate_all(self):
		for k, v in self.table.iteritems():
			if isclass(v):
				self.table[k] = v()

	@proxy
	def get_plugin(self, id):
		'''
			Proxy-Lazy implementatino. Try to get plugin if can.
			If can't, then initialise plugin then return it

			throws:
				AttributeError if plugin is not resolved
				IndexError if plugin doesn't exists
		'''

		plugin = self.table.values()[id]
		
		if plugin.state == State.ACTIVE:
			return plugin
		else:
			print plugin.info()
		
	def start_plugin(self, id):
		'''
		throws:
			TypeError if plugin is not activated
			IndexError if plugin desen't exists
			LifecycleException if try to valiate lifecycle
		'''

		self.table.values()[id].on_start()
		self.observable.notify(position=id, state=State.ACTIVE, call="start_plugin")
		
	def stop_plugin(self, id):
		self.table.values()[id].on_stop()
		self.observable.notify(position=id, state=State.STOPPED, call="stop_plugin")
		
	def restart_plugin(self, id):
		self.table.values()[id].on_restart()
		self.observable.notify(position=id, state=State.RESOLVED, call="restart_plugin")

	def register_plugin(self, module, key=None):
		if not key:
			key = uuid1()

		self.table[key] = self.extract_plugin(module)
		self.observable.notify(position=len(self.table.keys()), state=State.RESOLVED, call="register_plugin")

	def extract_plugin(self, module):
		for name, obj in getmembers(module):
			if isclass(obj) and issubclass(obj, Plugin) and name not in Plugin.__name__:
				return obj

	def unregister_plugin(self, id, update=False):
		'''
			Raise:
				IndexError: plugin desen't exists
				LifecycleException: try to valiate plugin lifecycle
		'''

		plugin = self.table.values()[id]
		key = self.table.keys()[id]
		plugin.on_unregister()

		if update:
			module = self.loader.reload_plugin(plugin.__module__)
			self.register_plugin(module, key)
			return

		del self.table[key]

	def print_table(self):
		print 'Plugins installed:'

		fmt = '%15s %15s %15s %25s'
		print fmt % ('Position', 'Name', 'State', 'ID')
		print '-' * 80
		for idx, (k,v) in enumerate(self.table.iteritems()):
			try:
				print fmt % (idx, v, v.state, k)
			except AttributeError, e:
				print fmt % (idx, v.__name__, State.INSTALLED, k)

	def load_plugins(self):
		for module in self.loader.load_plugins():
			self.register_plugin(module)