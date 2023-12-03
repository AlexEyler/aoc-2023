from __future__ import annotations
import argparse
import typing


parser = argparse.ArgumentParser('Day 3')
parser.add_argument('--filename', dest='filename')
parser.add_argument('--part', dest='part', type=int)

args = parser.parse_args()


class Part:
    def __init__(self, part_num: int, row: int, digit_indicies: list[int]):
        self.part_num = part_num
        self.row = row
        self.digit_indicies = digit_indicies

    def __str__(self):
        return '{} ({}, {})'.format(self.part_num, self.row, self.digit_indicies)


class Symbol:
    def __init__(self, row: int, col: int, symbol: str):
        self.row = row
        self.col = col
        self.symbol = symbol

    def __str(self):
        return '{} ({}, {})'.format(self.symbol, self.row, self.col)


def is_symbol(value: str):
    return not value.isnumeric() and value != '.' and value != '\n'


class Grid:
    def __init__(self, lines: list[str]):
        self.parts: list[Part] = []
        self.symbols: list[Symbol] = []
        row = 0
        for line in lines:
            curnum = None
            curdigit_indicies = []
            for i in range(len(line)):
                if line[i].isnumeric():
                    if curnum is None:
                        curnum = ''
                        curdigit_indicies = []
                    curnum += line[i]
                    curdigit_indicies.append(i)
                else:
                    if curnum is not None:
                        self.parts.append(
                            Part(int(curnum), row, curdigit_indicies))
                        curnum = None
                        curdigit_indicies = []
                    if is_symbol(line[i]):
                        self.symbols.append(Symbol(row, i, line[i]))

            row += 1

    def part_sum(self):
        sum = 0
        found_parts = []
        for part in self.parts:
            for idx in part.digit_indicies:
                for sym in self.symbols:
                    if abs(sym.row - part.row) <= 1 and abs(sym.col - idx) <= 1 and part not in found_parts:
                        sum += part.part_num
                        found_parts.append(part)

        return sum

    def gear_sum(self):
        gear_candidates: typing.Dict[Symbol, list[Part]] = {}
        found_parts = []
        for part in self.parts:
            for idx in part.digit_indicies:
                for sym in self.symbols:
                    if sym.symbol != '*':
                        continue
                    if abs(sym.row - part.row) <= 1 and abs(sym.col - idx) <= 1 and part not in found_parts:
                        if sym not in gear_candidates:
                            gear_candidates[sym] = []
                        gear_candidates[sym].append(part)
                        found_parts.append(part)

        sum = 0
        for candidate in gear_candidates:
            if len(gear_candidates[candidate]) == 2:
                sum += gear_candidates[candidate][0].part_num * \
                    gear_candidates[candidate][1].part_num
        return sum


with open(args.filename, 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    grid = Grid(lines)
    if args.part == 1:
        print(grid.part_sum())
    elif args.part == 2:
        print(grid.gear_sum())
