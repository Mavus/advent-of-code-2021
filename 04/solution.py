'''
Advent of Code 2021
Day 4: Giant Squid
'''
from dataclasses import dataclass

@dataclass
class BingoValue():
    '''Represent a single value on a Bingo board. Mutable to include if it's been scored.'''
    value: int
    marked: bool = False

    def __post_init__(self):
        self.value = int(self.value)

    def __repr__(self):
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        repr_string = f"{' ' if self.value < 10 else ''}{self.value}"
        if self.marked:
            repr_string = UNDERLINE + repr_string + END
        return repr_string

class BingoBoard():
    '''Represent a Bingo board with values arranged in a 5 x 5 grid.'''
    def __init__(self, input_array):
        self.board = [[BingoValue(value) for value in row] for row in input_array]
        self.rows = self.board
        self.columns = list(map(list, zip(*self.board)))
        super().__init__()

    def mark(self, digit):
        for number in self:
            if int(digit) == number.value:
                number.marked = True

    def won(self):
        '''Check if a Bingo board is won.'''
        if any(all(number.marked for number in row) for row in self.rows):
            return True
        if any(all(number.marked for number in column) for column in self.columns):
            return True
        return False

    def score(self):
        '''Return score of a Bingo board.'''
        return sum(number.value for number in self if not number.marked)

    def __iter__(self):
        for row in self.rows:
            for number in row:
                yield number

    def __repr__(self):
        newline = "\n"
        return f"{newline.join(' '.join(str(n) for n in row) for row in self.board)}"

def part1(boards_list, draws):
    '''Find the Bingo board that wins first.'''
    print("First Winning Board:")
    for draw in draws:
        for board in boards_list:
            board.mark(draw)
            if board.won():
                print("Bingo!")
                print(board)
                print(f"Score: {board.score()}")
                return int(draw) * board.score()
    return "No winning board"

def part2(boards_list, draws):
    '''Find the Bingo board that wins last.'''
    print("Last winning Board:")
    for draw in draws:
        for board in boards_list:
            board.mark(draw)
            if board.won():
                last_board_to_win = board
                last_draw_to_win = draw
        boards_list = [b for b in boards_list if not b.won()]
    print(last_board_to_win)
    print(f"Score: {last_board_to_win.score()}")
    return int(last_draw_to_win) * last_board_to_win.score()


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as input_file:
        bingo_draws = input_file.readline()[:-1].split(',')
        input_file.readline()
        bingo_boards_arrays = [
            [row.split() for row in board.split("\n")]
            for board in input_file.read().split("\n\n")
        ]
        bingo_boards = [BingoBoard(board_array) for board_array in bingo_boards_arrays]
        print(part1(bingo_boards, bingo_draws))
        print(part2(bingo_boards, bingo_draws))
