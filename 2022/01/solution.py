def read_text(fp: str = r"./calories.txt") -> list[list[int]]:
    with open(fp) as file:
        data = file.read().splitlines()

    new_elf_starts_index: list[int] = []
    for i, entry in enumerate(data):
        if entry == "":
            new_elf_starts_index.append(i)

    elf_calories: list[list] = []
    for i, idx in enumerate(new_elf_starts_index):
        if i == 0:
            elf_calories.append([int(x) for x in data[0: idx]])
        else:
            elf_calories.append([int(x) for x in data[new_elf_starts_index[i-1]+1: idx]])
    return elf_calories


def get_elf_with_most_calories(data: list[list[int]]) -> None:
    total: tuple[int, int] = (-1, -1)
    for i, sublist in enumerate(data):
        if sum(sublist) > total[1]:
            total = (i, sum(sublist))
    print(f"The elf with the most calories was elf number {total[0] + 1} who has {total[1]} calories")


def get_calories_of_top_3_elves(data: list[list[int]]) -> None:
    total_calories = []
    for i, sublist in enumerate(data):
        total_calories.append(sum(sublist))
    total_calories.sort(reverse=True)
    print(f"The 3 elves with the most calories had a combined total calory count of {sum(total_calories[:3])}")


def part_a() -> None:
    data = read_text()
    get_elf_with_most_calories(data)


def part_b() -> None:
    data = read_text()
    get_calories_of_top_3_elves(data)


if __name__ == "__main__":
    part_a()
    part_b()
