# Parser
parsedInput = []
with open("testinput.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(tuple(map(lambda x : int(x), line.strip().split(","))))

# Functions
def getRectangleArea(point1 : tuple[int, int], point2 : tuple[int, int]) -> int:
    return (abs(point1[0]-point2[0])+1) * (abs(point1[1]-point2[1])+1)


# Program
print(parsedInput)
biggestArea = 0
biggestAreaPoints = []
isRectIllegal = False
for i, p1 in enumerate(parsedInput):
    for p2 in parsedInput[i+1:]:
        isRectIllegal = False
        area = getRectangleArea(p1, p2)
        print("points:", p1, p2)
        for check in parsedInput:
            if p1[0] < p2[0] and p1[1] < p2[1]:
                if not (p1[0] < check[0] < p2[0] and p1[1] < check[1] < p2[1]):
                    continue
            elif p1[0] > p2[0] and p1[1] < p2[1]:
                if not(p1[0] > check[0] > p2[0] and p1[1] < check[1] < p2[1]):
                    continue
            elif p1[0] < p2[0] and p1[1] > p2[1]:
                if not (p1[0] < check[0] < p2[0] and p1[1] > check[1] > p2[1]):
                    continue
            elif p1[0] > p2[0] and p1[1] > p2[1]:
                if not (p1[0] > check[0] > p2[0] and p1[1] > check[1] > p2[1]):
                    continue
            print("check", check)
            isRectIllegal = True
            break
        print()
        if isRectIllegal:
            continue
        if area > biggestArea:
            biggestArea = area
            biggestAreaPoints = [p1, p2]
print(biggestArea)
print(biggestAreaPoints)