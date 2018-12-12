serial = 7165

def calcPoint(point):
		rackId = point[0] + 10
		powerLevel = rackId * point[1]
		powerLevel += serial
		powerLevel *= rackId
		if (powerLevel >= 100):
			powerLevel = int(str(powerLevel)[-3])
		else:
			powerLevel = 0
		return powerLevel - 5

def calcBox(point):
	score = 0
	for y in range(0, 3):
		for x in range(0, 3):
			score += calcPoint([x+point[0],y+point[1]])
	return score

max = [1, 1, calcBox([1,1])]
for x in range(0, 298):
	for y in range(0, 298):
		score = calcBox([x+1,y+1])
		if max[2] < score:
			max[0] = x+1
			max[1] = y+1
			max[2] = score
print(max)

	