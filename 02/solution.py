'''
Advent of Code 2021
Day 2: Dive!
'''

from dataclasses import dataclass

@dataclass
class Position():
    '''Store a submarine position and modify it by applying movement command.'''
    horizontal=0
    depth=0
    aim=0

    def distance_projection(self):
        '''Returns a projection product for distance covered.'''
        return self.horizontal * self.depth

    def move_ordinal(self, direction: str, amount: int):
        '''Move ordinally forward, down or up'''
        if   direction == "forward": self.horizontal += amount
        elif direction == "down":    self.depth      += amount
        elif direction == "up":      self.depth      -= amount

    def move_with_aim(self, direction: str, amount: int):
        '''Move'''
        if   direction == "forward": self.horizontal += amount; self.depth += self.aim * amount
        elif direction == "down":    self.aim        += amount
        elif direction == "up":      self.aim        -= amount

def part1(commands):
    '''Get submarine distance covered by moving ordinally.'''
    submarine_position = Position()
    for command in commands:
        submarine_position.move_ordinal(*command)
    return submarine_position.distance_projection()

def part2(commands):
    '''Get submarine distance covered move rotating and moving.'''
    submarine_postion = Position()
    for command in commands:
        submarine_postion.move_with_aim(*command)
    return submarine_postion.distance_projection()

if __name__ == "__main__":
    with open('input.txt', encoding='utf-8') as input_file:
        submarine_commands = [
            (d,int(m)) for d,m in map(lambda x: x.split(' '), input_file.readlines())
        ]
    print(f"Part 1: {part1(submarine_commands)}")
    print(f"Part 2: {part2(submarine_commands)}")
