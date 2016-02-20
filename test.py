from core import Puzzle

p = Puzzle()

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