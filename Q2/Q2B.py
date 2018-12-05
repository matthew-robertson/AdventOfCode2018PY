text_file = open("input.txt", "r")
lines = text_file.readlines()

for i, val in enumerate(lines):
	for x in range(i+1, len(lines)):
		diff = 0
		for y, v2 in enumerate(val):
			if not lines[x][y] == val[y]:
				diff += 1
				if (diff == 2):
					break
		if (diff == 1):
			print (val) 
			print (lines[x])
			break