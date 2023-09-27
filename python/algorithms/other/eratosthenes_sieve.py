# Sep 2020

def eratosthenes_sieve(N:int):
	"""
	Sieve of Eratosthenes algorithm. Determines whether a numer from
	an array from 0 to N is prime or compound.

	Complexity:
	O(nlog(logn))

	:param N: the maximum number from the sequence to check.
	:return A: array with prime numpbers

	Examples:
	>>> eratosthenes_sieve(10)
	[2, 3, 5, 7]
	>>> eratosthenes_sieve(20)
	[2, 3, 5, 7, 11, 13, 17, 19]
	"""
	A = [True]*N
	A[0] = A[1] = False
	for step in range(2, N):
		if A[step]:
			for itter in range(2*step, N, step):
				A[itter] = False
	array = []
	for i in range(N):
		if A[i]:
			array.append(i)
	return array

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)