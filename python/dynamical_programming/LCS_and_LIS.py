# Sep 2020

def lcs(A:list, B:list):
	"""
	Dynamic programming implementation of the solution
	of the longest common subsequence (LCS) problem.

	Complexity:
	O(n*m)
	
	:param A: list with first sequence.
	:param B: list with second sequence.
	:return: length of LCS.
	
	Examples:
	>>> lcs([1, 2, 3, 4], [1, 2, 3, 5])
	3
	>>> lcs([1, 2, 3, 4], [4, 2, 3, 5])
	2
	>>> lcs([1, 2, 3, 4], [3, 10, 20, 30])
	1
	>>> lcs([1, 2, 3, 4], [5])
	0
	>>> lcs([], [])
	0
	"""
	F = [[0]*(len(B) + 1) for i in range(len(A) + 1)]
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i - 1] == B[j - 1]:
				F[i][j] = 1 + F[i - 1][j - 1]
			else:
				F[i][j] = max(F[i - 1][j], F[i][j - 1])
	return F[len(A)][len(B)]

def lis(A:list):
	"""
	Dynamic programming implementation of the solution
	of the longest increasing subsequence (LIC) problem.

	:param A: list with the sequance.
	:return: length of the LIS.
	
	Complexity:
	O(N**2)
	
	Examples:
	>>> lis([4, 5, 6, 1, 2])
	3
	>>> lis([4, 5, 6, 7, 10])
	5
	>>> lis([4, 5, 6, 7, 10, 1, 1, 1])
	5
	>>> lis([])
	0
	>>> lis([1])
	1
	"""
	n = len(A)
	if n == 0:
		return 0
	F = [1] + [0]*n
	for i in range(1, n):
		m = 0
		for j in range(0, i):
			if A[i] > A[j]:
				m += 1
		if m >= F[i - 1]:
			F[i] = m + 1
		else:
			F[i] = F[i - 1]
	return F[n - 1]

def lis_with_lcs(A:list):
	"""
	Implementation of the solution of the longest increasing
	subsequence (LIC) problem using LCS.

	:param A: list with the sequance.
	:return: length of the LIS.
	
	Complexity:
	O(N**2)
	
	Examples:
	>>> lis([4, 5, 6, 1, 2])
	3
	>>> lis([4, 5, 6, 7, 10])
	5
	>>> lis([4, 5, 6, 7, 10, 1, 1, 1])
	5
	>>> lis([])
	0
	>>> lis([1])
	1
	"""
	return lcs(A, A.sort())

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)