# Sep 2020

import numpy as np

matrix = np.array([
    [0, 3, 1, 8, 1, 5, 3, 2],
    [4, 1, 2, 4, 7, 9, -3, 4],
    [2, 0, 3, 11, 6, 8, 8, 1],
    [0, 3, 3, 1, 6, 9, 4, 7],
    [4, 6, -2, 1, 9, 4, 4, 1]
])

rows, columns = matrix.shape

first = matrix[0]
second = matrix[:, 0]


first_strat = np.zeros(rows)
first_strat[0] = 1
second_strat = np.zeros(columns)
second_strat[0] = 1

print("Brown-Robinson Iterative Method \n")
print("Matrix:\n", matrix)

print("\nIterations:\n" + str(1).ljust(4),
      str(1).ljust(2),
      str(first).ljust(40),
      str(1).ljust(2),
      str(second).ljust(40))

start_itter = 2
n_itter = 20
for i in range(n_itter - 1):
    first_strat[second.tolist().index(max(second))] += 1
    fir = second.tolist().index(max(second))
    first = np.sum([first, matrix[second.tolist().index(max(second))]], axis=0)
    
    second_strat[first.tolist().index(min(first))] += 1
    sec = first.tolist().index(min(first))
    second = np.sum([second, matrix[:, first.tolist().index(min(first))]], axis=0)
    
    print(str(start_itter).ljust(4), str(fir + 1).ljust(2), str(first).ljust(40), str(sec + 1).ljust(2), str(second).ljust(40))
    start_itter += 1

print(("\nV_min = {0}" + 
      "\nV_max = {1}" + 
      "\nV_mean = {2}\n").format(str(min(first) / n_itter).ljust(10),
                                str(max(second) / n_itter).ljust(10),
                                str((max(first) + min(second)) / (n_itter*2)).ljust(10)
                               ))

print(("First player strategies: {0}" +
      "\nSecond player strategies: {1}").format([i / n_itter for i in first_strat],
                                               [j / n_itter for j in second_strat]
                                              ))