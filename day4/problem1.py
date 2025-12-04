# Parser
parsedInput = []
with open("testinput.txt", "r") as puzzleInput:
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
    elementAfter = x+2 if x < len(input[y])-1 else x
    output.append(input[rowAbove][elementBefore:elementAfter])
    print(input[rowAbove][elementBefore:elementAfter])
    output.append(input[y][elementBefore:elementAfter])
    print(input[y][elementBefore:elementAfter])
    output.append(input[rowBelow][elementBefore:elementAfter])
    print(input[rowBelow][elementBefore:elementAfter])
    return output

# Program
for i in parsedInput:
    [print(j, end="") for j in i]
    print()
print()
print()
print(getAdjacent8Places(parsedInput, (0, 1)))