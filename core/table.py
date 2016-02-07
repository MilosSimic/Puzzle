from utils import State
from inspect import getmembers, isclass
from base import Plugin
from uuid import uuid1

class PluginTable(object):
	def __init__(self, observable):
		self.table = {}
		self.observable = observable

	def activate(self, id):
		plugin = self.table.values()[id]
		if isclass(plugin):
			plugin = plugin()

			key = self.table.keys()[id]
			self.table[key] = plugin

			plugin.on_start()

		return plugin

	def activate_all(self):
		for k, v in self.table.iteritems():
			self.table[k] = v()

	def get_plugin(self, id):
		plugin = self.activate(id)
		try:
			if plugin.state == State.ACTIVE:
				return plugin
		except AttributeError, e:
			print "plugin must be active"
		
	def start_plugin(self, id):
		self.table.values()[id].on_start()
		self.observable.notify(id=id, state=State.ACTIVE, call="on_start")
		
	def stop_plugin(self, id):
		self.table.values()[id].on_stop()
		self.observable.notify(id=id, state=State.STOPPED, call="on_start")
		
	def restart_plugin(self, id):
		self.table.values()[id].on_restart()
		self.observable.notify(id=id, state=State.RESOLVED, call="on_start")

	def register_plugin(self, module):
		for name, obj in getmembers(module):
			if isclass(obj) and issubclass(obj, Plugin) and name != Plugin.__name__:
				self.table[uuid1()] = obj

	def print_table(self):
		print 'Plugins installed:'

		fmt = '%10s %30s %20s'
		print fmt % ('Position', 'ID', 'Name')
		print '-' * 70
		for idx, (k,v) in enumerate(self.table.iteritems()):
			print fmt % (idx, k, v)