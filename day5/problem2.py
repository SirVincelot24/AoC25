# Parser
parsedInput_ranges = []
parsedInput_ids = []
ranges = True
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        if line.strip() == "":
            ranges = False
            continue
        if ranges:
            parsedInput_ranges.append(line.strip())
        else:
            parsedInput_ids.append(line.strip())

# Functions

# Program
numberOfFreshIDs = 0
smallestRange = 0
biggestRange = 0

range1L = []
range2L = []

for j in parsedInput_ranges:
    range1, range2 = j.split("-")
    range1L.append(int(range1))
    range2L.append(int(range2))
range1L.sort()
smallestRange = range1L[0]
range2L.sort()
biggestRange = range2L[-1]
print(smallestRange)
print(biggestRange)

for id in range(smallestRange, biggestRange+1):
    for i in parsedInput_ranges:
        range1, range2 = i.split("-")
        if int(range1) <= int(id) <= int(range2):
            numberOfFreshIDs += 1
            break
print(numberOfFreshIDs)