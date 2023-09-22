# Sep 2020

def selection_sort(array:list):
	"""
	Selection sort implementation.
	
	:param array: some mutable ordered collection with heterogeneous
	comparable items inside
	:return: the same collection ordered by ascending
	
	Complexity:
	- Worst O(n**2)
	- Average O(n**2)
	- Best O(n**2)
	Examples:
	>>> selection_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]
	>>> selection_sort([])
	[]
	>>> selection_sort([-2, -5, -45])
	[-45, -5, -2]
	"""
	length = len(array)
	for position in range(0, length-1):
		for key in range(position+1, length):
			if array[key] < array[position]:
				array[key], array[position] = array[position], array[key]
	return array

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)