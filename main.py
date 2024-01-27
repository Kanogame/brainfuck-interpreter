#!/usr/bin/env python3
import sys

if len(sys.argv) < 1:
    print("error")
    exit(-1)

inp = "".join([i for i in open(sys.argv[1])])
cmds = []
allowed = "<>+-,.[]"
streak = 0
streakCommand = ""

callStack = []

for i in inp:
    if i not in allowed:
        continue
    if i == "[":
        callStack.append(len(cmds) + 1)
    elif i == "]":
        cmds[callStack[-1]][1] = len(cmds) + 1
        callStack.pop()
    if i == streakCommand:
        streak += 1
    else:
        if streak > 0:
            cmds.append([streakCommand, streak])
        streak = 1
        streakCommand = i

cells = [0]
pointer = 0

#print("\n".join([str(i) + " " + cmds[i][0] + " " + str(cmds[i][1]) for i in range(len(cmds))]))

def inter(commands, offset=0):
    global pointer
    i = 0
    while i < len(commands):
        command = commands[i]
        match command[0]:
            case "+":
                cells[pointer] += command[1]
            case "-":
                cells[pointer] -= command[1]
            case ">":
                pointer += command[1]
            case "<":
                pointer -= command[1]
            case ".":
                for _ in range(command[1]):
                    print(chr(cells[pointer]), end="")
            case ",":
                0
            case "[":
                while cells[pointer] >= 1:
                    inter(commands[i + 1:command[1] - offset], i + 1)
                i = command[1] - offset
        if pointer > len(cells) - 1:
            cells.append(0)
        i += 1
inter(cmds)
print("")
