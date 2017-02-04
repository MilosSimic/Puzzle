from core import Puzzle, Plugin
from os.path import isfile, join, getsize
from os import getcwd
import unittest
from core.state import statemachine

# path = join(getcwd(), 'plugins')

# p = Puzzle(plugins_dir=path)

# p.load_plugins()
# p.print_table()

# p.table.resolve_all()
# p.print_table()

# p.table.activate_all()
# p.print_table()

# p.table.stop_plugin(0)
# p.print_table()

# p.table.unregister_plugin(0, False)
# p.print_table()

# p.table.stop_plugin(0)
# p.print_table()

# p.table.restart_plugin(0)
# p.print_table()

class PuzzleTestBasic(unittest.TestCase):

	def setUp(self):
		self.p = Puzzle(plugins_dir=join(getcwd(), 'plugins'))

	def test_creation_puzzle(self):
		self.assertIsNotNone("Creating instance of Puzzle.", self.p)

	def test_table_load(self):
		self.assertIsNotNone("Creating instance of Puzzle.", self.p.table)

	def test_observer_load(self):
		self.assertIsNotNone("Creating instance of Puzzle.", self.p.observable)

	def test_loading_plugins(self):
		self.p.load_plugins()
		self.assertEqual(self.p.table.size(), 2)


class PuzzleTestLifecycle(unittest.TestCase):

	def setUp(self):
		self.p = Puzzle(plugins_dir=join(getcwd(), 'plugins'))

	def test_creation_puzzle(self):
		self.assertIsNotNone("Creating instance of Puzzle.", self.p)

	def test_loading_plugins(self):
		self.p.load_plugins()
		self.assertEqual(self.p.table.size(), 2)

	def test_resolve_state(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		for key, plugin in self.p.table_items():
			self.assertIsInstance(plugin.state, statemachine.Resolved)

	def test_active_state(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		self.p.table.activate_all()
		for key, plugin in self.p.table_items():
			self.assertIsInstance(plugin.state, statemachine.Active)

	def test_stop_plugin(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		self.p.table.activate_all()

		self.p.table.stop_plugin(0)
		plugin = self.p.table.get_plugin(0)
		self.assertIsInstance(plugin.state, statemachine.Stopped)

	def test_restart_plugin(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		self.p.table.activate_all()

		self.p.table.stop_plugin(0)
		self.p.table.restart_plugin(0)
		plugin = self.p.table.get_plugin(0)
		self.assertIsInstance(plugin.state, statemachine.Resolved)

	def test_unregister_no_plugin_refresh(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		self.p.table.activate_all()

		self.p.table.stop_plugin(0)
		self.p.table.unregister_plugin(0, False)
		self.assertEqual(self.p.table.size(), 1)

	def test_unregister_plugin_refresh(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		self.p.table.activate_all()

		self.p.table.stop_plugin(0)
		self.p.table.unregister_plugin(0, True)
		self.assertEqual(self.p.table.size(), 2)

	def test_resolve_plugin_after_refresh(self):
		self.p.load_plugins()
		self.p.table.resolve_all()
		self.p.table.activate_all()

		self.p.table.stop_plugin(0)
		self.p.table.unregister_plugin(0, True)
		self.p.table.resolve(0)

		plugin = self.p.table.get_plugin(0)
		self.assertIsInstance(plugin.state, statemachine.Resolved)


'''
#Test download zip archive with plugin
url = 'file:///Users/milossimic/Desktop/ziptest/plugin3.zip'
ff = '/Users/milossimic/Desktop/ziptest/plugin3.zip'
fsize = getsize(ff)
p.download_puzzle_part(url, fsize)
p.print_table()
'''

# class TestInstalation(unittest.TestCase):
# 	def setUp(self):
# 		self.p = Puzzle(plugins_dir=path)
# 		self.p.load_plugins()

# 	def test_plugins_instalation(self):
# 		for id,(key, plugin) in enumerate(self.p.table.table.iteritems()):
# 			self.assertTrue(issubclass(plugin, Plugin))

# 	def test_load_plugins(self):
# 		self.assertEqual(len(self.p.table.table), 2)

# 	def tearDown(self):
# 		pass
		

if __name__ == '__main__':
	unittest.main()