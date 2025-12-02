# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    splitLine = puzzleInput.readline().split(",")
    for i in splitLine:
        parsedInput.append(i.split("-"))

# Functions
def isNumberDoubled(number: int) -> bool:
    number = str(number)
    possibleNumberOfGroups = []
    # print(number)
    # print(number[0])
    for i in [2, 3, 4, 5, 6, 7, 8, 9]:
        if len(number) % i == 0:
            possibleNumberOfGroups.append(i)
    # print(possibleNumberOfGroups)
    for numberOfGroups in possibleNumberOfGroups:
        groupLength = (len(number) // numberOfGroups)
        # print("groupLength" , groupLength, "Possible:", (number[:groupLength] * numberOfGroups) == number, number[:groupLength])
        if (number[:groupLength] * numberOfGroups) == number:
            return True
    return False

#print(isNumberDoubled(121312))
# Program
invalidIDs = []
for idRange in parsedInput:
    for i in range(int(idRange[0]), int(idRange[1])+1):
        if isNumberDoubled(i):
            invalidIDs.append(i)

print(sum(invalidIDs))