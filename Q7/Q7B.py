from collections import defaultdict

''' Our basic plan here: 
- create two dictionaries, one mapping keys to what they unlock, and one mapping keys to their prereqs
- while our dict still has keys:
	- iterate through to find keys with no prereqs remaining
	- choose the lowest alphabetically, then remove it as a prereq for everything else
'''
postreqs = defaultdict(list)
prereqs = defaultdict(list)
vals = []
with open("input.txt", "r") as ins:
	for line in ins:
		prereq = line.split(' ')[1]
		postreq = line.split(' ')[-3]
		prereqs[postreq].append(prereq)
		postreqs[prereq].append(postreq)
		vals.append(prereq)
		vals.append(postreq)

possibleKeys = set(vals)
remainingTime = defaultdict(int)
for x in possibleKeys:
		remainingTime[x] = 61 + ord(x) - ord("A")
answer = ""
totalTime = 0
while possibleKeys:
	possibilites = []
	for val in possibleKeys:
		if not val in prereqs:
			possibilites.append(val)

	target = ""
	for x in sorted(possibilites[:5]):
		if not target or remainingTime[x] < remainingTime[target]:
			target = x
	totalTime += remainingTime[target]
	decTime = remainingTime[target]
	for x in sorted(possibilites[:5]):
		remainingTime[x] = max(0, remainingTime[x] - decTime)

	for val in postreqs[target]:
		prereqs[val].remove(target)
		if not prereqs[val]:
			prereqs.pop(val)

	postreqs.pop(target)
	answer += target
	possibleKeys.remove(target)
print(answer)
print(totalTime)