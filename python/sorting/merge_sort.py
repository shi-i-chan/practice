# Sep 2020

def merge_lists(A:list, B:list):
	"""
	Merges two sorted lists to one sorted list.

	:param A: first sorted list.
	:param B: second sorted list.
	:return: sorted list with elements from lists A and B.

	Examples:
	>>> merge_lists([1, 7, 11], [4, 5, 10])
	[1, 4, 5, 7, 10, 11]
	"""
	C = [0] * (len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[k]:
			C[n] = A[i]
			i += 1
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C

def merge_sort(A:list):
	"""
	Merge sort implementation.

	Complexity:
	- Best O(nlogn)
	- Average O(nlogn)
	- Worst O(nlogn)

	:param A: sortable list.
	:return: sorted list A.

	Examples:
	>>> merge_sort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]
	>>> merge_sort([])
	[]
	>>> merge_sort([-2, -5, -45])
	[-45, -5, -2]
	>>> merge_sort([1])
	[1]
	"""
	if len(A) == 0:
		return []
	if len(A) == 1:
		return A
	middle = len(A)//2
	left = [A[i] for i in range(0, middle)]
	right = [A[i] for i in range(middle, len(A))]
	merge_sort(left)
	merge_sort(right)
	C = merge_lists(left, right)
	for i in range(len(C)):
		A[i] = C[i]
	return C

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)