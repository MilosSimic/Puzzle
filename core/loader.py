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

	def pipeline_generator(self, path=None):
		if not path:
			path = self.path

		return (file for file in listdir(path)) #0

	def registration_plugin_pipeline(self, plugin_register, path=None,):
		c_register = plugin_register() #4
		c_filter_clear = self.clear_filter(c_register) #3
		c_filter_plugin = self.filter_plugins(c_filter_clear) #2
		c_filter_files = self.filter_files(c_filter_plugin) #1

		c_filter_files.next() #1
		c_filter_plugin.next() #2
		c_filter_clear.next() #3
		c_register.next() #4

		for file in self.pipeline_generator(path):
			c_filter_files.send(file)

		c_filter_files.close() #1
		c_filter_plugin.close() #2
		c_filter_clear.close() #3
		c_register.close() #4

	def clear_filter(self, plugin_register):
		while  True:
			file = (yield)
			file, ext = clear(file)
			if PY_EXT in ext:
				plugin_register.send(file)

	def filter_plugins(self, clear_filter):
		while True:
			file = (yield)
			if eliminate(file):
				clear_filter.send(file)

	def filter_files(self, filter_plugins):
		while True:
			file = (yield)
			if isfile(join(self.path, file)):
				filter_plugins.send(file)

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

		return self.get_from_path(path, folder)

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
		