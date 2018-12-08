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
		print(prereq + " is a prereq of " + postreq)
		prereqs[postreq].append(prereq)
		postreqs[prereq].append(postreq)
		vals.append(prereq)
		vals.append(postreq)
possibleKeys = set(vals)
print(possibleKeys)
print("")
answer = ""

while possibleKeys:
	possibilites = []
	for val in possibleKeys:
		if not val in prereqs:
			possibilites.append(val)
	target = sorted(possibilites)[0]

	for val in postreqs[target]:
		print("Removing " + target + " as a prereq of " + str(val))
		prereqs[val].remove(target)
		if not prereqs[val]:
			prereqs.pop(val)

	postreqs.pop(target)
	answer += target
	possibleKeys.remove(target)
print(answer)