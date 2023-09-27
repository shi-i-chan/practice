def levenshtein(a: str, b: str) -> int:
	F = [[(i + j) if i*j == 0 else 0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]
	for i in range(1, len(a) + 1):
		for j in range(1, len(b) + 1):
			if a[i - 1] == b[j - 1]:
				F[i][j] = F[i - 1][j - 1]
			else:
				F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
	return F[len(a)][len(b)]
