from collections import defaultdict
isPlantMap = {}
isPlantMap['.#...'] = '#'
isPlantMap['#....'] = '.'
isPlantMap['#.###'] = '.'
isPlantMap['#.##.'] = '.'
isPlantMap['#...#'] = '.'
isPlantMap['...#.'] = '.'
isPlantMap['.#..#'] = '#'
isPlantMap['.####'] = '#'
isPlantMap['.###.'] = '.'
isPlantMap['###..'] = '#'
isPlantMap['#####'] = '.'
isPlantMap['....#'] = '.'
isPlantMap['.#.##'] = '#'
isPlantMap['####.'] = '.'
isPlantMap['##.#.'] = '#'
isPlantMap['#.#.#'] = '#'
isPlantMap['..#.#'] = '.'
isPlantMap['.#.#.'] = '#'
isPlantMap['###.#'] = '#'
isPlantMap['##.##'] = '.'
isPlantMap['..#..'] = '.'
isPlantMap['.....'] = '.'
isPlantMap['..###'] = '#'
isPlantMap['#..##'] = '#'
isPlantMap['##...'] = '#'
isPlantMap['...##'] = '#'
isPlantMap['##..#'] = '.'
isPlantMap['.##..'] = '#'
isPlantMap['#..#.'] = '.'
isPlantMap['#.#..'] = '#'
isPlantMap['.##.#'] = '.'
isPlantMap['..##.'] = '.'

inputStr = '.##..##..####..#.#.#.###....#...#..#.#.#..#...#....##.#.#.#.#.#..######.##....##.###....##..#.####.#'
plants = defaultdict(lambda:'.')
for x in range(0, len(inputStr)):
	if inputStr[x] == '#':
		plants[x] = '#'
		rightMost = x

leftMost = sorted(plants.keys())[0]
rightMost = sorted(plants.keys())[-1]
sums = []
for x in range(0, 1000):
	hasFound = False
	tempPlants = defaultdict(lambda:'.')
	for y in range(leftMost - 5, rightMost+1):
		checkString = plants[y] + plants[y+1] + plants[y+2] + plants[y+3] + plants[y+4]
		if isPlantMap[checkString] == '#':	
			tempPlants[y+2] = '#'
			if not hasFound:
				leftMost = y+2
				hasFound = True
			rightMost = y+2

	plants = tempPlants
	print ("Done checking: " + str(x))
	sums.append(sum(plants.keys()))

#print(plants.keys())
print(sums[-1] + (50000000000 - 1000)*58)