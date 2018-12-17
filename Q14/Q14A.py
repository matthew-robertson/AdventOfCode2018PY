scores = [3,7]

ins = 77201
e1 = 0
e2 = 1
while True:
	if (len(scores) == ins + 10):
		break
	total = scores[e1] + scores[e2]
	s2 = total % 10
	if total > 9:
		s1 = int(total / 10)
		scores.append(s1)
	scores.append(s2)

	e1 = (e1 + scores[e1] + 1) % len(scores)
	e2 = (e2 + scores[e2] + 1) % len(scores)

print(scores[-10:])