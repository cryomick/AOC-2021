#!/usr/bin/python3

def get_params(input_list):
    output_max = ""
    output_min = ""
    string_size = len(input_list[0])
    for i in range(string_size):
        temp = [x[i] for x in input_list]
        output_max += max(set(temp), key=temp.count)
        output_min += min(set(temp), key=temp.count)
    return int(output_max, 2), int(output_min, 2)


def filter_list(input_list, position, value):
    output_list = []
    for item in input_list:
        if item[position] == value:
            output_list.append(item)
    return output_list


def get_params_part_two(input_list):
    size = len(input_list[0])
    O2_list = input_list
    CO2_list = input_list
    for i in range(size):
        pos_vals = [x[i] for x in O2_list]
        one_count = pos_vals.count('1')
        zero_count = pos_vals.count('0')
        if one_count >= zero_count:
            if len(O2_list) > 1:
                O2_list = filter_list(O2_list, i, "1")
        elif zero_count > one_count:
            if len(O2_list) > 1:
                O2_list = filter_list(O2_list, i, "0")

        pos_vals = [x[i] for x in CO2_list]
        one_count = pos_vals.count('1')
        zero_count = pos_vals.count('0')
        if one_count >= zero_count:
            if len(CO2_list) > 1:
                CO2_list = filter_list(CO2_list, i, "0")
        elif zero_count > one_count:
            if len(CO2_list) > 1:
                CO2_list = filter_list(CO2_list, i, "1")

    o2 = int("".join(O2_list[0]), 2)
    co2 = int("".join(CO2_list[0]), 2)
    return o2, co2


def generate_list(filename):
    with open(filename) as f:
        return [list(x.strip()) for x in f.readlines()]


def part_one(filename):
    gamma, epsilon = get_params(generate_list(filename))
    print(f"Part one: {gamma * epsilon}")


def part_two(filename):
    o2, co2 = get_params_part_two(generate_list(filename))
    print(f"Part two: {o2 * co2 }")


def main():
    filename = "input.txt"
    part_one(filename)
    part_two(filename)


if __name__ == '__main__':
    main()
