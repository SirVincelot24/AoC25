# Parser
import random

parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(list(line.strip()))

# Functions
def generateDecisions():
    decisions = []
    for line in parsedInput:
        if "^" in line:
            decisions.append(random.choice([0, 1]))
        else:
            decisions.append(0)
    return decisions


# Program
decisions = generateDecisions()
# for line in range(len(parsedInput)):
#     currentLine = parsedInput[line]
#     try:
#         nextLine = parsedInput[line+1]
#     except IndexError:
#         nextLine = None
#     previousLine = parsedInput[line-1]
#     for i in range(len(currentLine)):
#         if currentLine[i] == "S":
#             nextLine[i] = "|"
#         if currentLine[i] == "^" and previousLine[i] == "|":
#             if decisions[line]:
#                 currentLine[i-1] = "|"
#             else:
#                 currentLine[i+1] = "|"
#         if currentLine[i] == "." and previousLine[i] == "|":
#             currentLine[i] = "|"
numberOfDecisions = 0
for line in parsedInput:
    if "^" in line:
        numberOfDecisions += 1


for _ in parsedInput:
    for __ in _:
        print(__, end="")
    print()
print(numberOfDecisions)