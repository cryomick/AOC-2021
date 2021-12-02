class Pos:
    horizontal = 0
    vertical = 0
    aim = 0

def compute_position(position: Pos, direction: str, distance: int):
    if direction == 'forward':
        position.horizontal += distance
    elif direction == 'up':
        position.vertical -= distance
    elif direction == 'down':
        position.vertical += distance

def compute_position_part_two(position: Pos, direction: str, distance: int):
    if direction == 'forward':
        position.horizontal += distance
        position.vertical += (position.aim * distance)
    elif direction == 'up':
        position.aim -= distance
    elif direction == 'down':
        position.aim += distance

def get_instructions(filename: str):
    ret = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            items = line.split()
            ret.append((items[0], int(items[1])))
    return ret

def main():
    instructions = get_instructions('input.txt')
    position_one = Pos()
    position_two = Pos()
    for instruction in instructions:
        compute_position(position_one, instruction[0], instruction[1])
        compute_position_part_two(position_two, instruction[0], instruction[1])
    print(f"Part one: {position_one.horizontal * position_one.vertical}")
    print(f"Part two: {position_two.horizontal * position_two.vertical}")

if __name__ == "__main__":
    main()
