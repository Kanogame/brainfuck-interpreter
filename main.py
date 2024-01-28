#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("error")
        exit(-1)
    cmds = parse_file(sys.argv[1])
    interpret(cmds)

def parse_file(path):
    inp = "".join([i for i in open(path)])
    cmds, callStack = [], []
    allowed = "<>+-,.[]"

    streak = 1
    prev = ""
    for i in inp:
        if i not in allowed: continue
        if i == prev and i in allowed[:-2]: streak += 1
        else:
            cmds.append([prev, streak])
            streak = 1
            if i == "[":
                callStack.append(len(cmds))
            if i == "]":
                cmds[callStack[-1]][1] = len(cmds)
                streak = callStack[-1]
                callStack.pop()
        prev = i
    cmds.append([prev, streak])
    return cmds
cells = [0]
pointer = 0

def interpret(commands):
    global pointer
    i = 0
    while i < len(commands):
        command = commands[i]
        match command[0]:
            case "+": cells[pointer] += command[1]
            case "-": cells[pointer] -= command[1]
            case ">":
                pointer += command[1]
                for _ in range(pointer - len(cells) + 1):
                    cells.append(0) 
            case "<": pointer -= command[1]
            case ".":
                for _ in range(command[1]):
                    print(chr(cells[pointer]), end="")
            case ",": cells[pointer] = ord(sys.stdin.read(1))
            case "[": 
                if cells[pointer] == 0: i = command[1]
            case "]": 
                if cells[pointer] != 0: i = command[1]
        i += 1

if __name__ == "__main__":
    main()
