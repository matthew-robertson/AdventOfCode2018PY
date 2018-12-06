# Our idea is to find every distint character in the string (case-insensitive), then try removing each one to find the one the yields the shortest polymer

answer = 50000
with open("input.txt", "r") as ins:
	for line in ins:
		testSet = set(line.lower())
		for x in testSet:
			y = line.replace(x, '').replace(x.upper(), '')
			le = 0
			while True:
				if le >= len(y)-1:
					break
				while (not y[le].islower() == y[le+1].islower()) and y[le].lower() == y[le+1].lower():
					y = y[:le] + y[le+2:]

					le -= 1
					le = max(0, le)
					if le >= len(y)-1:
						break
				le += 1

			answer = min(answer, len(y))

print (answer)