class Tree(object):
    def __init__(self):
        self.children = []
        self.data = []
        self.value = 0

answer = 0
def makeTree (numbers):
	global answer
	node = Tree()
	numChild = numbers[0]
	numData = numbers[1]
	trimNums = numbers[2:]
	for x in range(0, numChild):
		val = makeTree(trimNums)
		node.children.append(val[0])
		trimNums = val[1]

	for x in range(0, numData):
		val = trimNums.pop(0)
		node.data.append(val)

		if numChild == 0:
			node.value += val
		elif numChild > 0 and val <= len(node.children) and val > 0:
			node.value += node.children[val-1].value


	return node, trimNums

with open("input.txt", "r") as ins:
	for line in ins:
		nums = list(map(int, line.split(" ")))
		tree = makeTree(nums)[0]
		print (tree.value)
