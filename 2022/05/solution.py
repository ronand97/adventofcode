from utils import read_text_file
import numpy as np

def parse_data(fp) -> tuple[list[str], list[str], str]:
    raw = read_text_file(fp)
    split_index = raw.index('')
    return raw[:split_index - 1], raw[split_index + 1:], raw[split_index-1]


def parse_turns(turns: list[str]):
    moves = []
    from_cols = []
    to_cols = []
    for turn in turns:
        turn_split = turn.split(" ")
        moves.append(int(turn_split[1]))
        from_cols.append(int(turn_split[3]) - 1)
        to_cols.append(int(turn_split[5]) - 1)
    return moves, from_cols, to_cols


def parse_initial_state(initial_state: list[str], colnums: str):
    colnums_parsed = [int(x) for x in colnums if x.isnumeric()]
    cols = []
    for row in initial_state[::-1]:
        print("")
        tempcol = []
        for i in range(len(colnums_parsed)):
             idx = (i*4)+1
             tempcol.append(row[idx])
        cols.append(tempcol)
    
    as_columns = np.array(cols).T.tolist()
    for i, sublist in enumerate(as_columns):
        as_columns[i] = [x for x in sublist if x != " "]
    return as_columns


def take_turn(
        cols,
        n_move,
        from_col,
        to_col
    ) -> list[list]:

    for i in range(n_move):
        to_move = cols[from_col].pop(-1)
        cols[to_col].append(to_move)
        print(f"moving {to_move} from {from_col} to {to_col}")
        print(cols)
    return cols



def part_1(fp) -> str:
    initial_state, turns, colnums = parse_data(fp)
    moves, from_cols, to_cols = parse_turns(turns)
    columns = parse_initial_state(initial_state, colnums)
    for (move, from_col, to_col) in zip(moves, from_cols, to_cols):
        print('mft', move, from_col, to_col)
        columns = take_turn(columns, move, from_col, to_col)
    return columns


def take_turn_part2(
        cols,
        n_move,
        from_col,
        to_col
    ) -> list[list]:

    to_move_as_block = cols[from_col][-n_move:]
    del cols[from_col][-n_move:]
    [cols[to_col].append(x) for x in to_move_as_block]
    print(f"moving {to_move_as_block} from {from_col} to {to_col}")
    print(cols)
    return cols


def part_2(fp) -> str:
    initial_state, turns, colnums = parse_data(fp)
    moves, from_cols, to_cols = parse_turns(turns)
    columns = parse_initial_state(initial_state, colnums)
    for (move, from_col, to_col) in zip(moves, from_cols, to_cols):
        print('mft', move, from_col, to_col)
        columns = take_turn_part2(columns, move, from_col, to_col)
    return columns


if __name__ == "__main__":
    part1 = part_1('/Users/ronandiver/repos/adventofcode/2022/05/data.txt')
    for sublist in part1:
        print(sublist[-1])
    
    part2 = part_2('/Users/ronandiver/repos/adventofcode/2022/05/data.txt')
    print(part2)
    for sublist in part2:
        print(sublist[-1])