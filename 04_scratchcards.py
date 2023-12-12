#!/usr/bin/python3

## Advent of Code 2023
## Day 4 - Scratchcards
## https://adventofcode.com/2023/day/4

import os
import sys

def countMatches(card, pile):
    matches = 0
    for num in pile:
        if num in card:
            matches += 1
    return matches

part1 = 0

with open("input04.txt") as f:
    for line in f:
        line = line.rstrip()
        line1 = line[10:]
        line1 = line1.split("|")
        #print(list(filter(None, line1[0].split(" "))))
        card = list(map(int, list(filter(None, line1[0].split(" ")))))
        pile = list(map(int, list(filter(None, line1[1].split(" ")))))
        matches = countMatches(card, pile)
        part1 += int(2 ** (matches - 1))

print("Part One:")
print(str(part1) + "\n")
#print("Part Two:")
#print(str(part2) + "\n")
exit(0)
