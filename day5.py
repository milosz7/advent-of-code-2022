def parse_crates():
    crates_array = []
    crates = open('day5crates.txt', 'r')
    crates_data = list(map(lambda data: list(data), crates.read().splitlines()))
    for item in crates_data[-1]:
        column = []
        if item.isnumeric():
            column_index = crates_data[-1].index(item)
            for i in range(len(crates_data) - 1):
                column_element = crates_data[i][column_index]
                if column_element.isalpha():
                    column.append(crates_data[i][column_index])
            column.reverse()
            crates_array.append(column)
    return crates_array


def parse_data(data):
    contents = data.split()
    return [int(elem) - 1 for elem in contents if elem.isnumeric()]


def parse_moves():
    moves = open('day5moves.txt', 'r')
    moves_data = list(map(parse_data, moves.read().splitlines()))
    return moves_data


def move_crates():
    top_crates = ''
    crates = parse_crates()
    moves = parse_moves()
    for amount, column_from, column_to in moves:
        for i in range(amount + 1):
            crates[column_to].append(crates[column_from].pop())
    for column in crates:
        top_crates += column[-1]
    print('Move crates 9000: ' + top_crates)


def move_crates_9001():
    top_crates = ''
    crates = parse_crates()
    moves = parse_moves()
    for amount, column_from, column_to in moves:
        stack = []
        for i in range(amount + 1):
            stack.insert(0, crates[column_from].pop())
        for crate in stack:
            crates[column_to].append(crate)
    for column in crates:
        top_crates += column[-1]
    print('Move crates 9001: ' + top_crates)


move_crates()
move_crates_9001()
