'''
Advent of Code 2021
Day 1: Sonar Sweep
'''

def part1(readings: int):
    '''Count the number of times depth increases.'''
    return sum(
        1 if readings[i+1] > readings[i]
        else 0 for i in range(0,len(readings)-1)
    )

def part2(readings):
    '''Count the number of time depth increases averaged over length three sliding window.'''
    return sum(
        1 if sum(readings[i+1:i+4]) > sum(readings[i:i+3])
        else 0 for i in range(0,len(readings)-2)
    )

if __name__ == "__main__":
    with open('input.txt', encoding='utf-8') as f:
        measurements = [int(line) for line in f.readlines()]
    print(f"Part 1: {part1(measurements)}")
    print(f"Part 2: {part2(measurements)}")
