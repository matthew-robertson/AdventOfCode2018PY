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

for x in range(0, 20):
	vals = sorted(plants.keys())
	tempPlants = defaultdict(lambda:'.')
	for y in range(vals[0] - 5, vals[-1]+1):
		checkString = plants[y] + plants[y+1] + plants[y+2] + plants[y+3] + plants[y+4]
		if isPlantMap[checkString] == '#':
			tempPlants[y+2] = '#'
	plants = tempPlants
print(plants.keys())
print(sum(plants.keys()))