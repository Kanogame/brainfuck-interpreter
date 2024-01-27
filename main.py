#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("error")
        exit(-1)
    cmds = parse_file(sys.argv[1])
    interpret(cmds)
    print("")

def parse_file(path):
    inp = "".join([i for i in open(path)])
    cmds, callStack = [], []
    allowed = "<>+-,.[]"
    streak = 0
    streakCommand = ""

    for i in inp:
        if i not in allowed: continue
        if i == "[": callStack.append(len(cmds) + 1)
        elif i == "]":
            cmds[callStack[-1]][1] = len(cmds) + 1
            callStack.pop()
        if i == streakCommand: streak += 1
        else:
            if streak > 0:
                cmds.append([streakCommand, streak])
            streak = 1
            streakCommand = i
    return cmds
cells = [0]
pointer = 0

def interpret(commands, offset=0):
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
                    interpret(commands[i + 1:command[1] - offset], i + 1)
                i = command[1] - offset
        if pointer > len(cells) - 1:
            cells.append(0)
        i += 1

if __name__ == "__main__":
    main()
