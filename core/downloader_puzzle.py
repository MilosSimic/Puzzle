import urllib2, os, zipfile
from excp import ValidationException

class PluginDownloader(object):
	'''
		Class that download puzzle pack aka .zip file from internet
		and unpack it and load into puzzle framework.
		archive must contains:
			1) plugin_file.py file with class that inherite Plugin class. Must be just one class!
		and may contains: 
			2) other logic inside some folder/module pur rest of implementation insede this folder/module

		Args:
			plugins_dir (string): Path to plugins folder
	'''
	def __init__(self, plugins_dir):
		self.plugins_dir = plugins_dir

	def transfer_zip_to_py(self, path_to_zip_file):
		'''
			Transfer name of archive to python file. When archive is downloaded and extracted,
			archive is deleted and on top level must be python file that is core of plugin.
			This name is returned, and name MUST be same as archive name!

			Args:
				path_to_zip_file (string): full path to zip archive

			Returns:
				path_to_zip_file (string): path replace .zip to .py in name

			Reises:
				ValidationException if path_to_zip_file doese not contains .zip in name
		'''

		if '.zip' in path_to_zip_file:
			return path_to_zip_file.replace('.zip', '.py')

		raise ValidationException('Not valid puzzle pack!')

	def delete_after_unpack(self, path_to_zip_file):
		'''
			Delete zip archive after extracting it's content

			Args:
				path_to_zip_file (string): full path to .zip file
		'''

		os.remove(path_to_zip_file)

	def unpack_archive(self, path_to_zip_file):
		'''
			Unpack content of zip file to specific plugins_dir folder

			Args:
				path_to_zip_file (string): full path to zip file
		'''

		zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
		zip_ref.extractall(self.plugins_dir)
		zip_ref.close()

	def download_pack(self, url, size=None):
		'''
			Download zip archive that contains files/modules of plugin
			from some url.

			Args:
				url (string): url to .zip archivr-plugin file
				size (int) [optional]: size of the archive

			Returns:
				file_name (string) path to downloaded archive some/path/to/file.zip

		'''

		file_name = url.split('/')[-1]
		file_name = os.sep.join([self.plugins_dir, file_name])

		u = urllib2.urlopen(url)
		with open(file_name, 'wb') as f:
			meta = u.info()

			if not size:
				file_size = int(meta.getheaders("Content-Length")[0])
			else:
				file_size = size

			file_size_dl = 0
			block_sz = 8192
			while True:
				buffer = u.read(block_sz)
				if not buffer:
					break
					
				file_size_dl += len(buffer)
				f.write(buffer)

		return file_name #some/path/to/file.zip

	def download_puzzle_part(self, url):
		'''
			method that wrap not things. Download zip archive then unpack it.
			After that delete archive, and return full path to extracted py file.
			This file MUST inherite Plugin class in order to be loaded into puzzle.

			Args:
				url (string): path to zip archive

			Returns:
				file_name (string): path_to_zip_file (string): path replace .zip to .py in name
		'''


		#download
		zip_file = self.download_pack(url)

		#unzip archive
		self.unpack_archive(zip_file)

		#delete zip archive
		self.delete_after_unpack(zip_file)

		#full path to plugins_dir/pluginname.py
		return self.transfer_zip_to_py(zip_file)

			