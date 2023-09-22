# Sep 2020

def quicksort(A:list):
	"""
	Hoare sorting implementation.

	Complexity:
	- Best O(nlogn)
	- Average O(nlogn)
	- Worst O(n**2)
	
	:param A: sortable list.
	:return: sorted list A.
	
	Examples:
	>>> quicksort([0, 5, 3, 2, 2])
	[0, 2, 2, 3, 5]
	>>> quicksort([])
	[]
	>>> quicksort([-2, -5, -45])
	[-45, -5, -2]
	>>> quicksort([1])
	[1]
	"""
	if len(A) == 0:
		return []
	if len(A) == 1:
		return A
	barrier = A[0]
	L = []
	M = []
	R = []
	for x in A:
		if x < barrier:
			L.append(x)
		elif x == barrier:
			M.append(x)
		else:
			R.append(x)
		quicksort(L)
		quicksort(R)
		k = 0
		for x in L + M + R:
			A[k] = x
			k += 1
	return A

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)