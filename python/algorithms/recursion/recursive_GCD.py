# Sep 2020

def gcd_pure(a:int, b:int):
	"""
	Pure implementation of Euclid's algorithm
	for obtaining greatest common divisor.

	:param a: the first number.
	:param b: the second number.
	:return: the greatest common divisor.

	Examples:
	>>> gcd_pure(184, 1288)
	184
	>>> gcd_pure(156, 16)
	4
	"""
	if a == b:
		return a
	elif a > b:
		return gcd_pure(a-b, b)
	else:
		return gcd_pure(a, b-a)

def gcd_optimized(a:int, b:int):
	"""
	Optimized implementation of Euclid's algorithm
	for obtaining greatest common divisor.

	:param a: the first number.
	:param b: the second number.
	:return: the greatest common divisor.

	Examples:
	>>> gcd_optimized(184, 1288)
	184
	>>> gcd_optimized(156, 16)
	4
	"""
	return a if b == 0 else gcd_optimized(b, a%b)

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)