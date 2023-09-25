from math import log

def decompose(number):
	i = 2
	lst = []
	while number >= i * i:
		lst.append(k := int(log(number, i)))
		number -= i ** k
		i += 1
	return [lst, number]
