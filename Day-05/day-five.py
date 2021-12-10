def parseFile(filename, diag=False):
    coords = []
    with open(filename) as f:
        coords = [x.split("->") for x in f.readlines()]
        coords = [[x.strip().strip('\n').split(',')
                   for x in y] for y in coords]
        coords = [[[int(x) for x in y] for y in z] for z in coords]
        # for item in coords:
        # print(item)
        if not diag:
            #print("\nReduced List:")
            coords = [x for x in coords if x[0][0]
                      == x[1][0] or x[0][1] == x[1][1]]
            # for item in coords:
            # print(item)
    return coords


def get_points_on_line(x1, y1, x2, y2, diag):
    ret = []
    if x1 == x2:
        high, low = max(y1, y2), min(y1, y2)
        for i in range(low, high + 1):
            ret.append((x1, i))
    elif y1 == y2:
        high, low = max(x1, x2), min(x1, x2)
        for i in range(low, high + 1):
            ret.append((i, y1))
    else:
        if diag:
            # (0,0) -> (-8,8): m = -1; (x+m, y-m) => x2 < x1; y2 > y1
            # (0,0) -> (8,8): m = 1; (x+m, y+m) => x2 > x1; y2 > y1
            # (0,0) -> (8,-8): m = -1; (x-m, y+m) => x2 > x1, y2 < y1
            # (0,0) -> (-8,-8): m = 1; (x-m, y-m) => x2 < x1, y2 < y1
            slope = (y2 - y1) / (x2 - x1)
            ret.append((x1, y1))
            while y2 != y1 and x2 != x1:
                if x2 < x1 and y2 > y1:
                    x1 += slope
                    y1 -= slope
                elif x2 > x1 and y2 > y1:
                    x1 += slope
                    y1 += slope
                elif x2 > x1 and y2 < y1:
                    x1 -= slope
                    y1 += slope
                elif x2 < x1 and y2 < y1:
                    x1 -= slope
                    y1 -= slope
                ret.append((int(x1), int(y1)))

    return ret


def compute_collisions(coords, diag=False):
    crossed_map = {}
    for item in coords:
        line = get_points_on_line(
            item[0][0], item[0][1], item[1][0], item[1][1], diag)
        # print(
        # f"{item}: {line}")
        for point in line:
            if point not in crossed_map:
                crossed_map[point] = 1
            else:
                crossed_map[point] += 1
    return [x for x in crossed_map if crossed_map[x] >= 2]


def part_one(filename):
    coords = parseFile(filename)
    collisions = compute_collisions(coords)
    print(f"Part one: {len(collisions)}")


def part_two(filename):
    coords = parseFile(filename, True)
    collisions = compute_collisions(coords, True)
    print(f"Part two: {len(collisions)}")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == "__main__":
    main()
