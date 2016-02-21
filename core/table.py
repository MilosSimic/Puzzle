from utils import proxy
from inspect import getmembers, isclass
from base import Plugin
from uuid import uuid1
from excp import LifecycleException
from loader import PluginLoader
from state import state_const

class PluginTable(object):
	def __init__(self, observable, plugins_dir):
		self.table = {}
		self.observable = observable
		self.loader = PluginLoader(plugins_dir, auto_load_plugins=True)

	def activate(self, id):
		'''
		Function that active single plugin

		Args:
			id (int): plugin position in table to activate

		Raises:
			IndexError if plugin doesn't exists
		'''

		plugin = self.table.values()[id]
		if isclass(plugin):
			plugin = plugin()

			key = self.table.keys()[id]
			self.table[key] = plugin

			self.start_plugin(id)
			self.observable.notify(position=id, state='ACTIVE', call="activate")

	def activate_all(self):
		'''
			Funcntion that activate all plugins one by one
		'''

		for k, v in self.table.iteritems():
			if isclass(v):
				self.table[k] = v()
				self.observable.notify(position=id, state='ACTIVE', call="activate_all")

	@proxy
	def get_plugin(self, id):
		'''
			Proxy-Lazy implementatino. Try to get plugin if can.
			If can't, then initialise plugin then return it

			Args:
				id (int): plugin position in table to get

			Returns:
				if plugin is in ACTIVE state then return plugin instance,
				else return plugin info

			Raises:
				AttributeError if plugin is not resolved
				IndexError if plugin doesn't exists
		'''

		plugin = self.table.values()[id]
		
		if plugin.state == State.ACTIVE:
			return plugin
		else:
			return plugin.info()
	
	def start_plugin(self, id):
		'''
		Function that start plugin. Call on_start method from lifecycle of plugin

		Args:
			id (int): plugin position in table to start

		Raises:
			TypeError if plugin is not activated
			IndexError if plugin desen't exists
			LifecycleException if try to valiate lifecycle
		'''

		plugin = self.table.values()[id]
		plugin.state.on_start()
		self.observable.notify(position=id, state='ACTIVE', call="start_plugin")
		
	def stop_plugin(self, id):
		'''
		Function that stop plugin

		Args:
			id (int): plugin position in table to stop

		Raises:
			TypeError if plugin is not activated
			IndexError if plugin desen't exists
			LifecycleException if try to valiate lifecycle
		'''

		plugin = self.table.values()[id]
		plugin.state.on_stop()
		self.observable.notify(position=id, state='STOPPED', call="stop_plugin")
		
	def restart_plugin(self, id):
		'''
		Restart plugin state

		Args:
			id (int): plugin position in table to restart plugin state

		Raises:
			TypeError if plugin is not activated
			IndexError if plugin desen't exists
			LifecycleException if try to valiate lifecycle
		'''

		plugin = self.table.values()[id]
		plugin.state.on_restart()
		self.observable.notify(position=id, state='RESOLVED', call="restart_plugin")

	def register_plugin(self, module, key=None):
		'''
		Register new plugin into plugins table

		Args:
			module (python module): module to be registered
			key (uuid string): key for plugin. If None, new plugin is created, else update plugin is done
		'''
		if not key:
			key = uuid1()

		self.table[key] = self.extract_plugin(module)
		self.observable.notify(position=len(self.table.keys()), state='RESOLVED', call="register_plugin")

	def extract_plugin(self, module):
		'''
		Extract plugin class from module. Plugin class is class that inherite Plugin and override it

		Args:
			module (python module): modue to extract class from

		Returns:
			class that inherite Plugin folder.

		NOTE: only ONE class need to be in file!
		'''

		for name, obj in getmembers(module):
			if isclass(obj) and issubclass(obj, Plugin) and name not in Plugin.__name__:
				return obj

	def unregister_plugin(self, id, update=False):
		'''
			Function that unregister plugin and/or update plugin.

			Args:
				id (int): plugin position in table to unregister/update
				update (bool): optional argumet to tell should plugin update or not

			Raises:
				IndexError: plugin desen't exists
				LifecycleException: try to valiate plugin lifecycle
		'''

		plugin = self.table.values()[id]
		key = self.table.keys()[id]
		plugin.state.on_unregister()
		self.observable.notify(position=id, state='UNINSTALLED', call="unregister_plugin")

		#remove old instance
		self.table[key] = None

		if update:
			module = self.loader.reload_plugin(plugin.__module__)
			self.register_plugin(module, key)
			return

		self.observable.notify(position=id, state=None, call="unregister_plugin")
		#if no update/refresh plugin then delete
		del self.table[key]

	def print_table(self):
		'''
			Print table that contains plugins

			Returns:
				table (list): list of strings taht contains id, key, name, state of plugin
		'''

		table = []
		table.append('Plugins installed:')

		fmt = '%15s %15s %15s %25s'
		table.append(fmt % ('Position', 'Name', 'State', 'ID'))
		table.append('-' * 80)

		for idx, (k,v) in enumerate(self.table.iteritems()):
			try:
				table.append(fmt % (idx, v, v.state, k))
			except AttributeError, e:
				table.append(fmt % (idx, v.__name__, repr(state_const.INSTALLED), k))

		return table

	def load_plugins(self):
		'''
		Register single plugin in plugins table
		'''

		for module in self.loader.load_plugins():
			self.register_plugin(module)