from math import ceil


def solution(s: int, t: int) -> int:
	dist = s * t
	max_s_n = ceil(t / 2)
	for i in range(0, max_s_n):
		if s - 3 * i > 0:
			dist += s - 3 * i
	return dist
