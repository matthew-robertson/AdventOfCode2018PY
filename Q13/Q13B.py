from __future__ import print_function

def find(s, ch):
    return [[i, ch] for i, ltr in enumerate(s) if ltr == ch]

cartMap = {'<':[-1, 0], '>':[1, 0], 'v':[0,1], '^':[0, -1]}
carts = []
grid = []
with open("input.txt", "r") as ins:
	lineCount = 0
	for line in ins:
		track = line.replace('^', '|').replace('v', '|').replace('>', '-').replace('<', '-')
		grid.append(track)

		lineCarts = find(line, '<') + find(line, '>') + find(line, '^') + find(line, 'v')
		for x in lineCarts:
			carts.append([x[0], lineCount, cartMap[x[1]], 0])

		lineCount += 1

shouldRun = True
while shouldRun:
	carts.sort(key=lambda tup: 1000*tup[1] + tup[0])
	for idx, val in enumerate(carts):
		if val == -1:
			continue
		# Check where we're moving to
		newPos = val[:2]
		newPos[0] += val[2][0]
		newPos[1] += val[2][1]
		
		# Check if we've hit anything. If so, remove both carts, print and break.
		isCollision = False
		for idx2, val2 in enumerate(carts):
			if val2 == -1:
				continue
			if newPos == val2[:2]:
				print("HIT AT: " + str(newPos))
				isCollision = True
				carts[idx2] = -1
		if isCollision:
			carts[idx] = -1
			continue


		# Check what direction we now need to turn/update intersection code
		currentPiece = grid[newPos[1]][newPos[0]]
		if currentPiece == '\\':
			carts[idx][2] = [val[2][1], val[2][0]]
		elif currentPiece == '/':
			carts[idx][2] = [-val[2][1], -val[2][0]]
		elif currentPiece == '+':
			if carts[idx][3] == 0:
				newDir = [val[2][1], val[2][0]]
				if newDir[1] != 0:
					newDir[1] *= -1
				carts[idx][2] = newDir
			elif carts[idx][3] == 2:
				newDir = [val[2][1], val[2][0]]
				if newDir[0] != 0:
					newDir[0] *= -1
				carts[idx][2] = newDir

			carts[idx][3] = (carts[idx][3] + 1) % 3

		carts[idx][0] = newPos[0]
		carts[idx][1] = newPos[1]
	carts = list(filter(lambda a: a != -1, carts))
	if len(carts) == 1:
		break
	
print(carts)
