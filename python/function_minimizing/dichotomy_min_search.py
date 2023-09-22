# Sep 2020

import math
import numpy as np
import matplotlib.pyplot as plt

def function(x):
	return(x*x*x - 6*x*x + 4)

def dichotomy_search(left_edge, right_edge, t_interval):
	X_list, FX_list = ([] for i in range(2))
	interval = math.fabs(right_edge - left_edge)
	mean = (left_edge + right_edge)/2
	while interval > t_interval:
		left = left_edge + interval / 4
		right = right_edge - interval / 4
		X_list.extend([left, right])
		FX_list.extend([function(left), function(right)])
		if function(left) < function(mean):
			right_edge = mean
			mean = left
		elif function(left) >= function(mean):
			if function(right) < function(mean):
				left_edge = mean
				mean = right
			elif function(right) >= function(mean):
				left_edge = left
				right_edge = right
		interval = math.fabs(right_edge - left_edge)
	x_point = (left_edge + right_edge)/2
	fx_point = function((left_edge + right_edge)/2)
	print("Dichotomy_search: \n x* = {0}, f(x*) = {1}, a = {2}, b = {3}, Interval = {4} \n".format(x_point,
																								   fx_point,
																								   left_edge,
																								   right_edge,
																								   interval))
	return(X_list, FX_list, x_point, fx_point)
	
X_list, FX_list, x_point, fx_point = dichotomy_search(3, 5, 0.001)

g_x = np.arange(min(X_list), max(X_list), 0.1)
g_y = [function(i) for i in g_x]

plt.figure(figsize=(15, 5))	
plt.plot(g_x, g_y)
plt.plot(X_list, FX_list, 'ro')
plt.annotate('minimum', xy=(x_point, fx_point), xytext=(4.25, -26.5),
				   arrowprops=dict(facecolor='black', shrink=0.05))
#plt.savefig('path.png', dpi=300)
plt.show()