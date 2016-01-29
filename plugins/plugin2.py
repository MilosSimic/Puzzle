from plugin1 import A

class B(A):
	def __init__(self, par1="bla", par2="bla"):
		A.__init__(self, par1)
		self.par2 = par2

	def activate(self, **kwargs):
		print 'hello from plugin 2'
		
	def __str__(self):
		return self.par1