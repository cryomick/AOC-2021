#!/usr/bin/python3

class Constants:
    bracket_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    openings = ['(', '[', '{', '<']
    closings = [')', ']', '}', '>']
    costs_one = {')': 3, ']': 57, '}': 1197, '>': 25137}
    costs_two = {')': 1, ']': 2, '}': 3, '>': 4}


def part_one(filename):
    error_value = 0
    with open(filename) as f:
        for line in f.readlines():
            brackets = []
            for bracket in line:
                if bracket in Constants.openings:
                    brackets.append(bracket)
                elif bracket in Constants.closings:
                    bracket_to_close = brackets.pop()
                    if bracket != Constants.bracket_pairs[bracket_to_close]:
                        error_value += Constants.costs_one[bracket]
                        break
    print(f"Part one: {error_value}")


def part_two(filename):
    points = []
    with open(filename) as f:
        for line in f.readlines():
            score = 0
            brackets = []
            valid = True
            for bracket in line:
                if bracket in Constants.openings:
                    brackets.append(bracket)
                elif bracket in Constants.closings:
                    bracket_to_close = brackets.pop()
                    if bracket != Constants.bracket_pairs[bracket_to_close]:
                        valid = False
                        break
            if valid:
                for bracket in reversed(brackets):
                    score = (score * 5) + \
                        Constants.costs_two[Constants.bracket_pairs[bracket]]
                points.append(score)
    points.sort()
    print(f"Part two: {points[len(points) // 2]}")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == "__main__":
    main()
