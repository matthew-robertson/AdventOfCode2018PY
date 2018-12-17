scores = [3,7]

ins = '077201'
e1 = 0
e2 = 1
while True:
	if (len(scores) > 7):
		matchCount = 0
		for x in range(len(ins)):
			if scores[-1-x] == int(ins[-1-x]):
				matchCount += 1
		if matchCount == len(ins):
			break
		matchCount = 0
		for x in range(len(ins)):
			if scores[-2-x] == int(ins[-1-x]):
				matchCount += 1
		if matchCount == len(ins):
			break
	total = scores[e1] + scores[e2]
	s2 = total % 10
	if total > 9:
		s1 = int(total / 10)
		scores.append(s1)
	scores.append(s2)

	e1 = (e1 + scores[e1] + 1) % len(scores)
	e2 = (e2 + scores[e2] + 1) % len(scores)
	if (len(scores) % 100000 < 2):
		print("done this many: " + str(len(scores)))

print(len(scores)-len(ins))