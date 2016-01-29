class Plugin(object):
	def __init__(self, name, description, version, author, id, image=None):
		self.name = name
		self.description = description
		self.version = version
		self.author = author
		self.id = id
		self.image = image
		
	def activate(self, **kwargs):
		pass