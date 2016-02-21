from core import Puzzle
from datetime import datetime

p = Puzzle()

dt1 = datetime.now()
p.table.pipeline()
dt2 = datetime.now()

print dt2 - dt1

p.table.activate_all()
p.table.unregister_all_plugins()

dt1 = datetime.now()
p.load_plugins()
dt2 = datetime.now()

print dt2 - dt1

p.table.activate_all()
p.table.unregister_all_plugins()


'''p.print_table()
p.table.activate_all()
p.print_table()
p.table.unregister_all_plugins()
p.print_table()'''

'''
p.load_plugins()
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