# Parser
import itertools

parsedInput = []
with open("testinput.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        line = line.strip()
        targetLights = line[1:line.find("]")]
        targetLights = [False if i == "." else True for i in targetLights]
        btns = line[line.find("]")+1:line.find("{")].strip()
        btns = btns.split(" ")
        buttons = []
        for btn in btns:
            btn = btn[1:-1]
            btn = btn.split(",")
            buttons.append(tuple(map(int, btn)))
        joltage = line[line.find("{")+1:-1].strip().split(",")
        joltage = list(map(int, joltage))
        parsedInput.append([targetLights, buttons, joltage])

# Functions
def pressButton(lights : list, button : tuple[int, ...]):
    for action in button:
        lights[action] = not lights[action]
    return lights

# Program
for machine in parsedInput:
    targetLights = machine[0]
    buttons = machine[1]
    joltage = machine[2]
    initialLights = [False for i in targetLights]
    possibilities = 2 ** (len(buttons)+1) - 1 # endless
    smallestNumberOfPresses = len(buttons)
    print("targetLights:", targetLights)
    print("buttons:", buttons)
    print("joltage:", joltage)
    print("initialLights:", initialLights)
    print()
    break