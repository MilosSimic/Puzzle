from puzzle.core import Plugin

class B(Plugin):
	def __init__(self, par1="bla2"):
		Plugin.__init__(self, name="par2",description="",version="",author="",image=None)
		self.par1 = par1

	def call(self, **kwargs):
		print 'hello from plugin 2'
		
	def __str__(self):
		return self.par1