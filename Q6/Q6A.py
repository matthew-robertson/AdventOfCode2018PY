from collections import defaultdict

points = []

def manhatDist (p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def closest (p1):
	least = [[-1, 99999999999999]]
	for idx, val in enumerate(points):
		if manhatDist(p1, val) < least[0][1]:
			least = [[idx, manhatDist(p1, val)]]
		elif manhatDist(p1, val) == least[0][1]:
			least.append([idx, manhatDist(p1, val)])

	if len(least) == 1:
		return least[0][0]
	else:
		return -1

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

grid = [[0 for y in range(least[1], greatest[1]+1)] for x in range(least[0], greatest[0]+1)]
areaTally = defaultdict(int)
for x in range (least[0], greatest[0]+1):
	for y in range (least[1], greatest[1]+1):
		v = closest([x, y])
		grid[x-least[0]][y-least[1]] = v
		areaTally[v] += 1

areaTally.pop(-1, None)

for x in range(0, len(grid)):
	areaTally.pop(grid[x][0], None)
	areaTally.pop(grid[x][-1], None)

for x in range(0, len(grid[0])):
	areaTally.pop(grid[0][x], None)
	areaTally.pop(grid[-1][x], None)

print(max(areaTally.values()))