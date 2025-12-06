# Parser
from math import prod

parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        strippedLine = line.strip().split(" ")
        lineList = []
        for i in strippedLine:
            if i != "":
                lineList.append(int(i) if i.isdigit() else i)
        parsedInput.append(lineList)

# Functions

# Program
solutions = []
operations = list(zip(*parsedInput))
for operation in operations:
    solution = 0
    if operation[-1] == "+":
        solution = sum(operation[:-1])
    else:
        solution = prod(operation[:-1])
    solutions.append(solution)
print(sum(solutions))