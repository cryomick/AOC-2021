#!/usr/bin/python3

class Cell:
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col
        self.flashed = False


def reset_flashes(grid):
    for row in grid:
        for cell in row:
            cell.flashed = False


def flash(grid, cell):
    for n in get_neighbours(grid, cell):
        if not n.flashed:
            n.val += 1


def age_cells(grid):
    flashes = 0
    reset_flashes(grid)
    for row in grid:
        for cell in row:
            cell.val += 1
    stop = False
    while not stop:
        stop = True
        for row in grid:
            for cell in row:
                if cell.val > 9:
                    flashes += 1
                    cell.val = 0
                    cell.flashed = True
                    flash(grid, cell)
                    stop = False
    return flashes


def print_grid(grid):
    for row in grid:
        for cell in row:
            print(f"[{cell.val:2}]  ", end="")
        print("\n")
    print(f"{'=' * 40}")


def parse_file(filename):
    grid = []
    with open(filename) as f:
        grid = [[Cell(int(x), row, col)
                 for col, x in enumerate(list(line.strip('\n')))]
                for row, line in enumerate(f.readlines())]
    return grid


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
    # TOP LEFT
    if up_row >= 0 and left_col >= 0:
        neighbours.append(grid[up_row][left_col])
    # TOP RIGHT
    if up_row >= 0 and right_col < width:
        neighbours.append(grid[up_row][right_col])
    # BOTTOM LEFT
    if down_row < height and left_col >= 0:
        neighbours.append(grid[down_row][left_col])
    # BOTTOM RIGHT
    if down_row < height and right_col < width:
        neighbours.append(grid[down_row][right_col])
    return neighbours


def part_one(filename):
    grid = parse_file(filename)
    count = 0
    for _ in range(100):
        count += age_cells(grid)
    print(f"Part one: {count}")


def part_two(filename):
    grid = parse_file(filename)
    count = 0
    iteration = 0
    while count != 100:
        count = age_cells(grid)
        iteration += 1
    print(f"Part two: {iteration}")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == "__main__":
    main()
