from collections import defaultdict

def find_between(s, start, end):
  return (s.split(start))[1].split(end)[0]

count = 0
fabric = defaultdict(int)
with open("input.txt", "r") as ins:
	for line in ins:
		key = int(line.split(' @ ')[0][1:])
		le   = int(find_between(line, ' @ ', ',' ))
		te   = int(find_between(line, ','  , ': '))
		w    = int(find_between(line, ': ' , 'x' ))
		h    = int(line.split('x')[1])

		for x in range(le, le + w):
			for y in range(te, te + h):
				fabric[(x,y)] = fabric[(x,y)] + 1
				if fabric[(x,y)] == 2:
					count = count + 1
print (count)