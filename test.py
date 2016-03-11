from core import Puzzle, Plugin
from os.path import isfile, join, getsize
from os import getcwd
import unittest
from core.state import statemachine

'''
path = join(getcwd(), 'plugins')

p = Puzzle(plugins_dir=path)

p.load_plugins()
p.print_table()
p.table.activate_all()
p.table.unregister_plugin(0, True)
p.print_table()
p.table.start_plugin(1)
p.print_table()
p.table.stop_plugin(1)
p.print_table()
p.table.restart_plugin(1)
p.print_table()
'''

'''
#Test download zip archive with plugin
url = 'file:///Users/milossimic/Desktop/ziptest/plugin3.zip'
ff = '/Users/milossimic/Desktop/ziptest/plugin3.zip'
fsize = getsize(ff)
p.download_puzzle_part(url, fsize)
p.print_table()
'''

path = join(getcwd(), 'plugins')

class TestPuzzleCreation(unittest.TestCase):

	def setUp(self):
		self.p = Puzzle(plugins_dir=path)
		self.p.load_plugins()
		self.p.table.activate_all()


	def test_creation_puzzle(self):
		self.assertIsNotNone("Creating instance of Puzzle.", self.p)

	def test_plugins_states_RESOLVED(self):
		for key, plugin in self.p.table.table.iteritems():
			self.assertIsInstance(plugin.state, statemachine.Resolved)

	def test_unregister_plugin(self):
		self.p.table.unregister_plugin(0)
		self.assertEqual(len(self.p.table.table), 1)


	def tearDown(self):
		pass

class TestLifecycle(unittest.TestCase):

	def setUp(self):
		self.p = Puzzle(plugins_dir=path)
		self.p.load_plugins()
		self.p.table.activate_all()

	def test_start_plugin(self):
		self.p.table.start_plugin(1)
		plugin = self.p.table.get_plugin(1)
		self.assertIsInstance(plugin.state, statemachine.Active)

	def test_stop_plugin(self):
		self.p.table.start_plugin(1)
		self.p.table.stop_plugin(1)
		plugin = self.p.table.get_plugin(1)
		self.assertIsInstance(plugin.state, statemachine.Stopped)

	def test_restart_plugin(self):
		self.p.table.start_plugin(1)
		self.p.table.stop_plugin(1)
		self.p.table.restart_plugin(1)
		plugin = self.p.table.get_plugin(1)
		self.assertIsInstance(plugin.state, statemachine.Resolved)

	def tearDown(self):
		pass

class TestInstalation(unittest.TestCase):
	def setUp(self):
		self.p = Puzzle(plugins_dir=path)
		self.p.load_plugins()

	def test_plugins_instalation(self):
		for id,(key, plugin) in enumerate(self.p.table.table.iteritems()):
			self.assertTrue(issubclass(plugin, Plugin))

	def test_load_plugins(self):
		self.assertEqual(len(self.p.table.table), 2)

	def tearDown(self):
		pass
		

if __name__ == '__main__':
	unittest.main()