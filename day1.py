def parse_data(data):
    if data != "":
        return int(data)
    else:
        return data


def highest_calories():
    counter = 0
    file = open("data.txt", "r")
    data = list(map(parse_data, file.read().splitlines()))
    calories = []
    for i in data:
        if i != '':
            counter += i
        else:
            calories.append(counter)
            counter = 0
    calories.sort(reverse=True)
    first, second, third, *rest = calories
    print(first + second + third)


highest_calories()
