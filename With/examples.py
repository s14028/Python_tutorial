class A:
	def __init__(self, i):
		self.i = i
	def __enter__(self):
		print("Enter.")
	def __exit__(self, type, value, traceBack):
		print("Exit.")

with A(100) as a:
	print("Inside.")
