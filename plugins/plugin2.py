from plugin1 import A

class B(A):
	def __init__(self, par1, par2):
		A.__init__(self, par1)
		self.par2 = par2
		
	def __str__(self):
		return self.par1