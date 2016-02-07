from imp import find_module, load_module
from os import listdir, getcwd, sep
from os.path import isfile, join
from utils import clear, eliminate, PY_EXT

class PluginLoader(object):
	def __init__(self, plugins_dir='plugins', auto_load_plugins=True, plugin_table=None):
		self.plugins_dir = plugins_dir
		self.plugin_table = plugin_table

		if auto_load_plugins:
			self.load_plugins()

	def files(self, path):
		for file in listdir(path):
			if isfile(join(path, file)) and eliminate(file):
				yield file

	def load_plugins(self):
		try:
			path = join(getcwd(), self.plugins_dir)
			for file in self.files(path):
				file, ext = clear(file)
				if PY_EXT in ext:
					self.prepare_module(file, path)
				
		except ImportError, err:
			print 'ImportError:', err

	def prepare_module(self, file, plugins_folder):
		f, filename, description = self.get_from_path(file, plugins_folder)
		module = self.create_module(file, f, filename, description)
		self.plugin_table.register_plugin(module)
	
	def get_from_path(self, file, folder):
		try:
			return find_module(file, [folder])
		except ImportError, err:
			print 'ImportError:', err
		
	def create_module(self, name, f, filename, description):
		return load_module(name, f, filename, description)
		