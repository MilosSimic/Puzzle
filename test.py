from core import Puzzle
from os.path import isfile, join, getsize
from os import getcwd

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
#Test download zip archive with plugin
url = 'file:///Users/milossimic/Desktop/ziptest/plugin3.zip'
ff = '/Users/milossimic/Desktop/ziptest/plugin3.zip'
fsize = getsize(ff)
p.download_puzzle_part(url, fsize)
p.print_table()
'''