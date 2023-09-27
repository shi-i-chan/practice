# Sep 2020 

import numpy as np
import matplotlib.pyplot as plt

def function(x):
	return(x*x*x - 6*x*x + 4)

def swann(center, step=1):
	itter = 0
	left_edge = center - step
	right_edge = center + step
	while not (function(left_edge) >= function(center) <= function(right_edge)):
		if itter == 100000:
			print("Interval not found. Try to change the starting point.")
			return
		if function(left_edge) >= function(center) >= function(right_edge):
			x = right_edge
			right_edge = right_edge + step
		elif function(left_edge) <= function(center) <= function(right_edge):
			center = left_edge
			left_edge -= step
		elif function(left_edge) <= function(center) >= function(right_edge):
			center += step
		left_edge = center - step
		right_edge = center + step
		itter += 1
	return(left_edge, right_edge)

print(swann(100, step=1))