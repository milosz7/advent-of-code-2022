def find_similar(data):
    first, second, third, *rest = data
    for elem in first:
        if elem in second and elem in third:
            return elem


def calculate_value(element):
    if element.isupper():
        return ord(element) - ord('A') + 27
    else:
        return ord(element) - ord('a') + 1


def calculate_groups():
    i = 0
    priorities = 0
    file = open("day3.txt", "r")
    data = list(file.read().splitlines())
    while i < (len(data) - 2):
        priorities += calculate_value(find_similar(list(data[i:i + 3])))
        i += 3
    print(priorities)


calculate_groups()
