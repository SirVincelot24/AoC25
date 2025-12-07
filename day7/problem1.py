# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(list(line.strip()))

# Functions

# Program
splits = 0
for line in range(len(parsedInput)):
    currentLine = parsedInput[line]
    try:
        nextLine = parsedInput[line+1]
    except IndexError:
        nextLine = None
    previousLine = parsedInput[line-1]
    for i in range(len(currentLine)):
        if currentLine[i] == "S":
            nextLine[i] = "|"
        if currentLine[i] == "^" and previousLine[i] == "|":
            splits += 1
            currentLine[i-1] = "|"
            currentLine[i+1] = "|"
        if currentLine[i] == "." and previousLine[i] == "|":
            currentLine[i] = "|"


for _ in parsedInput:
    for __ in _:
        print(__, end="")
    print()
print(splits)