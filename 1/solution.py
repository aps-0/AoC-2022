with open("input.txt", "r") as input_file:
    input = input_file.read().rstrip()

data = []
for elf_calories in input.split("\n\n"):
    data.append([int(item_calories) for item_calories in elf_calories.split("\n")])

elf_total_calories = sorted([sum(elf_calories) for elf_calories in data], reverse=True)

print("Part 1:", elf_total_calories[0])
print("Part 2:", sum(elf_total_calories[0:3]))
