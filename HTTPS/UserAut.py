class User:
	def __init__(self, username, password):
		self.name = username
		self.password = password
	def __repr__(self):
		return str(self.name) + str(self.password)

