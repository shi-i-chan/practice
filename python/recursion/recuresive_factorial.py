# Sep 2020

def factorial(n:int):
	"""
	Recursive implementation of obtaining factorial.

	:param n: the number for obtaining factorial.
	:return: factorial for number n.

	Examples:
	>>> factorial(10)
	3628800
	>>> factorial(0)
	1
	>>> factorial(5)
	120
	"""
	assert n >= 0, "Factorial not defined! Enter a number greater than zero."
	if n == 0:
		return 1
	return factorial(n-1)*n

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)