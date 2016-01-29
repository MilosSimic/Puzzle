from core import Puzzle

p = Puzzle()
p.print_table()

if p.table.get_plugin(1):
	p.table.get_plugin(1).activate()

if p.table.get_plugin(0):
	p.table.get_plugin(0).activate()

p.table.start_plugin(1)
p.table.get_plugin(1).activate()

p.print_table()