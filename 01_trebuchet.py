#!/usr/bin/python3

## Advent of Code 2023
## Day 1 - Trebuchet?!
## https://adventofcode.com/2023/day/1

import os
import re
import sys

def numeralTranslation(line):
    line = re.sub(r'nine', '9', line)
    line = re.sub(r'eight', '8', line)
    line = re.sub(r'seven', '7', line)
    line = re.sub(r'six', '6', line)
    line = re.sub(r'five', '5', line)
    line = re.sub(r'four', '4', line)
    line = re.sub(r'three', '3', line)
    line = re.sub(r'two', '2', line)
    line = re.sub(r'one', '1', line)
    return line

part1 = part2 = 0

with open("input01.txt") as f:
    for line in f:
        line = line.rstrip()
        p2line = numeralTranslation(line)
        p1nums = re.sub(r'[a-z]', '', line)
        p2nums = re.sub(r'[a-z]', '', p2line)
        
        if len(p2nums) > 0:
            part1 += int(p1nums[0] + p1nums[len(p1nums) - 1])
            linesum = int(p2nums[0] + p2nums[len(p2nums) - 1])
            part2 += linesum
            print("Original line: " + line + ", proccessed line: " + p2line + ", pruned line: " + p2nums + ", adding: " + str(linesum) + ", sum: " + str(part2))

print("Part One:")
print(str(part1) + "\n")
print("Part Two:")
print(str(part2) + "\n")
exit(0)
