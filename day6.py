def find_signal():
    data = list(open('day6.txt', 'r').read())
    for i in range(len(data) - 3):
        possible_marker = set(data[i:i+4])
        if len(possible_marker) == 4:
            return i + 4
    return -1


def find_message():
    data = list(open('day6.txt', 'r').read())
    for i in range(len(data) - 14):
        possible_message = set(data[i:i+14])
        if len(possible_message) == 14:
            return i + 14
    return -1


print(find_signal())
print(find_message())
