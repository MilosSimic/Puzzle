from puzzle.core import Puzzle, Plugin
from os.path import isfile, join, getsize
from os import getcwd
from puzzle.core.state import statemachine

path = join(getcwd(), 'puzzle/plugins')
p = Puzzle(plugins_dir=path)

p.load_plugins()
p.print_table()

p.table.resolve_all()
p.print_table()

p.table.activate_all()
p.print_table()

p.table.stop_plugin(0)
p.print_table()

p.table.unregister_plugin(0, False)
p.print_table()

p.table.stop_plugin(0)
p.print_table()

p.table.restart_plugin(0)
p.print_table()

# url = 'file:///Users/milossimic/Desktop/plugin3.zip'
# ff = '/Users/milossimic/Desktop/plugin3.zip'

# fsize = getsize(ff)
# p.download_puzzle_part(url)
# p.print_table()