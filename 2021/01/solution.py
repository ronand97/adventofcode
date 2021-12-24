def read_text_lines(fp):
    with open(fp) as f:
        lines = f.read().splitlines()
    return [int(x) for x in lines]

def solution_part1(data):
    num_increases = 0
    for idx, current_val in enumerate(data):
        if current_val > data[idx - 1]:
            num_increases += 1
    return num_increases

def solution_part2(data):
    '''essentially a window function with rolling sum over 3 index positions.
    could use pandas but will just write the algo manually then pass into our
    part1 solution'''
    window_sums = []
    for i in range(1, len(data)-1):
        calc = data[i-1] + data[i] + data[i+1]
        window_sums.append(calc)

    return solution_part1(window_sums)

if __name__ == "__main__":
    data = read_text_lines(fp='sonar-data.txt')
    soln_part_1 = solution_part1(data)
    soln_part_2 = solution_part2(data)
    print('# Part 1: The number of increases was ', soln_part_1)
    print('# Part 2: The number of increased window sums was ', soln_part_2)