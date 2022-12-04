def read_text_file(fp) -> list[str]:
    with open(fp) as f:
        data = f.read().splitlines()
    return data


def set_intersection(in_list: list[any]) -> list[any]:
    """
    given a lists of strings each of same length return
    their intersection as a list
    """
    sets = [set(x) for x in in_list]
    return list(set.intersection(*sets))


def split_list_into_sublists(my_list, n) -> list[list]:
    """
    similar to numpy.array_split
    :param n: split every nth entry into new sublist
    """
    return [my_list[x:x+n] for x in range(0, len(my_list), n)]