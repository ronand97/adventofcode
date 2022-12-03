from utils import read_text_file, set_intersection

def validate_file(data: list[str]):
    for strings in data:
        if len(strings) % 2 != 0:
            raise ValueError("strings not divisible by 2")


def split_rucksack(chars: str) -> list[str, str]:
    len_ruck = len(chars)
    return [chars[:len_ruck//2], chars[len_ruck//2:]]


def get_item_priorities(item: str) -> int:
    ascii_item = ord(item)
    if item.isupper():
        return ascii_item - 38
    else:
        return ascii_item - 96

def part_1(data) -> int:
    split_rucksacks = [split_rucksack(x) for x in data]
    duplicate_items = [set_intersection(x) for x in split_rucksacks]
    all_priorities: list[int] = []
    for sublist in duplicate_items:
        running_total = 0
        running_total += sum([get_item_priorities(item) for item in sublist])
        all_priorities.append(running_total)
    return sum(all_priorities)


def part_2(data) -> int:
    split_groups = [data[x:x+3] for x in range(0, len(data), 3)]
    badges = [set_intersection(x) for x in split_groups]
    if not all([len(x) == 1 for x in badges]):
        raise ValueError("not all badges are length 1")
    priorities = [get_item_priorities(x[0]) for x in badges]
    return sum(priorities)

if __name__ == "__main__":
    data = read_text_file('./data.txt')
    validate_file(data)

    total_duplicate_priorities = part_1(data)
    print(f"The sum of duplicate item priorities is {total_duplicate_priorities}")

    badge_priorities= part_2(data)
    print(f"The sum of the badge priorities is {badge_priorities}")