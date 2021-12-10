#!/usr/bin/python3

def age(listFishes):
    back_list = [0] * 9
    back_list[8] += listFishes[0]
    back_list[6] += listFishes[0]

    for i in range(1, len(listFishes)):
        back_list[i - 1] += listFishes[i]
    return back_list


def parseFile(filename):
    listFishes = [0] * 9
    with open(filename) as f:
        list_ages = f.readline()
        ages = [int(x) for x in list_ages.strip().strip('\n').split(',')]
        for age in ages:
            listFishes[age] += 1
    return listFishes


def part_one(filename):
    listFishes = parseFile(filename)
    for _ in range(80):
        listFishes = age(listFishes)
    print(f"Part one: {sum(listFishes)}")


def part_two(filename):
    listFishes = parseFile(filename)
    for _ in range(256):
        listFishes = age(listFishes)
    print(f"Part two: {sum(listFishes)}")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == "__main__":
    main()
