from imp import find_module, load_module
from os import listdir, getcwd, sep
from os.path import isfile, join
from utils import clear, eliminate, PY_EXT

class PluginLoader(object):
	def __init__(self, plugins_dir, auto_load_plugins=False):
		self.plugins_dir = plugins_dir
		self.path = join(getcwd(), self.plugins_dir)

		if auto_load_plugins:
			self.load_plugins()

	def files_generator(self, path):
		for file in listdir(path):
			if isfile(join(path, file)) and eliminate(file):
				yield file

	def load_plugins(self):
		'''
			Throws:
				ImportError : if module or plugins folder don't exists
		'''

		for file in self.files_generator(self.path):
			file, ext = clear(file)
			if PY_EXT in ext:
				yield self.get_from_path(file, self.path)

	def load_plugin(self, path, folder=None):
		if not folder:
			folder = self.path

	def reload_plugin(self, file):
		return self.get_from_path(file, self.path)

	def get_from_path(self, file, folder):
		'''
			Throws:
				ImportError : if module can't be find
		'''

		f, filename, description =  find_module(file, [folder])
		module = self.create_module(file, f, filename, description)
		f.close()

		return module
		
	def create_module(self, name, f, filename, description):
		return load_module(name, f, filename, description)
		