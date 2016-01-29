from state import State
from inspect import getmembers, isclass
from base import Plugin

class PluginTable(object):
	def __init__(self):
		self.table = {}

	def get_plugin(self, id):
		return self.table[i]
		
	def start_plugin(self, id):
		self.table[id][State.ACTIVE]
		
	def stop_plugin(self, id):
		self.table[id][State.STOPPED]
		
	def restart_plugin(self, id):
		self.table[id][State.RESOLVED]

	def _is_plugin_child(self, myclass, parentclass):
		return issubclass(myclass, parentclass)

	def register_plugin(self, module):
		for idx, (name, obj) in enumerate(getmembers(module)):
			if isclass(obj) and self._is_plugin_child(obj, Plugin):
				self.table[idx] = (obj, State.RESOLVED)

	def print_table(self):
		print 'Plugins installed:'
		for k,v in self.table.iteritems():
			print k, v