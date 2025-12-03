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

def getHighestnDigits(n : int, input : str, currentDigits=None) -> int:
    if currentDigits is None:
        currentDigits = []
    currentDigit = getHighestNumber(input[:-n])
    if n == 0:
        currentDigit = getHighestNumber(input)
    currentDigitPosition = input.find(str(currentDigit))
    currentDigits.append(str(currentDigit))
    # print("CurrentDigit:", currentDigit,
    #       "currentDigitPos:", currentDigitPosition,
    #       "input[:-n]", input[:-n],
    #       "currentDigits:", currentDigits)
    if len(currentDigits) >= 12:
        return int("".join(currentDigits))
    return getHighestnDigits(n-1, input[currentDigitPosition+1:], currentDigits)

# Program
numbers = []
for line in parsedInput:
    numbers.append(getHighestnDigits(11, line))
    print(line)
print(numbers)
print(sum(numbers))
# print(getHighestnDigits(11, "818181911112111"))