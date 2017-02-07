
class LifecycleException(Exception):
	def __init__(self, msg):
		#self.msg = msg
		super(Exception, self).__init__(msg)

	def __str__(self):
		return repr(self.message)