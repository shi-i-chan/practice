# Sep 2020

def bubble_sort(array:list):
	"""
	Pure bubble sort.

	:param array: some mutable ordered collection with heterogeneous
	comparable items inside
	:return: the same collection ordered by ascending
	
	Complexity:
	- Best O(n)
	- Average O(n**2)
	- Worst O(n**2)
	
	Examples:
	>>> bubble_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]

	>>> bubble_sort([])
	[]

	>>> bubble_sort([-2, -5, -45])
	[-45, -5, -2]
	"""
	length = len(array)
	for start in range(length):
		for index in range(0, length-start-1):
			if array[index] > array[index+1]:
				array[index], array[index+1] = array[index+1], array[index]
	return array

def optimized_bubble_sort(array:list):
	"""
	Optimazed bubble sort.

	:param array: some mutable ordered collection with heterogeneous
	comparable items inside
	:return: the same collection ordered by ascending
	
	Complexity:
	- Best O(n)
	- Average O(n**2)
	- Worst O(n**2)
	
	Examples:
	>>> bubble_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]

	>>> bubble_sort([])
	[]

	>>> bubble_sort([-2, -5, -45])
	[-45, -5, -2]
	"""
	length = len(array)
	for start in range(length):
		swapped = False
		for index in range(0, length-start-1):
			if array[index] > array[index+1]:
				array[index], array[index+1] = array[index+1], array[index]
				swapped = True
		if swaped == False:
			break

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)