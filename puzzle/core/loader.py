from imp import find_module, load_module
from os import listdir, getcwd, sep
from os.path import isfile, join
from utils import clear, eliminate, PY_EXT

INIT_FILE = '__init__.py'

class PluginLoader(object):
	'''
		Class that do work on loading plugins from specific folder.

		Args:
			plugins_dir (string): path to specific plugin folder
			auto_load_plugins (Optional [bool]): doese the plugin folder load plugins authomatic
	'''

	def __init__(self, plugins_dir, auto_load_plugins=False):
		self.path = self.prepare_plugins_dir(plugins_dir)

		if auto_load_plugins:
			self.load_plugins()

	def prepare_plugins_dir(self, plugins_dir):
		'''
			Test if given path contains __init__.py file. If not,
			then create file and return path, else just return path.

			Args:
				plugins_dir (string): path to test

			Returns:
				plugins_dir (string): path to plugins dir
		'''

		if "__init__.py" not in listdir(plugins_dir):
			file = join(plugins_dir, "__init__.py")
			with open(file, 'w') as f:
				pass
		
		return plugins_dir

	def files_generator(self, path):
		'''
			Generator function, that will generate file by file

			Args:
				path (string): path from where to read
		'''

		for file in listdir(path):
			if isfile(join(path, file)) and eliminate(file):
				yield file

	def load_plugins(self):
		'''
			Function that load plugins from specific path. Generator function load one at the time.

			Raises:
				ImportError : if module or plugins folder don't exists
		'''

		for file in self.files_generator(self.path):
			file, ext = clear(file)
			if PY_EXT in ext:
				yield self.get_from_path(file, self.path)

	def load_plugin(self, file, folder=None):
		'''
			Load single plugin from some specificic folder.

			Args:
				file (string): filename of single plugin to load
				file (string): folder name where to look for plugins.

			Returns:
				module (module): return module that contains class that inherate Plugin class
		'''

		if not folder:
			folder = self.path

		return self.get_from_path(file, folder)

	def reload_plugin(self, file):
		return self.get_from_path(file, self.path)

	def get_from_path(self, file, folder):
		'''
			Function that loads specific file from specific folder.

			Args:
				file (string): name of file to load
				folder (string): name of folder where to look for plugin

			Returns:
				module (python module): loaded python module

			Raises:
				ImportError : if module can't be find
		'''

		f, filename, description = find_module(file, [folder])
		module = self.create_module(file, f, filename, description)
		f.close()

		return module
		
	def create_module(self, name, f, filename, description):
		'''
			Load single module.

			name (string): name of module
			f (file): file of single module
			filename (string): filename of module
			description (string): description of module

			Returns:
				loaded python module
		'''

		return load_module(name, f, filename, description)
		