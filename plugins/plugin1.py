from puzzle.core import Plugin
from time import sleep

class A(Plugin):
	def __init__(self, par1="bla1"):
		Plugin.__init__(self, name="par1",description="",version="",author="",image=None)
		self.par1 = par1
		#sleep(3)

	def call(self, **kwargs):
		print 'hello from plugin 1'
		
	def __str__(self):
		return self.par1