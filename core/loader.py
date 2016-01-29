from imp import find_module, load_module
from os import listdir, getcwd, sep
from os.path import isfile, join
from state import State
from utils import clear, eliminate

class PluginLoader(object):
	def __init__(self, plugins_dir='plugins', auto_load_plugins=True, plugin_table=None):
		self.plugins_dir = plugins_dir
		self.auto_load_plugins = auto_load_plugins
		self.plugin_table = plugin_table

		if self.auto_load_plugins:
			self.load_plugins()

	def load_plugins(self):
		try:
			path = join(getcwd(), self.plugins_dir)
			files = [clear(f) for f in listdir(path) if eliminate(f)]
			plugins_folder = self.get_plugins_folder()
			
			for file in files:
				module = self.prepare_module(file, plugins_folder)
				self.plugin_table.register_plugin(module)
				
		except ImportError, err:
			print 'ImportError:', err
	
	def get_plugins_folder(self):
		f, filename, description = find_module(self.plugins_dir)
		return filename

	def prepare_module(self, file, plugins_folder):
		f, filename, description = self.get_from_path(file, plugins_folder)
		return self.create_module(file, f, filename, description)
	
	def get_from_path(self, file, folder):
		try:
			return find_module(file, [folder])
		except ImportError, err:
			print 'ImportError:', err
		
	def create_module(self, name, f, filename, description):
		return load_module(name, f, filename, description)
		