# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(list(line.strip()))

# Functions
def getAdjacent8Places(input : list, space : tuple) -> list:
    output = []
    x = space[0]
    y = space[1]
    rowAbove = y-1 if y > 0 else y
    rowBelow = y+1 if y < len(input)-1 else y
    elementBefore = x-1 if x > 0 else x
    elementAfter = x+2 if x < len(input[y])+1 else x
    output.append(input[rowAbove][elementBefore:elementAfter])
    if rowAbove == y:
        output[0] = []
    output.append(input[y][elementBefore:elementAfter])
    output.append(input[rowBelow][elementBefore:elementAfter])
    if rowBelow == y:
        output[2] = []
    return output

def countNestedList(listToCount : list, characterToCount) -> int:
    return sum([listToCount[i].count(characterToCount) for i in range(len(listToCount))])

def prg():
    global accessiblePaperRolls
    for y, line in enumerate(parsedInput):
        for x, elem in enumerate(line):
            if elem != "@":
                continue
            adjacent8Places = getAdjacent8Places(parsedInput, (x, y))
            if countNestedList(adjacent8Places, "@") < 5:
                # print(adjacent8Places[0])
                # print(adjacent8Places[1])
                # print(adjacent8Places[2])
                # print()
                accessiblePaperRolls += 1
                parsedInput[y][x] = "x"

# Program

global accessiblePaperRolls
accessiblePaperRolls = 0

for _ in range(200):
    prg()

for i in parsedInput:
    [print(j, end="") for j in i]
    print()

print(accessiblePaperRolls)