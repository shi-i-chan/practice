# Sep 2020

class Stack:
	"""
	Examples:
	>>> my_stack = Stack(1); my_stack.push(10);
	>>> len(my_stack.alist)
	1
	>>> my_stack.peek()
	10
	>>> my_stack.pop()
	10
	>>> len(my_stack.alist)
	0
	"""
	def __init__(self, size=100):
		self.size = size
		self.alist = []
		
	def push(self, data):
		if len(self.alist) < self.size:
			self.alist.append(data)
		else:
		   raise Exception("Stack is oveflow")
	
	def pop(self):
		if len(self.alist) != 0:
			return self.alist.pop()
		else:
			raise Exception("Stack is empty")
			
	def peek(self):
		if len(self.alist) != 0:
			return self.alist[-1]
		else:
			raise Exception("Stack is empty")
			
	def show(self):
		print("Stack:")
		for i in reversed(self.alist):
			print(i)

	def is_empty(self):
		return len(self.alist) == 0
	
	def clean(self):
		self.alist = []

def check_braces_correct(braces:str, stack:object):
	"""
	Examples:
	>>> check_braces_correct("[(()())]([])", Stack())
	True
	>>> check_braces_correct("[(])", Stack())
	False
	"""
	for brace in braces:
		if brace not in "()[]":
			continue
		if brace in "([":
			stack.push(brace)
		else:
			assert brace in ")]", "Error"
			if stack.is_empty():
				return False
			left = stack.pop()
			if left == "(":
				right = ")"
			elif left == "[":
				right = "]"
			if right != brace:
				return False
	return stack.is_empty()

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)