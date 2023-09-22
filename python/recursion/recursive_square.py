# Sep 2020

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

img = Image.new("RGB", (510, 510), "gray")
img_draw = ImageDraw.Draw(img)

def recursive_square(A, B, C, D, deep=10, alpha=0.1):
	"""
	Implement recurhison with drawing squares.

	:param A, B, C, D: tuples with cube the coordinates of the angles of the square.
	:param deep: deep of recursion.
	:param alpha: multiplier for shifting the corners of the square.
	"""
	if deep < 1:
		return
	points = [A, B, C, D]
	img_draw.polygon(points)
	A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
	B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
	C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
	D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
	recursive_square(A1, B1, C1, D1, deep-1)
		
recursive_square((10, 10), (500, 10), (500, 500), (10, 500), deep=75, alpha=0.09)
plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.show()