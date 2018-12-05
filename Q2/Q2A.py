import string
import collections

count2 = 0
count3 = 0
alphabet = ['a','b','c','d']
with open("input.txt", "r") as ins:
	for line in ins:
		counts2 = False
		counts3 = False
		d = collections.defaultdict(int)
		for y in line:
			d[y] += 1
		for x in list(string.ascii_lowercase):
			if (d[x] == 2):
				counts2 = True
			if (d[x] == 3):
				counts3 = True
			if (counts2 and counts3):
				break
		count2 = count2 + counts2
		count3 = count3 + counts3
    
print (count2 * count3)