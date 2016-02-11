from core import Puzzle

p = Puzzle()
#p.print_table()

'''a = p.table.get_plugin(0)
a.call()
p.print_table()'''
#p.table.activate_all()
p.print_table()
p.table.activate(0)
print p.table.get_plugin(0)
#p.table.stop_plugin(0)
'''b = p.table.get_plugin(1)

a = p.table.activate(0)
a.on_start()
a.call()'''
#b = b()
#b.call()