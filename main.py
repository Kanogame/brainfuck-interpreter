#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("error")
        exit(-1)
    cmds, cin = parse_file(sys.argv[1])
    if not cin:
        interpret(cmds, input())
    else:
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
    if streak > 0:
        cmds.append([streakCommand, streak])
    return (cmds, inp.count(",") == 0)
cells = [0]
pointer = 0

def interpret(commands, cin="", offset=0):
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
                if pointer > len(cells) - 1:
                    while pointer > len(cells) - 1:
                        cells.append(0)
            case "<":
                pointer -= command[1]
                if pointer < 0: pointer = 0
            case ".":
                for _ in range(command[1]):
                    print(cells[pointer], end=" ")
            case ",":
                if cin == "":
                    cells[pointer] = 0
                else:
                    cells[pointer] = ord(cin[0])
                cin = cin[1:]
            case "[":
                while cells[pointer] > 0:
                    #print(cin, commands[i + 1:command[1] - offset],  offset + i + 1)
                    interpret(commands[i + 1:command[1] - offset], cin, offset + i + 1)
                i = command[1] - offset
            case "]":
                print("ERRR")
                exit(-1)
        i += 1
        #print(cells)

if __name__ == "__main__":
    main()
