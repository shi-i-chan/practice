# Sep 2020

def recursive_fib(n:int):
	"""
	Recursive implementation of Fibonacci numbers.

	Complexity:
	O(recursive_fib(n)) # Exponentially.

	:param n >= 0: number of Fibonacci number. :)
	:return: Fibonacci number with number n. :0
	
	Examples:
	>>> recursive_fib(9)
	34
	>>> recursive_fib(0)
	0
	>>> recursive_fib(1)
	1
	>>> recursive_fib(2)
	1
	"""
	if n <= 1:
		return n
	else:
		return recursive_fib(n - 1) + recursive_fib(n - 2)

def dp_fib(n:int):
	"""
	Dynamic programming implementation of Fibonacci nymbers.

	:param n >= 0: number of Fibonacci number. :)
	:return: Fibonacci number with number n. :0

	Complexity:
	O(n)
	
	Examples:
	>>> dp_fib(9)
	34
	>>> recursive_fib(0)
	0
	>>> recursive_fib(1)
	1
	>>> recursive_fib(2)
	1
	"""
	if n <= 1:
		return n
	A = [0, 1] + [0]*(n - 1)
	for i in range(2, n + 1):
		A[i] = A[i-1] + A[i-2]
	return A[n]

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)