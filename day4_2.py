def parse_data(data):
    pairs = data.split(',')
    return list(map(lambda pair: [int(elem) for elem in pair.split('-')], pairs))


def is_intersecting(first, second):
    first_sections = set(x for x in range(first[0], first[1] + 1))
    second_sections = set(x for x in range(second[0], second[1] + 1))
    if second_sections.intersection(first_sections):
        return 1
    return 0


def count_intersections():
    intersections = 0
    file = open('day4.txt', 'r')
    data = list(map(parse_data, file.read().splitlines()))
    for pair in data:
        intersections += is_intersecting(*pair)
    print(intersections)


count_intersections()