from __future__ import print_function
points = []

def bounding_box_height(points):
	maxy = points[0][1]
	miny = points[0][1]
	for x in points:
		maxy = max(maxy, x[1])
		miny = min(miny, x[1])

	return abs(maxy - miny)

def print_array(points):
	maxy = points[0][1]
	miny = points[0][1]
	maxx = points[0][0]
	minx = points[0][0]

	for x in range(0, len(points)):
		maxy = max(maxy, points[x][1])
		miny = min(miny, points[x][1])
		maxx = max(maxx, points[x][0])
		minx = min(minx, points[x][0])

	for y in range(0, maxy-miny+1):
		for x in range(0, maxx - minx+1):
			if [x+minx, y+miny] in points:
				print('#', end='')
			else:
				print('.', end='')
		print('')

	return 0

minsetup = [99999999999, 0]
with open("input.txt", "r") as ins:
	for line in ins:
		points.append([int(line[10:16]), int(line[18:24]), int(line[36:38]), int(line[40:42])])
	minsetup = [bounding_box_height(points), points]
	for x in range(1, 11000):
		for y in range(0, len(points)):
			points[y][0] += points[y][2]
			points[y][1] += points[y][3]
		nh = bounding_box_height(points)
		if nh < minsetup[0]:
			minsetup = [nh, [[i[0], i[1]] for i in points]]
			print(x)

	print (minsetup[0])
	print_array(minsetup[1])
	