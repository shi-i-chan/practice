# Sep 2020

def naive_ps(text:str, pat:str):
	"""
	Naive pattern searching algorithm implementation.
 
	Complexity:
	O(n*m)

	:param text: the text.
	:param pat: the pattern.
	:return: list with indexes of the beginning of the found patterns.
	
	Examples:
	>>> naive_ps("aaa", "a")
	[0, 1, 2]
	"""
	N = len(text)
	M = len(pat)
	indexes = []
	for i in range(N - M + 1):
		j = 0
		while j < M:
			if text[i + j] != pat[j]:
				break
			j += 1
		if j == M:
			indexes.append(i)
	return indexes


# It's working right???
def opt_naive_ps(text:str, pat:str):
	"""
	Optimazed naive pattern searching algorithm implementation.
	All characters of pattern must be different.

	:param text: the text.
	:param pat: the pattern.
	:return: list with indexes of the beginning of the found patterns.
	
	Examples:
	>>> naive_ps("ABCEABCDABCEABCD", "ABCD")
	[4, 12]
	"""
	N = len(text)
	M = len(pat)
	i = 0
	indexes = []
	while i <= N - M:
		for j in range(M):
			if txt[i - 1] != pat[j]:
				break
			j += 1  
		if j == M:
			indexes.append(i)
			i = i + M
		elif j == 0:
			i += 1
		else:
			i = i + j
	return indexes

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)