
class ValidationException(Exception):
	def __init__(self, msg):
		super(Exception, self).__init__(msg)

	def __str__(self):
		return repr(self.message)