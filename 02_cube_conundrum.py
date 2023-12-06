#!/usr/bin/python3

## Advent of Code 2023
## Day 2 - Cube Conundrum
## https://adventofcode.com/2023/day/2

import os
import sys

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

part1 = part2 = 0

# returns true if all colors in the game are under the constant color limits, and false otherwise
def checkCubes(g):
    counts = {'red': 0, 'green': 0, 'blue': 0}
    g = g.split(', ')
    for color in g:
        color = color.split(' ')
        if color[1] not in ['red', 'green', 'blue']:
            continue
        counts[color[1]] += int(color[0])
    return (counts['red'] <= RED_LIMIT) and (counts['green'] <= GREEN_LIMIT) and (counts['blue'] <= BLUE_LIMIT)

# returns a dict representing the minimum set of cube colors for each game (keys = colors, values = min. counts)
# takes as parameter an array of the bag pulls from each game
def minimumSet(g):
    minset = {'red': 0, 'green': 0, 'blue': 0}
    for pull in g:
        pull = pull.split(', ')
        for color in pull:
            color = color.split(' ')
            if color[1] not in ['red', 'green', 'blue']:
                continue
            count = int(color[0])
            if count > minset[color[1]]:
                minset[color[1]] = count
    return minset


with open("input02.txt") as f:
    for line in f:
        line = line.rstrip()
        print(line)
        gameValid = True
        if len(line) == 0:
            continue
        line = line.split(': ')
        gameID = int(line[0].split(' ')[1])
        pulls = line[1].split('; ')
        minset = minimumSet(pulls)
        for color, count in minset.items():
            print("\t" + str(count) + " " + color)
        for pull in pulls:
            if not checkCubes(pull):
                gameValid = False
        if gameValid:
            part1 += gameID
        part2 += (minset['red'] * minset['green'] * minset['blue'])

print("Part One:")
print(str(part1) + "\n")
print("Part Two:")
print(str(part2) + "\n")
exit(0)
