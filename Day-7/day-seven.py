def parseFile(filename):
    with open(filename) as f:
        ret = [int(x) for x in f.readline().strip().strip('\n').split(',')]
        return ret


def compute_cost_part_one(listPos, target):
    sum = 0
    for pos in listPos:
        sum += abs(pos - target)
    return sum


def compute_cost_part_two(listPos, target):
    sum = 0
    for pos in listPos:
        steps = abs(pos - target)
        sum += ((steps * (steps + 1)) / 2)
    return sum


def func(filename, computer):
    listPos = parseFile(filename)
    max_elem, min_elem = max(listPos), min(listPos)
    minimum_cost = float('inf')
    target = -1
    for i in range(min_elem, max_elem + 1):
        cost = computer(listPos, i)
        if cost < minimum_cost:
            minimum_cost = cost
            target = i
    return target, int(minimum_cost)


def part_one(filename):
    target, minimum_cost = func(filename, compute_cost_part_one)
    print(f"Part one: Cost to target {target} is {minimum_cost}")


def part_two(filename):
    target, minimum_cost = func(filename, compute_cost_part_two)
    print(f"Part two: Cost to target {target} is {minimum_cost}")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == "__main__":
    main()
