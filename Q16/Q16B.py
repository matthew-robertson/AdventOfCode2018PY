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

unknownCodes = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
knownCodes = {}

def checkNumBehaviour(sample):
	count = 0
	lastCode = addr
	for x in unknownCodes:
		if x(list(sample[0]), list(sample[1])) == list(sample[2]):
			count += 1
			lastCode = x
	if count == 1:
		knownCodes[sample[1][0]] = lastCode
		print("Found " + lastCode.__name__ + " as unique")
		unknownCodes.remove(lastCode)
	return count

sampleProgram = []
with open("input.txt", "r") as ins:
	parsingSamples = True
	lineCount = 0
	activeSample = []
	lastLine = ' '
	for line in ins:
		if line.isspace():
			if lastLine.isspace():
				parsingSamples = False
			lastLine = line
			lineCount += 1
			continue
		if parsingSamples:
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
		else:
			nums = line.split(' ')
			sampleProgram.append([int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])])

		lastLine = line
		lineCount += 1

ans = 0
while len(unknownCodes) > 0:
	for x in samples:
		checkNumBehaviour(x)

regs = [0, 0, 0, 0]
for x in sampleProgram:
	knownCodes[x[0]](regs, x)
print(regs)