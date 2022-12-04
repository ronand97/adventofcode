from utils import split_list_into_sublists, set_intersection

def parse_data(fp) -> list[str]:
    """
    returns in form
    ['2-4', '5-9'] etc
    """
    with open(fp) as f:
        data = f.read().replace('\n', ',')
    return data.split(",")


def explode_range(range_str: str) -> list[int]:
    """
    given "2-4" return [2, 3, 4]
    """
    split = range_str.split('-')
    start = int(split[0])
    end = int(split[1])
    assert start <= end
    return list(range(start, end + 1))


def part_1(data) -> int:
    ranges = [explode_range(x) for x in data]
    pairs = split_list_into_sublists(ranges, 2)
    subsets: int = 0
    for pair in pairs:
        set1 = set(pair[0])
        set2 = set(pair[1])
        if set1.issubset(set2) or set2.issubset(set1):
            subsets += 1
    return subsets


def part_2(data) -> int:
    ranges = [explode_range(x) for x in data]
    pairs = split_list_into_sublists(ranges, 2)
    subsets: int = 0
    for pair in pairs:
        overlap = set_intersection(pair)
        if len(overlap) > 0:
            subsets += 1
    return subsets


if __name__ == "__main__":
    data = parse_data('./data.txt')
    subsets_1 = part_1(data)
    print(f"The number of assignment pairs that fully contains the other is {subsets_1}")
    subsets_2 = part_2(data)
    print(f"Number of overlapping ranges: {subsets_2}")

