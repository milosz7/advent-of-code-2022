def parse_data(data):
    pairs = data.split(',')
    return list(map(lambda pair: [int(elem) for elem in pair.split('-')], pairs))


def check_pair(pair):
    def get_range(a, b): return b - a
    first, second, *rest = pair
    higher_range = first
    lower_range = second
    if get_range(*second) > get_range(*first):
        higher_range = second
        lower_range = first
    if lower_range[0] >= higher_range[0] and lower_range[1] <= higher_range[1]:
        return 1
    else:
        return 0


def count_repetition():
    repetitions = 0
    file = open('day4.txt', 'r')
    data = list(map(parse_data, file.read().splitlines()))
    for pair in data:
        repetitions += check_pair(pair)
    print(repetitions)


count_repetition()
