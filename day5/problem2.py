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
def combineRanges(range1 : tuple[int, int], range2 : tuple[int, int]) -> tuple[int, int] | tuple[tuple[int, int], tuple[int, int]]:
    if range1[0] <= range2[0] <= range1[1] and not (range1[0] <= range2[1] <= range1[1]):
        return range1[0], range2[1]
    elif not (range1[0] <= range2[0] <= range1[1]) and range1[0] <= range2[1] <= range1[1]:
        return range2[0], range1[1]
    elif range1[0] <= range2[0] <= range1[1] and range1[0] <= range2[1] <= range1[1]:
        return range1[0], range1[1]
    elif not (range1[0] <= range2[0] <= range1[1]) and not (range1[0] <= range2[1] <= range1[1]):
        if range2[0] < range1[0] and range2[1] > range1[1]:
            return range2[0], range2[1]
        elif range2[0] > range1[1] :
            return range1, range2
        else:
            return range1, range2
    else:
        return range2[0], range2[1]

def main(intRanges):
    afterRanges = []
    for i, intRange in enumerate(intRanges):
        if i == 0:
            afterRanges.append(intRange)
            continue
        previousRange = afterRanges[-1]
        combinedRanges = combineRanges(previousRange, intRange)
        # print(intRange)
        # print(previousRange)
        # print(combinedRanges)
        # print()
        if isinstance(combinedRanges[0], tuple):
            afterRanges[-1] = combinedRanges[0]
            afterRanges.append(combinedRanges[1])
            continue
        afterRanges[-1] = combineRanges(previousRange, intRange)
    return afterRanges

# Program
numberOfFreshIDs = 0
intRanges = []

for j in parsedInput_ranges:
    range1, range2 = j.split("-")
    intRanges.append((int(range1), int(range2)))

print(intRanges)
intRanges.sort()

afterRanges = main(intRanges)
for _ in range(300):
    afterRanges = main(afterRanges)
print(afterRanges)
for i in afterRanges:
    numberOfFreshIDs += i[1] + 1 - i[0]
print(numberOfFreshIDs)