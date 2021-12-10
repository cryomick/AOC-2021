#!/usr/bin/python3

class Cell:
    def __init__(self, val, row, col):
        self.val = val
        self.valid = True
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __ne__(self, other):
        return self.val != other.val

    def __str__(self):
        return f"{self.val}"


def printGrid(grid):
    for row in grid:
        for cell in row:
            if cell.valid:
                print(f"[{cell.val}]", end="")
            else:
                print(f"{cell.val}", end="")
        print("\n")
    print(f"{'=' * 40}")


def printVisited(grid):
    for row in grid:
        for cell in row:
            if cell:
                print("[X]", end="")
            else:
                print("[ ]", end="")
        print("\n")
    print(f"{'=' * 40}")


def get_neighbours(grid, cell):
    height = len(grid)
    assert height != 0
    width = len(grid[0])
    neighbours = []

    # UP
    up_row = cell.row - 1
    up_col = cell.col

    # DOWN
    down_row = cell.row + 1
    down_col = cell.col

    # LEFT
    left_row = cell.row
    left_col = cell.col - 1

    # UP
    right_row = cell.row
    right_col = cell.col + 1

    if up_row >= 0:
        neighbours.append(grid[up_row][up_col])
    if down_row < height:
        neighbours.append(grid[down_row][down_col])
    if left_col >= 0:
        neighbours.append(grid[left_row][left_col])
    if right_col < width:
        neighbours.append(grid[right_row][right_col])
    return neighbours


def parseFile(filename):
    output = []
    with open(filename) as f:
        row_count = 0
        for line in f.readlines():
            row = [Cell(int(x), row_count, i)
                   for i, x in enumerate(line.strip().strip('\n'))]
            output.append(row)
            row_count += 1
    return output


def get_low_points(grid):
    low_points = []
    for row in grid:
        for cell in row:
            if cell.valid:
                neighbours = get_neighbours(grid, cell)
                if min(neighbours) > cell:
                    low_points.append(cell)
                    for n in neighbours:
                        n.valid = False
    return low_points


def part_one(filename):
    grid = parseFile(filename)
    low_points = get_low_points(grid)
    print(f"Part one: {sum([cell.val + 1 for cell in low_points])}")


def search(grid, cell):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    to_be_visited = [cell]
    count = 0
    basin_cells = []
    while len(to_be_visited):
        cell_under_consideration = to_be_visited.pop()
        if visited[cell_under_consideration.row][cell_under_consideration.col]:
            continue
        count += 1
        basin_cells.append(cell_under_consideration)
        visited[cell_under_consideration.row][cell_under_consideration.col] = True
        valid_cells = [n for n in get_neighbours(
            grid, cell_under_consideration) if ((not visited[n.row][n.col]) and n.val < 9)]
        to_be_visited += valid_cells
    return count


def part_two(filename):
    grid = parseFile(filename)
    low_points = get_low_points(grid)
    basin_sizes = [search(grid, point) for point in low_points]
    basin_sizes.sort(reverse=True)
    valid_basins = basin_sizes[0:3]
    prod = 1
    for point in valid_basins:
        prod *= point
    print(f"Part two: {prod}")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == "__main__":
    main()
