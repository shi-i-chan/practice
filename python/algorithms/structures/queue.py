# Sep 2020

class queue:
	def __init__(self):
		self.queue = []
	
	def sett(self, element):
		self.queue.append(element)
		
	def gett(self):
		return(self.queue[0])
		
	def remove(self):
		self.queue.pop(0)
		
	def get_len(self):
		return len(self.queue)
		
	def check(self, element):
		if element in self.queue:
			return(0)
		else:
			return(1)

queue = queue()

queue.sett(1)
queue.sett(2)
queue.sett(3)

print(queue.get_len())
queue.remove()
print(queue.get_len())
print(queue.check(1))
print(queue.gett())
