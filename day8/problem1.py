# Parser
import math

parsedInput = []
with open("testinput.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        parsedInput.append(tuple(map(lambda x : int(x), line.strip().split(","))))

# Functions
def calculate3dDistance(coord1 : tuple[int, int, int], coord2 : tuple[int, int, int]) -> float:
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2 + (coord1[2] - coord2[2])**2)

def findShortestPoints(inp : list, blacklist : list[list[tuple[int, int, int]]]= None) -> list[tuple[int]]:
    if blacklist is None:
        blacklist = []
    shortestDistance = 1000000000000000000
    shortestPoints = []
    for i, c1 in enumerate(inp):
        for j, c2 in enumerate(inp[i+1:]):
            if [c1, c2] in blacklist:
                continue
            dist = calculate3dDistance(c1, c2)
            if dist < shortestDistance:
                shortestDistance = dist
                shortestPoints = [c1, c2]
    return list(shortestPoints)

def combine(connectedPoints):
    finalConnectedPoints = []
    for i, pair1 in enumerate(connectedPoints):
        for j, pair2 in enumerate(connectedPoints[i + 1:]):
            for point1 in pair1:
                if point1 in pair2:
                    print(pair1, " & ", pair2)
                    print(pair1+pair2)
                    print(set(pair1+pair2))
                    print(list(set(pair1+pair2)))
                    finalConnectedPoints.append(list(set(pair1+pair2)))
                    # if not connectedPoints[i] == connectedPoints[-1]:
                    # print(connectedPoints.pop(j))
                    print("###############################################")
                    for _ in connectedPoints:
                        print(_)
                    print("###############################################")
    return finalConnectedPoints

# Program
connectedPoints = []
for _ in range(10):
    connectedPoints.append(findShortestPoints(parsedInput, connectedPoints))
# for _ in range(100):
#     connectedPoints = combine(connectedPoints)
for _ in connectedPoints:
    print(_)
connectedPoints = combine(connectedPoints)
for _ in connectedPoints:
    print(_)