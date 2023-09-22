# Sep 2020

def counting_sort(array:list):
	"""
	Counting sort implementation.
	
	:param array: some mutable ordered collection with heterogeneous
	comparable items inside
	:return: the same collection ordered by ascending
	
	Complexity:
	- Worst O(n + k), where k is the range of the key values.
	
	Examples:
	>>> counting_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]
	>>> counting_sort([])
	[]
	>>> counting_sort([-2, -5, -45])
	[-45, -5, -2]
	"""
	if array == []:
		return []
	
	array_len = len(array)
	array_max = max(array)
	array_min = min(array)

	counting_array_length = array_max + 1 - array_min
	counting_array = [0] * counting_array_length

	for number in array:
		counting_array[number - array_min] += 1
		
	out_array = []

	for index in range(0, len(counting_array)):
		if counting_array[index] != 0:
			for counter in range(0, counting_array[index]):
				out_array.append(index + array_min)
	return out_array

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)