from itertools import zip_longest
from math import prod

# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        strippedLine = line[:-1]#.strip().split(" ")
        lineList = []
        for i in strippedLine:
            if i != "":
                lineList.append(i)
        parsedInput.append(lineList)
operators = parsedInput[-1]
parsedInput.pop(-1)

# Functions
def batchOperatorList(lst):
    batchedList = []
    batch = []
    for i in range(len(lst)):
        if i == 0:
            batch.append(lst[i])
            continue
        if not (lst[i] == "+" or lst[i] == "*"):
            batch.append(lst[i])
            continue
        else:
            batchedList.append(tuple(batch))
            batch.clear()
            batch.append(lst[i])
    batchedList.append(tuple(batch))
    return batchedList

def batchNumberList(lst):
    batchedList = []
    batch = []
    for i in range(len(lst)):
        if i == 0:
            batch.append(lst[i])
            continue
        if not (lst[i] == ""):
            batch.append(lst[i])
            continue
        else:
            batch.append(lst[i])
            batchedList.append(tuple(batch))
            batch.clear()
    return batchedList


# Program
solutions = []
columnNumbers = list(zip_longest(*parsedInput, fillvalue=" "))
for col in range(len(columnNumbers)):
    columnNumbers[col] = "".join(columnNumbers[col]).strip()
columnNumbers.append("")
print(columnNumbers)

print(operators)
batchedOperators = batchOperatorList(operators)
onlyOperators = list(map(lambda x: x[0], batchedOperators))
print(batchedOperators)
print(onlyOperators)

batchedNumbers = batchNumberList(columnNumbers)
print(batchedNumbers)
batchedNumbers = list(map(lambda x: x[:-1], batchedNumbers))
print(batchedNumbers)
batchedNumbers = list(map(lambda x: list(map(lambda y: int(y), x)), batchedNumbers))
print(batchedNumbers)

for operation in range(len(batchedNumbers)):
    solution = 0
    if onlyOperators[operation] == "+":
        solution = sum(batchedNumbers[operation])
    else:
        solution = prod(batchedNumbers[operation])
    solutions.append(solution)
print(solutions)
print(sum(solutions))