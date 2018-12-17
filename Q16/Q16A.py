samples = []

def addr(regs, ins):
	regs[ins[3]] = regs[ins[1]] + regs[ins[2]]
	return regs

def addi(regs, ins):
	regs[ins[3]] = regs[ins[1]] + ins[2]
	return regs

def mulr(regs, ins):
	regs[ins[3]] = regs[ins[1]] * regs[ins[2]]
	return regs

def muli(regs, ins):
	regs[ins[3]] = regs[ins[1]] * ins[2]
	return regs

def banr(regs, ins):
	regs[ins[3]] = regs[ins[1]] & regs[ins[2]]
	return regs

def bani(regs, ins):
	regs[ins[3]] = regs[ins[1]] & ins[2]
	return regs

def borr(regs, ins):
	regs[ins[3]] = regs[ins[1]] | regs[ins[2]]
	return regs

def bori(regs, ins):
	regs[ins[3]] = regs[ins[1]] | ins[2]
	return regs

def setr(regs, ins):
	regs[ins[3]] = regs[ins[1]]
	return regs

def seti(regs, ins):
	regs[ins[3]] = ins[1]
	return regs

def gtir(regs, ins):
	regs[ins[3]] = int(ins[1] > regs[ins[2]])
	return regs

def gtri(regs, ins):
	regs[ins[3]] = int(regs[ins[1]] > ins[2])
	return regs

def gtrr(regs, ins):
	regs[ins[3]] = int(regs[ins[1]] > regs[ins[2]])
	return regs

def eqir(regs, ins):
	regs[ins[3]] = int(ins[1] == regs[ins[2]])
	return regs

def eqri(regs, ins):
	regs[ins[3]] = int(regs[ins[1]] == ins[2])
	return regs

def eqrr(regs, ins):
	regs[ins[3]] = int(regs[ins[1]] == regs[ins[2]])
	return regs
codes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def checkNumBehaviour(sample):
	count = 0
	for x in codes:
		if x(list(sample[0]), list(sample[1])) == list(sample[2]):
			count += 1
	return count

with open("inpput2.txt", "r") as ins:
	lineCount = 0
	activeSample = []
	lastLine = ' '
	for line in ins:
		if line.isspace():
			if lastLine.isspace():
				break
			lastLine = line
			lineCount += 1
			continue
		if lineCount % 4 == 0:
			nums = line.split('[')[1].split(']')[0].split(', ')
			activeSample.append([int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])])
		elif lineCount % 4 == 1:
			nums = line.split(' ')
			activeSample.append([int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])])
		elif lineCount % 4 == 2:
			nums = line.split('[')[1].split(']')[0].split(', ')
			activeSample.append([int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])])
			samples.append(activeSample)
			activeSample = []

		lastLine = line
		lineCount += 1

ans = 0
for x in samples:
	if checkNumBehaviour(x) >= 3:
		ans += 1
print(ans)