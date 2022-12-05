with open("input.txt", "r") as input_file:
    input = input_file.read().rstrip()

data = []
for group in input.split("\n"):
    section_ranges = [
        [int(terminal) for terminal in section_range.split("-")]
        for section_range in group.split(",")
    ]
    data.append(
        (
            (section_ranges[0][0], section_ranges[0][1]),
            (section_ranges[1][0], section_ranges[1][1]),
        )
    )


def part1(data):
    def is_subrange(a, b):
        return a[0] >= b[0] and a[1] <= b[1]

    fully_redundant_pairs = 0
    for group in data:
        if is_subrange(group[0], group[1]) or is_subrange(group[1], group[0]):
            fully_redundant_pairs += 1

    return fully_redundant_pairs


def part2(data):
    def has_overlap(a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    overlapping_pairs = 0
    for group in data:
        if has_overlap(group[0], group[1]):
            overlapping_pairs += 1
    return overlapping_pairs


print("Part 1:", part1(data))
print("Part 2:", part2(data))
