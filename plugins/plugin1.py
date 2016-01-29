#from ..core.base import Plugin
from core import Plugin

class A(Plugin):
	def __init__(self, par1):
		self.par1 = par1
		
	def __str__(self):
		return self.par1