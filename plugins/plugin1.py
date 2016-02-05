#from ..core.base import Plugin
from core import Plugin

class A(Plugin):
	def __init__(self, par1="bla"):
		Plugin.__init__(self, "par1","","","","")
		self.par1 = par1

	def call(self, **kwargs):
		print 'hello from plugin 1'
		
	def __str__(self):
		return self.par1