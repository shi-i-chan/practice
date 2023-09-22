# Sep 2020

def check_sorted(A:list, ascending=True):
	"""
	Check list sorting in ascending or descending order.
	
	Complexity:
	O(n)

	:param A: verifiable list.
	:param ascending: True if ascending False if descending.
	:return: True, if list sorted.

	Examples:
	>>> check_sorted([1, 2, 5, 10, 20, 1000])
	True
	>>> check_sorted([20, 11, 9, 5, 0], False)
	True
	>>> check_sorted([11, 20, 30, 15])
	False
	"""
	flag = True
	S = 2*int(ascending)
	for i in range(0, len(A) - 1):
		if S*A[i] > S*A[i + 1]:
			flag = False
			break
	return flag

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)