from table import PluginTable
from callbacks import Observable

class Puzzle(object):
	def __init__(self, plugins_dir='plugins'):
		self.observable = Observable()
		self.table = PluginTable(self.observable, plugins_dir)

	def print_table(self):
		for line in self.table.print_table():
			print line

	def load_plugins(self):
		self.table.load_plugins()