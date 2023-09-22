# Sep 2020

def left_bound(A:list, key:int):
	"""
	Implementation left bound search in binary search.

	:param A: sorted list for search.
	:param key: value for search.
	:return: index the of first element, which smaller then key.
	
	Examples:
	>>> left_bound([1, 2, 3, 4, 4, 4, 5, 6], 4)
	2
	>>> left_bound([1, 2, 3, 4, 4, 4, 5, 6], 1)
	-1
	"""
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] < key:
			left = middle
		else:
			right = middle
	return left

def right_bound(A:list, key:int):
	"""
	Implementation right bound search in binary search.

	:param A: sorted list for search.
	:param key: value for search.
	:return: index the of first element, which larger then key.
	
	Examples:
	>>> right_bound([1, 2, 3, 4, 4, 4, 5, 6], 4)
	6
	>>> right_bound([1, 2, 3, 4, 4, 4, 5, 6], 6)
	8
	"""
	left = -1
	right = len(A)
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] <= key:
			left = middle
		else:
			right = middle
	return right

def binary_search(A:list, key:int):
	"""
	Binary search implementation.
	
	:param A: sorted list for search.
	:param key: value for search.
	:return: tuple with left and right bound of key value.

	Examples:
	>>> binary_search([1, 2, 3, 4], 3)
	(1, 3)
	"""
	return left_bound(A, key), right_bound(A, key)

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)