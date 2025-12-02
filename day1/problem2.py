# Parser
parsedInput = []
with open("^input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        line.strip()
        parsedInput.append((line[0] + " " + line[1:]).split())

# Program
number = 50
zeros = 0
for i in parsedInput:
    increaser = int(i[1])
    for j in range(increaser):
        if i[0].lower() == "r":
            number = (1 + number) % 100
        else:
            number = (number - 1) % 100
        if number == 0:
            zeros += 1

print(number)
print(zeros)