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
# freshIDs = set([])
numberOfFreshIDs = 0
# for currentRange in parsedInput_ranges:
#     separatedRange = [int(currentRange.split("-")[i]) for i in range(2)]
#     for freshID in range(separatedRange[0], separatedRange[1]+1):
#         freshIDs.add(freshID)
#     # print(separatedRange)
# # print(freshIDs)
# for availID in parsedInput_ids:
#     if int(availID) in freshIDs:
#         numberOfFreshIDs += 1
for id in parsedInput_ids:
    for i in parsedInput_ranges:
        range1, range2 = i.split("-")
        if int(range1) <= int(id) <= int(range2):
            numberOfFreshIDs += 1
            break
print(numberOfFreshIDs)