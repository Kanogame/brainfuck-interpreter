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

#print("\n".join([str(i) + " " + cmds[i][0] + " " + str(cmds[i][1]) for i in range(len(cmds))]))
