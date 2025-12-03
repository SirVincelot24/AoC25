# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(line.strip())

# Functions
def getHighestNumber(string : str) -> int:
    for number in range(9, 0, -1):
        if string.find(str(number)) == -1:
            continue
        return number
    return 1
# Program
numbers = []
# print(parsedInput[0][:-1])
for line in parsedInput:
    print(getHighestNumber(line[:-1]))
    firstDigit = getHighestNumber(line[:-1])
    firstDigitPosition = line.find(str(firstDigit))
    secondDigit = getHighestNumber(line[firstDigitPosition+1:])
    numbers.append(int(str(firstDigit) + str(secondDigit)))
print(sum(numbers))