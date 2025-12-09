# Parser
parsedInput = []
with open("input.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(tuple(map(lambda x : int(x), line.strip().split(","))))

# Functions
def getRectangleArea(point1 : tuple[int, int], point2 : tuple[int, int]) -> int:
    return (abs(point1[0]-point2[0])+1) * (abs(point1[1]-point2[1])+1)


# Program
print(parsedInput)
biggestArea = 0
biggestAreaPoints = []
for p1 in parsedInput:
    for p2 in parsedInput:
        area = getRectangleArea(p1, p2)
        if area > biggestArea:
            biggestArea = area
            biggestAreaPoints = [p1, p2]
print(biggestArea)
print(biggestAreaPoints)