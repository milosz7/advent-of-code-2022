def parse_data(data):
    if data != "":
        return int(data)
    else:
        return data


def highest_calories():
    result = 0
    counter = 0
    file = open("data.txt", "r")
    data = list(map(parse_data, file.read().splitlines()))
    for i in data:
        if i != '':
            counter += i
        else:
            if counter > result:
                result = counter
            counter = 0
    return result


print("Most calories: " + str(highest_calories()))
