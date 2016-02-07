from loader import PluginLoader
from table import PluginTable
from callbacks import Observable

class Puzzle(object):
	def __init__(self, plugins_dir='plugins'):
		self.observable = Observable()
		self.table = PluginTable(self.observable)
		self.loader = PluginLoader(plugins_dir, self.table)

	def print_table(self):
		self.table.print_table()