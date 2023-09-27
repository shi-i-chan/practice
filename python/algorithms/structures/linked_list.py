# Sep 2020

class Node():
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node 
		
	def get_data(self):
		return(self.data)
	
	def get_next(self):
		return(self.next_node)
	
	def set_next(self, new_next):
		self.next_node = new_next
		
class Linked_List():
	def __init__(self):
		self.size = 0
		self.head = Node()
		self.tail = None
	
	def clear(self):
		self.__init__()
	
	def __str__(self):
		if self.head.get_next() != None:
			current_node = self.head.get_next()
			out = 'LinkedList [\n' + str(current_node.get_data()) +'\n'
			while current_node.get_next() != None:
				current_node = current_node.get_next()
				out += str(current_node.data) + '\n'
			return out + ']'
		return 'LinkedList []'
	
	def insert(self, data):
		self.size += 1
		if self.head.get_next() == None:
			self.tail = Node(data)
			self.head.set_next(self.tail)
		else:
			self.tail.set_next(Node(data))
			self.tail = self.tail.get_next()
		print("Insert " + str(data) + ".\n")
			
	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list.")
		print("Found node address:")
		return current  
	
	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list.")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())
		print(str(data) + " deleted.\n")
					  
	def as_list(self):
		current = self.head.get_next()
		alist = []
		while current != None:
			alist.append(current.get_data())
			current = current.get_next()
		print("Get linked list as list.\n")
		return alist
	
	def insert_first(self, data):
		self.size += 1
		if self.head == None:
			self.tail = Node(data)
			self.head.set_next(self.tail)
		else:
			self.head.set_next(Node(data, self.head.get_next()))
		print("Insert " + str(data) + " as first element.\n")
		
				
	def remove_duplicates(self):
		if(self.head.get_next() == None):
			return
		number = current = self.head.get_next()
		while current != None:
			if number.get_data() == current.get_next().get_data():
				current.set_next(current.get_next().get_next())
				if current.get_next() == None:
					number = current = current.get_next()
			else:
				current = current.get_next()
		print("Duplicates deleted.\n")

ll = Linked_List()
ll.insert(5)
ll.insert(10)
ll.insert(5)
print(ll)
print()
print(ll.search(10))
print()
ll.insert_first(22)
print(ll)
print()
ll.delete(22)
print(ll)
print()
ll.remove_duplicates()
print(ll)
print()
print(ll.as_list())