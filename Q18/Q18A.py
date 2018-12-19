from __future__ import print_function
def countTiles(grid):
	lC = 0
	tC = 0
	for y in grid:
		for x in y:
			if x == '#':
				lC += 1
			elif x == '|':
				tC += 1
	return [lC, tC]


def getNewVal(x, y, grid):
	currentTile = grid[y][x]
	lC = 0
	tC = 0

	for y2 in range(max(0, y-1), min(len(grid), y+2)):
		for x2 in range(max(0, x-1), min(len(grid[0]), x+2)):
			if x2 == x and y2 == y:
				continue
			
			char = grid[y2][x2]
			if char == '#':
				lC += 1
			elif char == '|':
				tC += 1
	
	if currentTile == '.' and tC >= 3:
		return '|'
	elif currentTile == '|' and lC >= 3:
		return '#'
	elif currentTile == '#' and (lC == 0 or tC == 0):
		return '.'
	return currentTile

grid = []
with open("input.txt", "r") as ins:
	for line in ins:
		chars = []
		for char in line:
			if char == '\n':
				continue
			chars.append(char)
		grid.append(chars)

for z in range(10):
	tempGrid = []
	for y in range(len(grid)):
		tempLine = []
		for x in range(len(grid[0])):
			tempLine.append(getNewVal(x, y, grid))
		tempGrid.append(tempLine)
	grid = tempGrid

vals = countTiles(grid)
print(vals)
print(vals[0] * vals[1])
