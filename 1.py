import argparse

parser = argparse.ArgumentParser('Day 1')
parser.add_argument('filename')
args = parser.parse_args()

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def end_of_number(value, num_str, index):
    num_len = len(num_str)
    start_index = index - num_len + 1
    if start_index < 0:
        return False
    num_str_i = 0
    for i in range(start_index, start_index + num_len):
        if i >= len(value):
            return False
        if value[i] != num_str[num_str_i]:
            return False
        num_str_i += 1
    return True


def start_of_number(value, num_str, index):
    num_len = len(num_str)
    end_index = index + num_len - 1
    if end_index >= len(value):
        return False
    num_str_i = 0
    for i in range(index, end_index + 1):
        if value[i] != num_str[num_str_i]:
            return False
        num_str_i += 1
    return True


def check_start(value, index):
    for num in numbers:
        if start_of_number(value, num, index):
            return numbers[num]
    return -1


def check_end(value, index):
    for num in numbers:
        if end_of_number(value, num, index):
            return numbers[num]
    return -1


with open(args.filename, 'r', encoding='UTF-8') as file:
    sum = 0
    for line in file:
        value = line.rstrip()
        lval = ''
        rval = ''

        for l in range(0, len(value)):
            num = check_end(value, l)
            if num != -1:
                lval = str(num)
                break
            if value[l].isnumeric():
                lval = value[l]
                break
        if lval == '':
            raise ValueError('Couldn\'t find lvalue: ' + value)

        for r in range(len(value) - 1, -1, -1):
            num = check_start(value, r)
            if num != -1:
                rval = str(num)
                break
            if value[r].isnumeric():
                rval = value[r]
                break
        if rval == '':
            raise ValueError('Couldn\'t find rvalue: ' + value)

        num = int(lval + rval)
        print(num)
        sum += num
    print(sum)
