unique_sizes = [2, 3, 4, 7]


def part_one(filename):
    with open(filename) as f:
        count = 0
        digit_repr = [x.split('|')[1].strip().strip('\n')
                      for x in f.readlines()]
        for item in digit_repr:
            temp = item.split()
            for digit in temp:
                if len(digit) in unique_sizes:
                    count += 1
        print(f"Part one: {count}")


def main():
    filename = "input.txt"
    part_one(filename)


if __name__ == "__main__":
    main()
