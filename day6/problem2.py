from itertools import zip_longest, batched
from math import prod

# Parser
parsedInput = []
with open("testinput.txt", "r") as puzzleInput:
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

# Program
solutions = []
columnNumbers = list(zip_longest(*parsedInput, fillvalue=" "))
for col in range(len(columnNumbers)):
    columnNumbers[col] = "".join(columnNumbers[col]).strip()
columnNumbers.append("")
print(columnNumbers)

print(operators)
batchedOperators = []
batch = []
for i in range(len(operators)):
    if i == 0:
        batch.append(operators[i])
        continue
    if not (operators[i] == "+" or operators[i] == "*"):
        batch.append(operators[i])
        continue
    else:
        batchedOperators.append(batch)
        batch.clear()
        batch.append(operators[i])
# batchedOperators = list(map(lambda x: x[0], batchedOperators))
print(batchedOperators)

# batchedNumbers = list(batched(columnNumbers, n=columnNumbers.index("")+1))
# print(batchedNumbers)
# batchedNumbers = list(map(lambda x: x[:-1], batchedNumbers))
# print(batchedNumbers)
# batchedNumbers = list(map(lambda x: list(map(lambda y: int(y), x)), batchedNumbers))
# print(batchedNumbers)
#
# for operation in range(len(batchedNumbers)):
#     solution = 0
#     if batchedOperators[operation] == "+":
#         solution = sum(batchedNumbers[operation])
#     else:
#         solution = prod(batchedNumbers[operation])
#     solutions.append(solution)
# print(solutions)
# print(sum(solutions))