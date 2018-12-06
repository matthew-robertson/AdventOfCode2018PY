with open("input.txt", "r") as ins:
	for line in ins:
		le = 0
		while True:
			if le >= len(line)-1:
				break
			while (not line[le].islower() == line[le+1].islower()) and line[le].lower() == line[le+1].lower():
				line = line[:le] + line[le+2:]
				le -= 1
				le = max(0, le)
				if le >= len(line)-1:
					break
			le += 1
		print(len(line))