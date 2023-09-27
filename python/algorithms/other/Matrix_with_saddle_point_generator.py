# Sep 2020

# Matrix generator with saddle point
import numpy as np
import numpy.random as rnd

def make_matrix(n, m):
	matr = np.zeros((n, m))

	c = rnd.randint(2, 20)
	print("Clear sum:", c, "\n")

	row = rnd.randint(n)
	column = rnd.randint(m)

	matr[row][column] = c
	for i in range(0, m):
		if matr[row][i] == 0:
			matr[row][i] = rnd.randint(c, 20)
	for i in range(0, n):
		if matr[i][column] == 0:
			matr[i][column] = rnd.randint(1, c)
	for i in range(0, n):
		for j in range(0, m):
			if matr[i][j] == 0:
				matr[i][j] = rnd.randint(1, 20)

	print("The matrix:")
	print(matr, "\n")

	def get_max_min(matr):
		lst = []
		for i in matr:
			lst.append(min(i))
		return(max(lst))

	def get_min_max(matr):  
		lst = []
		for i in range(0, m):
			lst.append(max(matr[ :, i]))
		return(min(lst))

	print("Max min = ", get_max_min(matr))
	print("Min max = ", get_min_max(matr))
	
for i in range(0, 5):
	n = rnd.randint(2, 10)
	m = rnd.randint(2, 10)
	print("Matrix ", n, "x", m)
	make_matrix(n, m)
	print("_____________________________")