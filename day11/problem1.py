# Parser
parsedInput : dict[str, list[str]] = {}
with open("testinput.txt", "r") as puzzleInput:
    for line in puzzleInput.readlines():
        splitLine = line.strip().split(":")
        parsedInput.update({splitLine[0] : splitLine[1].strip().split(" ")})

# Functions
def recursiveFor(keys, outs=0): # , previousKeys
    for key in parsedInput[keys]:
        print("  keyR:", key)
        if key == "out":
            outs += 1
            continue
        return recursiveFor(key, outs)
    return outs



# Program
# while ["out"] in parsedInput.values():
#     for k1 in parsedInput:
#         val = parsedInput[k1]
#         # print("key:", k1)
#         # print("value:", val)
#         if ["out"] == val:
#             for i in parsedInput:
#                 try:
#                     index = parsedInput[i].index(k1)
#                     # print("  val:", val)
#                     # print("  parsedInput[i]: ", parsedInput[i])
#                     # print("  index: ", index)
#                     parsedInput[i][index] = "out"
#                 except ValueError:
#                     pass
#             parsedInput.pop(k1) if k1 != "you" else parsedInput[k1]
#             # print("inp", parsedInput)
#             break

outs = 0
for key in parsedInput.get("you"):
    print("key:", key)
    # for k2 in parsedInput[key]:
    #     print(" k2:", k2)
    #     if k2 == "out":
    #         continue
    #     recursiveFor(parsedInput[k2])
    outs += recursiveFor(key)
print(outs)