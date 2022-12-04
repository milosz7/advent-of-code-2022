def parse_data(data):
    pairs = data.split(',')
    return list(map(lambda pair: [int(elem) for elem in pair.split('-')], pairs))


def check_pair(first, second):
    first_set = set(x for x in range(first[0], first[1] + 1))
    second_set = set(x for x in range(second[0], second[1] + 1))
    if first_set.issubset(second_set) or second_set.issubset(first_set):
        return 1
    return 0


def count_repetition():
    repetitions = 0
    file = open('day4.txt', 'r')
    data = list(map(parse_data, file.read().splitlines()))
    for pair in data:
        repetitions += check_pair(*pair)
    print(repetitions)


count_repetition()
