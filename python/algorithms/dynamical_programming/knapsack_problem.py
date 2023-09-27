# Sep 2020

def knapsack(wt:list, val:list, M:int):
	"""
	DP implementation of solver of the knapsack problem.
	
	:param weigths: increasing list with weigths of the items.
	:param values: increasing list with values of the items.
	:param max: maximum weigth.
	:return: maximum available value.

	Examples:
	>>> knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7)
	9
	>>> knapsack([10, 20, 30], [60, 100, 120], 50)
	220
	"""
	N = len(wt) + 1
	A = [[0]*(M + 1) for i in range(N)]
	for i in range(N):
		for w in range(M + 1):
			if i == 0 or w == 0:
				A[i][w] = 0
			elif wt[i - 1] <= w:
				A[i][w] = max(val[i - 1] + A[i - 1][w - wt[i - 1]], A[i - 1][w])
			else:
				A[i][w] = A[i - 1][w]
	print(A[N - 1][M])

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)