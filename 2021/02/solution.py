import os

def read_file(fp):
    with open(fp) as f:
        lines = f.read().splitlines()
    directions = []
    magnitudes = []
    for line in lines:
        direction, magnitude = line.split(' ')
        directions.append(direction)
        magnitudes.append(magnitude)
    magnitudes = [int(x) for x in magnitudes]
    return directions, magnitudes

def solution_part1(directions, magnitudes):
    # initial position is (x, z) == (0, 0)
    x = 0
    z = 0
    for i, direction in enumerate(directions):
        if direction == 'up':
            z -= magnitudes[i]
        elif direction == 'down':
            z += magnitudes[i]
        elif direction == 'forward':
            x += magnitudes[i]
    solution = x * z
    print(f'''Final depth is {z} with horizontal position {x} giving a solution of {solution}''')
    return solution

def solution_part2(directions, magnitudes):
    # initial position is (x, z) == (0, 0)
    x = 0
    z = 0
    aim = 0
    for i, direction in enumerate(directions):
        if direction == 'up':
            aim -= magnitudes[i]
        elif direction == 'down':
            aim += magnitudes[i]
        elif direction == 'forward':
            x += magnitudes[i]
            z += aim * magnitudes[i]
    solution = x * z
    print(f'''Final depth is {z} with horizontal position {x} giving a solution of {solution}''')
    return solution

if __name__ == "__main__":
    directions, magnitudes = read_file(f'positional-data.txt')
    solution_part1(directions, magnitudes)
    solution_part2(directions, magnitudes)