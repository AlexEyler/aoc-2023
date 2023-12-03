import argparse
import re

parser = argparse.ArgumentParser('Day 2')
parser.add_argument('--filename', dest='filename')
parser.add_argument('--part', dest='part')
args = parser.parse_args()


class Game:
    def __init__(self, line: str):
        line_split = line.split(':')
        game_search = re.search('^Game (\d*)', line_split[0], re.IGNORECASE)
        if not game_search:
            raise ValueError('Invalid line: ' + line)
        self.game = int(game_search.group(1))
        sets = line_split[1].strip().split(';')
        self.sets = []
        for set in sets:
            cubes = {}
            for r in re.finditer('(?P<amt>\d*) (?P<color>blue|red|green)', set, re.IGNORECASE):
                cubes[r.group('color')] = int(r.group('amt'))
            self.sets.append(cubes)

    def __str__(self):
        return 'Game {}: {}'.format(self.game, self.sets)


def part1(games: list[Game]):
    sum = 0
    for game in games:
        valid_game = True
        for set in game.sets:
            valid_set = True
            for cube in set:
                if cube == 'red' and set[cube] > 12:
                    valid_set = False
                    break
                if cube == 'green' and set[cube] > 13:
                    valid_set = False
                    break
                if cube == 'blue' and set[cube] > 14:
                    valid_set = False
                    break
            if not valid_set:
                valid_game = False
                break
        if valid_game:
            sum += game.game
    print(sum)


def part2(games: list[Game]):
    sum = 0
    for game in games:
        required_cubes = {'red': 0, 'blue': 0, 'green': 0}
        for set in game.sets:
            for cube in set:
                if set[cube] > required_cubes[cube]:
                    required_cubes[cube] = set[cube]
        power = required_cubes['red'] * \
            required_cubes['blue'] * required_cubes['green']
        sum += power
    print(sum)


with open(args.filename) as file:
    games = []
    for line in file:
        games.append(Game(line))

    if args.part == '1':
        part1(games)
    if args.part == '2':
        part2(games)
