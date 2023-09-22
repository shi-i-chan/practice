# Sep 2020

def binary_generator(M:int, prefix=""):
	"""
	Recursive sequence generator with leading zeros in a
	binary numeral system of length m.

	:param M: length of sequance.
	:param prefix: string with ordered sequence.
	"""
	if M == 0:
		print(prefix)
		return
	binary_generator(M - 1, prefix + "0")
	binary_generator(M - 1, prefix + "1")

def number_generator(N:int, M:int, prefix=None):
	"""
	Recursive sequence generator with leading zeros in a
	n-th numeral system of length m.

	:param N: base of numeral system.
	:param M: length of sequance.
	:param prefix: list with ordered sequence.
	"""
	if M == 0:
		print(prefix)
		return
	prefix = prefix or []
	for digit in range(N):
		prefix.append(digit)
		number_generator(N, M-1, prefix)
		prefix.pop()

def permutation_generator(N:int, M:int=-1, prefix=None):
	"""
	Recursive generator of permutations of N numbers in M positions.

	:param N > M: base of numeral system.
	:param M: length of sequance.
	:param prefix: list with ordered sequence.
	"""
	M = N if M == -1 else M
	prefix = prefix or []
	if M == 0:
		print(prefix)
		return
	for number in range(1, N+1):
		if number in prefix:
			continue
		prefix.append(number)
		permutation_generator(N, M-1, prefix)
		prefix.pop()

binary_generator(3)
print()
number_generator(2, 3)
print()
permutation_generator(3, 3)