#!/usr/bin/python3

def get_depths(file_name):
    depths = []
    with open(file_name) as f:
        for line in f:
            depths.append(int(line))
    return depths


def get_depths_three_measurement_sliding_scale(file_name):
    depths = get_depths(file_name)
    ret = [sum(depths[i:i+3]) for i in range(0, len(depths) - 2)]
    return ret


def compute_depressions(depths):
    total_depressions = 0
    if len(depths) > 1:
        for i in range(1, len(depths)):
            if depths[i] > depths[i-1]:
                total_depressions += 1
    return total_depressions


def main():
    part_one = compute_depressions(get_depths('input.txt'))
    part_two = compute_depressions(
        get_depths_three_measurement_sliding_scale('input.txt'))
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')


if __name__ == '__main__':
    main()
