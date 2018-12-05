fixedInput = open("input.txt", "r").readlines()
fixedInput = sorted(fixedInput)

sleepDict = {}

# Key is the guard id. First two elements are metadata, 
# last 60 are the minutes and how many times they have been asleep in that minute.
# Metadata: first element is total sleep time, second is sleepiest minute
activeGuard = 0
sleepTime = 0
for y in fixedInput:
	currentTime = int(y.split(']')[0][-2:])
	x = y.split('] ')[1]
	if (x[0] == 'G'):
		activeGuard = int(x.split(' ')[1][1:])
		if activeGuard not in sleepDict:
			sleepDict[activeGuard] = [0] * 62
	elif (x[0] == 'f'):
		sleepTime = int(y.split(']')[0][-2:])
	else:
		sleepDict[activeGuard][0] += currentTime-sleepTime
		for i in range(sleepTime, currentTime):
			sleepDict[activeGuard][2+i] += 1
			if sleepDict[activeGuard][2+i] > sleepDict[activeGuard][2 + sleepDict[activeGuard][1]]:
				sleepDict[activeGuard][1] = i

sleepiestGuard = [0,0]
for key, elem in sleepDict.items():
	if elem[0] > sleepiestGuard[1]:
		sleepiestGuard[0] = key
		sleepiestGuard[1] = elem[0]

print ("id: " + str(sleepiestGuard[0]) + ", sleepiest minute: " + str(sleepDict[sleepiestGuard[0]][1]))