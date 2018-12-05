with open("input.txt", "r") as ins:
    total = 0
    for line in ins:
        total = total + int(line)
    print (total)