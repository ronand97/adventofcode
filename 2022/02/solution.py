def read_data(part: int, fp: str = "./data.txt") -> list[tuple[str, str]]:
    with open(fp) as f:
        data = f.read().splitlines()
    final_out = []
    for turn in data:
        both_turns = turn.split(" ")
        final_out.append(
            (_map_strings(both_turns[0], part), _map_strings(both_turns[1], part))
        )
    return final_out


def _map_strings(in_str: str, part: int) -> str:
    """
    map ABC XYZ to actual rock paper scissors
    """
    if part == 1:
        mapper = {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors",
            "X": "Rock",
            "Y": "Paper",
            "Z": "Scissors"
        }
    elif part == 2:
        mapper = {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors",
            "X": "Lose",
            "Y": "Draw",
            "Z": "Win"
        }
    return mapper[in_str]


def score_turn(turn: tuple[str, str]) -> int:
    """
    they play:
        A = rock
        B = paper
        C = scissors
    I play:
        X = rock (+1)
        Y = paper (+2)
        Z = scissors (+3)

    scoring:
        lose = 0
        draw = 3
        win = 6
    Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    """
    my_scores = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }
    shape_score = my_scores[turn[1]]

    if turn[0] == turn[1]:  # draw
        outcome_score = 3
        return shape_score + outcome_score
    else:
        did_win = is_winner(turn)
        if did_win:
            outcome_score = 6
        else:
            outcome_score = 0

    return shape_score + outcome_score


def is_winner(turn: tuple[str, str]) -> bool:
    them = turn[0]
    me = turn[1]
    if me == "Rock" and them == "Scissors":
        return True
    elif me == "Scissors" and them == "Paper":
        return True
    elif me == "Paper" and them == "Rock":
        return True
    else:
        return False


def part_1(data: list[tuple[str, str]]) -> int:
    scores = []
    for turn in data:
        scores.append(score_turn(turn))
    return sum(scores)


def _win_lose(play: str, win: bool):
    if play == "Scissors":
        if win:
            return "Rock"
        else:
            return "Paper"
    elif play == "Paper":
        if win:
            return "Scissors"
        else:
            return "Rock"
    elif play == "Rock":
        if win:
            return "Paper"
        else:
            return "Scissors"


def part_2(data: list[tuple[str, str]]) -> int:
    scores = []
    for turn in data:
        if turn[1] == "Draw":
            turn_modified = (turn[0], turn[0])
        else:
            win: bool = True if turn[1] == "Win" else False
            to_play = _win_lose(turn[0], win)
            turn_modified = (turn[0], to_play)

        scores.append(score_turn(turn_modified))
    return sum(scores)


if __name__ == "__main__":
    data_1 = read_data(part=1)
    total_1 = part_1(data_1)
    print(f"The total score in part 1 is {total_1}")
    data_2 = read_data(part=2, fp="./data.txt")
    total_2 = part_2(data_2)
    print(f"The total score in part 1 is {total_2}")
