# Sep 2020

def king_steps_v1(N:int, M:int):
	"""
	Emplementation of the search algorithm for the number of options
	for reaching the cell with the king, if possible move down and to the right.

	Filling the array by rows.
	
	:param N > 0: row number of the desired cell.
	:param M > 0: column number of the desired cell.
	:return: number of options of the reaching the cell.
	
	Examples:
	>>> king_steps_v1(2, 2)
	2
	>>> king_steps_v1(3, 2)
	3
	>>> king_steps_v1(2, 3)
	3
	>>> king_steps_v1(1, 1)
	1
	"""
	A = [[0]*(M + 1) for k in range(N + 1)]
	A[1][1] = 1
	for i in range(1, N + 1):
		for j in range(1, M + 1):
			if A[i][j] == 0:
				A[i][j] = A[i - 1][j] + A[i][j - 1]
	return A[N][M]

def king_steps_v2(N:int, M:int):
	"""
	Emplementation of the search algorithm for the number of options
	for reaching the cell with the king, if possible move down and to the right.	

	Filling the array by columns.
	
	:param N > 0: row number of the desired cell.
	:param M > 0: column number of the desired cell.
	:return: number of options of the reaching the cell.
	
	Examples:
	>>> king_steps_v2(2, 2)
	2
	>>> king_steps_v2(3, 2)
	3
	>>> king_steps_v2(2, 3)
	3
	>>> king_steps_v2(1, 1)
	1
	"""
	A = [[0]*(M + 1) for k in range(N + 1)]
	A[1][1] = 1
	for j in range(1, M + 1):
		for i in range(1, N + 1):
			if A[i][j] == 0:
				A[i][j] = A[i - 1][j] + A[i][j - 1]
	return A[N][M]
# Need to add a parallel implementation.

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)