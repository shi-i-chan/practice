# Sep 2020

def recursive_exponentiation_pure(a:int, n:int):
	"""
	Pure recursive implementation of exponentiation.

	Complexity:
	O(n)
	
	:param a: exponential number.
	:param n: exponent.
	:return: a in degree n.

	Examples:
	>>> recursive_exponentiation_pure(5, 25)
	298023223876953125
	>>> recursive_exponentiation_pure(5, 0)
	1
	>>> recursive_exponentiation_pure(10, 10)
	10000000000
	"""
	if n == 0:
		return 1
	else:
		return recursive_exponentiation_pure(a, n-1)*a

def recursive_exponentiation_optimized(a:int, n:int):
	"""
	Optimized recursive implementation of exponentiation.

	Complexity:
	O(log2(n))

	:param a: exponential number.
	:param n: exponent.
	:return: a in degree n.

	Examples:
	>>> recursive_exponentiation_pure(5, 25)
	298023223876953125
	>>> recursive_exponentiation_pure(5, 0)
	1
	>>> recursive_exponentiation_pure(10, 10)
	10000000000
	"""
	if n == 0:
		return 1
	elif n%2 == 1:
		return recursive_exponentiation_pure(a, n-1)*a
	else:
		return recursive_exponentiation_pure(a*a, n//2)

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)