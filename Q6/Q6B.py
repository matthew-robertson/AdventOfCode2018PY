from collections import defaultdict

points = []

def manhatDist (p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def closest (p1):
	totalDist = 0
	least = [[-1, 99999999999999]]
	for idx, val in enumerate(points):
		totalDist += manhatDist(p1, val)
		if manhatDist(p1, val) < least[0][1]:
			least = [[idx, manhatDist(p1, val)]]
		elif manhatDist(p1, val) == least[0][1]:
			least.append([idx, manhatDist(p1, val)])

	if len(least) == 1:
		return [least[0][0], totalDist]
	else:
		return [-1, totalDist]

least = [999, 999]
greatest = [0  ,  0 ]
with open("input.txt", "r") as ins:
	for line in ins:
		t = line.split(", ")
		points.append([int(t[0]), int(t[1])])
		least[0] = min(least[0], int(t[0]))
		least[1] = min(least[1], int(t[1]))
		greatest[0] = max(greatest[0], int(t[0]))
		greatest[1] = max(greatest[1], int(t[1]))

'''least[0] -= 200
least[1] -= 200
greatest[0] += 200
greatest[1] += 200'''
total = 0
for x in range (least[0], greatest[0]+1):
	for y in range (least[1], greatest[1]+1):
		v = closest([x, y])
		if v[1] < 10000:
			total+=1
			if x == least[0] or x == greatest[0] or y == least[1] or y == greatest[1]:
				print("Danger! Safe on the edge!")


print(total)