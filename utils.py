def read_text_file(fp) -> list[str]:
    with open(fp) as f:
        data = f.read().splitlines()
    return data


def set_intersection(in_list: list[str]) -> list[str]:
    """
    given a lists of strings each of same length return
    their intersection as a list of strings
    """
    sets = [set(x) for x in in_list]
    return list(set.intersection(*sets))
