class List(object):
    def __init__(self):
        self.val = 0
        self.next = None
        self.previous = None

gameCircle = List()
gameCircle.val = 0
gameCircle.next = gameCircle
gameCircle.previous = gameCircle

with open("input.txt", "r") as ins:
	players = 0
	maxMarble = 0
	for line in ins:
		players = int(line.split(" ")[0])
		maxMarble = int(line.split(" ")[-2])

	playerScore = [0] * players
	currentPlayer = 1
	for x in range(1, maxMarble):
		if x % 23 == 0:
			gameCircle = gameCircle.previous.previous.previous.previous.previous.previous.previous
			playerScore[currentPlayer] += x + gameCircle.val
			nodeToRemove = gameCircle
			gameCircle.previous.next = nodeToRemove.next
			gameCircle.next.previous = nodeToRemove.previous
			gameCircle = gameCircle.next
			'''print (gameCircle.val)
			print (gameCircle.next.previous.val)
			print (gameCircle.previous.next.val)
			print (gameCircle.next.val)
			print (gameCircle.previous.val)'''
		else:
			newNode = List()
			newNode.val = x
			gameCircle = gameCircle.next
			newNode.next = gameCircle.next
			gameCircle.next.previous = newNode
			newNode.previous = gameCircle
			gameCircle.next = newNode
			gameCircle = newNode

		currentPlayer = (currentPlayer + 1) % players

	print (max(playerScore))
