from loader import PluginLoader
from table import PluginTable

class Puzzle(object):
	def __init__(self, plugins_dir='plugins'):
		self.table = PluginTable()
		self.loader = PluginLoader(plugin_table=self.table)

	def print_table(self):
		self.table.print_table()