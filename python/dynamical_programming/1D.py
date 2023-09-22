# Sep 2020

def jumps(n:int):
	"""
	Jumping task implementation with jumps length = 1 and 2 cells.

	:param n > 1: number of cell for jumping.
	:retur: number of options for reaching the cell.
	
	Examples:
	>>> jumps(3)
	2
	>>> jumps(2)
	1
	"""
	A = [0, 1] + [0]*n
	for i in range(2, n + 1):
		A[i] = A[i - 1] + A[i - 2]
	return A[n]

def jumps_with_obstacles(n:int, allowed:list):
	"""
	Jumping task implementation with jumps length = 1 and 2
	and 3 cells. And with blocked cells.

	:param n > 1: number of cell for jumping.
	:param allowed: boolean values. allowed[i] == False, if
	cell[i] is unavailable to jump.
	:retur: number of options for reaching the cell.
	
	Examples:
	>>> jumps_with_obstacles(3, [False, False, True, True])
	2
	>>> jumps_with_obstacles(3, [False, False, False, True])
	1
	>>> jumps_with_obstacles(3, [False, False, True, False])
	0
	>>> jumps_with_obstacles(1, [False, False, True, False])
	1
	>>> jumps_with_obstacles(2, [False, False, True, False])
	1
	"""
	A = [0, 1, int(allowed[2])] + [0]*(n - 2)
	for i in range(3, n + 1):
		if allowed[i]:
			A[i] = A[i - 1] + A[i - 2] + A[i - 3]
	return A[n]

def jumps_with_prices(n:int, prices:list):
	"""
	Jumping task implementation with jumps length = 1 and 2 cells.
	And with the price of visiting cells.

	:param n > 1: number of cell for jumping.
	:param prices: cell visit prices.
	:retur: minimum cost of reaching the cell.
	
	Examples:
	>>> jumps_with_prices(3, [0, 1, 2, 5])
	6
	>>> jumps_with_prices(4, [0, 1, 2, 5, 1])
	4
	>>> jumps_with_prices(1, [0, 4, 2, 5, 1])
	4
	>>> jumps_with_prices(2, [0, 4, 2, 5, 1])
	6
	"""
	A = [None, prices[1], prices[1] + prices[2]] + [0]*(n - 2)
	for i in range(3, n + 1):
		A[i] = prices[i] + min(A[i - 1], A[i - 2])
	return A[n]

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)