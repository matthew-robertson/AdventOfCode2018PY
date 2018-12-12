'''Partial sums of boxes rooted in the upperleft corner are a way better solution
 but this works "well enough" by letting my just let it run, and once it stabilizes
 a bit I can try that answer'''

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
	for y in range(0, point[2]):
		for x in range(0, point[2]):
			score += grid[x+point[0]][y+point[1]]
	return score

gridSize = 300
grid = [[0 for i in range(0, gridSize)] for i in range(0, gridSize)]
for x in range(0, gridSize):
	for y in range(0, gridSize):
		grid[x][y] = calcPoint([x+1,y+1])

maxBox = [1, 1, 1, calcBox([1,1,1])]
for size in range(1, 301):
	print("checking: " + str(size))
	for x in range(0, 300-size):
		for y in range(0, 300-size):
			score = calcBox([x,y, size])
			if maxBox[3] < score:
				maxBox[0] = x+1
				maxBox[1] = y+1
				maxBox[2] = size
				maxBox[3] = score
				print(maxBox)


	