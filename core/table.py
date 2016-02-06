from state import State
from inspect import getmembers, isclass
from base import Plugin
from uuid import uuid1

class PluginTable(object):
	def __init__(self):
		self.table = {}

	def activate(self, id):
		return self.table[id]()

	def get_plugin(self, id):
		try:
			plugin = self.table[id]
			if plugin.stanje == State.ACTIVE:
				return plugin
		except AttributeError, e:
			print "plugin must be active"
		
	def start_plugin(self, id):
		self.table[id].on_start()
		
	def stop_plugin(self, id):
		self.table[id].on_stop()
		
	def restart_plugin(self, id):
		self.table[id].on_restart()

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