def parse_data(data):
    first = list(data[0:len(data) // 2])
    second = list(data[(len(data) // 2): len(data)])
    return [first, second]


def find_similar(rucksack):
    first, second, *rest = rucksack
    for elem in first:
        if elem in second:
            return elem


def calculate_value(element):
    if element.isupper():
        return ord(element) - ord('A') + 27
    else:
        return ord(element) - ord('a') + 1


def calculate_priorities():
    priorities = 0
    file = open("day3.txt", "r")
    rucksacks = list(map(parse_data, file.read().splitlines()))
    for rucksack in rucksacks:
        similar = find_similar(rucksack)
        priorities += calculate_value(similar)
    print(priorities)


calculate_priorities()
