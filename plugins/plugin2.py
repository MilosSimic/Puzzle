from core import Plugin

class B(Plugin):
	def __init__(self, par1="bla2"):
		Plugin.__init__(self, "par1","","","","")
		self.par1 = par1

	def call(self, **kwargs):
		print 'hello from plugin 2'
		
	def __str__(self):
		return self.par1