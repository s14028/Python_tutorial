class A:
	def __iadd__(self, other):
		print("Inside.")
	
	def someMethod(self):
		pass

a = A()

a += 1
a.someMethod() #a is none because we didn't returned self in __iadd__(self, other).
