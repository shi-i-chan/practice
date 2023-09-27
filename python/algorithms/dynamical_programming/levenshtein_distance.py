# Sep 2020

def lev_dis(A:str, B:str):
	"""
	DP Levenshtein distance search implementation.

	:param A: first string.
	:param B: second string.
	:return: Levenshtein distance.
	
	Examples:
	>>> lev_dis("qwer", "qwerty")
	2
	>>> lev_dis("", "qwerty")
	6
	>>> lev_dis("", "")
	0
	"""
	F = [[(i + j) if i*j == 0 else 0 for i in range(len(B) + 1)]
		 for j in range(len(A) + 1)]
	for i in range(1, len(A) + 1):
		for j in range(1, len(B) + 1):
			if A[i - 1] == B[j - 1]:
				F[i][j] = F[i - 1][j - 1]
			else:
				F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
	return F[len(A)][len(B)]

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)