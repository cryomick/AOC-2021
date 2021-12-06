class Cell:
    value: int
    marked: bool

    def __init__(self, value):
        self.marked = False
        self.value = value


class Grid:
    def __init__(self, input_str):
        self.__grid = []
        self.generate_grid(input_str)
        self.__width = len(self.__grid[0])
        self.__height = len(self.__grid)

    def generate_grid(self, input_str):
        input_str = input_str.strip().strip('\n')
        lines = input_str.split("\n")
        for line in lines:
            row = [Cell(int(val))
                   for val in line.strip().split()]
            self.__grid.append(row)

    def set_marked_if_present(self, value):
        for row in self.__grid:
            for item in row:
                if item.value == value and not item.marked:
                    item.marked = True

    def has_won(self):
        for row in self.__grid:
            row_marked = True
            for item in row:
                if not item.marked:
                    row_marked = False
                    break
            if row_marked:
                return True

        for col in range(self.__width):
            col_marked = True
            for row in range(self.__height):
                if not self.__grid[row][col].marked:
                    col_marked = False
                    break
            if col_marked:
                return True

    def print(self):
        for row in range(self.__height):
            row_str = ""
            for col in range(self.__width):
                marked = "X" if self.__grid[row][col].marked else ""
                row_str += f"{self.__grid[row][col].value}[{marked}]\t"
            print(row_str)

    def sum(self):
        sum = 0
        for row in range(self.__height):
            for col in range(self.__width):
                if not self.__grid[row][col].marked:
                    sum += self.__grid[row][col].value
        return sum


def part_one():
    with open("input.txt") as f:
        text = f.read()
        chunks = text.split("\n\n")
        moves = [int(val)
                 for val in chunks[0].strip().strip('\n').split(',')]
        grids = []
        for i in range(1, len(chunks)):
            grids.append(Grid(chunks[i]))

    for move in moves:
        for grid in grids:
            grid.set_marked_if_present(move)
            if grid.has_won():
                grid.print()
                print(f"Part One Solution is {grid.sum() * move}")
                return


def part_two():
    with open("input.txt") as f:
        text = f.read()
        chunks = text.split("\n\n")
        moves = [int(val)
                 for val in chunks[0].strip().strip('\n').split(',')]
        grids = []
        for i in range(1, len(chunks)):
            grids.append(Grid(chunks[i]))

    for move in moves:
        grids_to_remove = []
        for grid in grids:
            grid.set_marked_if_present(move)
            if grid.has_won():
                if len(grids) == 1:
                    grid.print()
                    print(f"Part Two Solution is {grid.sum() * move}")
                    return
                else:
                    grids_to_remove.append(grid)
        for grid in grids_to_remove:
            grids.remove(grid)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
