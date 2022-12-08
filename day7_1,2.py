update_space = 30000000
system_space = 70000000
removal_threshold = 100000


def replicate_folders():
    file = open('day7.txt', 'r').read().splitlines()
    data = [x for x in file]
    dirs_stack = []
    counter = {}
    result = 0
    to_remove = system_space
    for command in data:
        if '$ cd' in command:
            destination = command.split()[-1]
            if '..' not in destination:
                dirs_stack.append(destination)
            else:
                dirs_stack.pop()
        elif '$ ls' not in command and 'dir' not in command:
            value, key = command.split()
            for i in range(1, len(dirs_stack) + 1):
                unique_path = '/'.join(dirs_stack[0:i])
                if unique_path not in counter:
                    counter[unique_path] = 0
                counter[unique_path] += int(value)
    needed_space = update_space - (system_space - counter['/'])
    for v in counter.values():
        if v < removal_threshold:
            result += v
        if v >= needed_space:
            if v < to_remove:
                to_remove = v

    print(result, to_remove)


replicate_folders()

