# Sep 2020

def insertion_sort(array:list):
	"""
	Insertion sort implementation.

	:param array: some mutable ordered collection with heterogeneous
	comparable items inside
	:return: the same collection ordered by ascending
	
	Complexity:
	- Worst O(n**2)
	- Average O(n**2)
	- Best O(n)

	Examples:
	>>> insertion_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]
	>>> insertion_sort([])
	[]
	>>> insertion_sort([-2, -5, -45])
	[-45, -5, -2]
	"""
	for index in range(1, len(array)):
		position = index
		while position > 0 and array[position-1] > array[position]:
			array[position], array[position-1] = array[position-1], array[position]
			position -= 1
	return array

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)