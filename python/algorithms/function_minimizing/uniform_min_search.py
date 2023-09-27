# Sep 2020

import numpy as np
import matplotlib.pyplot as plt

def function(x):
	return(x*x*x - 6*x*x + 4)

def uniform_search(left_edge, right_edge, n_itter):
	X_list = np.arange(left_edge, right_edge, (right_edge - left_edge)/n_itter)
	FX_list = [function(i) for i in X_list]
	x_point = X_list[FX_list.index(min(FX_list))]
	fx_point = min(FX_list)
	print("Uniform_search: \n x* = {0}, f(x*) = {1}, n = {2} \n".format(x_point,
																		fx_point,
																		n_itter))
	return(X_list, FX_list, x_point, fx_point)
	
X_list, FX_list, x_point, fx_point = uniform_search(3, 5, 10)

g_x = np.arange(min(X_list), max(X_list), 0.1)
g_y = [function(i) for i in g_x]

plt.figure(figsize=(15, 5))	
plt.plot(g_x, g_y)
plt.plot(X_list, FX_list, 'ro')
plt.annotate('minimum', xy=(x_point, fx_point), xytext=(4.25, -25),
				   arrowprops=dict(facecolor='black', shrink=0.05))
#plt.savefig('path.png', dpi=300)
plt.show()