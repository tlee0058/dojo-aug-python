#modify MathDojo to accept integers, lists, AND tuples
class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, *args):
		for val in args:
			if type(val) is int:
				self.result += val
			elif type(val) is list:
				self.result += sum(val)
			elif type(val) is tuple:
				self.result += sum(val)
		return self
	def subtract(self, *args):
		for val in args:
			if type(val) is int:
				self.result -= val
			elif type(val) is list:
				self.result -= sum(val)
			elif type(val) is tuple:
				self.result -= sum(val)
		return self

#test class methods with md instance
md = MathDojo() 
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result