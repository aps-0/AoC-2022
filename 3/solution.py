from string import ascii_letters

with open("input.txt", "r") as input_file:
    input = input_file.read().rstrip()

data = input.split("\n")


def part1(raw_data):
    data = []
    for rucksack in raw_data:
        compartment_size = int(len(rucksack) / 2)
        data.append((rucksack[:compartment_size], rucksack[compartment_size:]))

    total_priority = 0
    for rucksack in data:
        common = [item for item in rucksack[0] if item in rucksack[1]][0]
        total_priority += ascii_letters.index(common) + 1
    return total_priority


def part2(raw_data):
    data = []
    current_group = []
    for rucksack in raw_data:
        current_group.append(rucksack)
        if len(current_group) == 3:
            data.append(tuple(current_group))
            current_group = []

    total_priority = 0
    for group in data:
        common = [item for item in group[0] if item in group[1] and item in group[2]][0]
        total_priority += ascii_letters.index(common) + 1
    return total_priority


print("Part 1:", part1(data))
print("Part 2:", part2(data))
