# Sep 2020

def tower_of_hanoi(n:int, sourse:list, target:list, auxiliary:list):
	"""
	Recursive mplementation of the Hanoi tower problem.

	:param n > 0: number of rings in sourse.
	:param sourse: list with rings indexes in start rod.
	:param target: list with rings indexes in target rod.
	:param auxiliary: list with rings indexes in auxiliary rod.
	:return: list with rings indexes in target rod.
	
	Examples:
	>>> tower_of_hanoi(3, [3, 2, 1], [], [])
	[3, 2, 1]
	>>> tower_of_hanoi(5, [5, 4, 3, 2, 1], [], [])
	[5, 4, 3, 2, 1]
	>>> tower_of_hanoi(1, [1], [], [])
	[1]
	"""
	if n == 1:
		target.append(sourse.pop())
		return target
	tower_of_hanoi(n - 1, sourse, auxiliary, target)
	target.append(sourse.pop())
	tower_of_hanoi(n - 1, auxiliary, target, sourse)
	return target

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)