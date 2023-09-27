# Sep 2020

import math
import numpy as np
import matplotlib.pyplot as plt

def function(x):
	return(x*x*x - 6*x*x + 4)

def golden_section_search(left_edge, right_edge, t_interval):
	X_list, FX_list = ([] for i in range(2))
	interval = math.fabs(right_edge - left_edge)
	left = left_edge + (left_edge - math.sqrt(right_edge))*(right_edge - left_edge)/2
	right = left_edge + right_edge - left
	while interval > t_interval:
		X_list.extend([left, right])
		FX_list.extend([function(left), function(right)])
		if function(left) <= function(right):
			right_edge = right
			right = left
			left = left_edge + right_edge - left
		elif function(left) > function(right):
			left_edge = left
			left = right
			right = left_edge + right_edge - right
		interval = math.fabs(right_edge - left_edge)
	x_point = (left_edge + right_edge) / 2
	fx_point = function((left_edge + right_edge) / 2)
	print("Golden_section_search: \n x* = {0}, f(x*) = {1}, a = {2}, b = {3}, Interval = {4} \n".format(x_point,
																										fx_point,
																										left_edge,
																										right_edge,
																										t_interval))
	return(X_list, FX_list, x_point, fx_point)
	
X_list, FX_list, x_point, fx_point = golden_section_search(3, 5, 0.01)

g_x = np.arange(min(X_list), max(X_list), 0.1)
g_y = [function(i) for i in g_x]

fig, ax = plt.subplots(figsize=(15, 5))   
ax.plot(g_x, g_y)
ax.plot(X_list, FX_list, 'ro')
ax.annotate('minimum', xy=(x_point, fx_point), xytext=(4.1, -27),
				   arrowprops=dict(facecolor='black', shrink=0.05))
#plt.savefig('path.png', dpi=300)
plt.show()