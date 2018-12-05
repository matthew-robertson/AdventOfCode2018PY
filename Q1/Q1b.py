text_file = open("input.txt", "r")
lines = text_file.readlines()
done = False
total = 0
occ = {0: 1}

while not done:
	print("Looping")
	for line in lines:
		total = total + int(line)
		if total not in occ:
			occ[total] = 1
		else:
			done = True
			break
print ("Done!")
print (total)