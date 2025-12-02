# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    splitLine = puzzleInput.readline().split(",")
    for i in splitLine:
        parsedInput.append(i.split("-"))

# Functions
def isNumberDoubeled(number: int) -> bool:
    number = str(number)
    if len(number) % 2 != 0:
        return False
    number_len = len(number) // 2
    return number[number_len:] == number[:number_len]

# Program
invalidIDs = []
for idRange in parsedInput:
    for i in range(int(idRange[0]), int(idRange[1])+1):
        if isNumberDoubeled(i):
            invalidIDs.append(i)

print(sum(invalidIDs))