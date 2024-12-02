def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def check_ascending(line: list[int]) -> bool:
    possible_steps_ascending = [1, 2, 3]
    for j in range(len(line) - 1):
        if line[j + 1] - line[j] not in possible_steps_ascending:
            return False
    return True

def check_descending(line: list[int]) -> bool:
    possible_steps_descending = [1, 2, 3]
    for j in range(len(line) - 1):
        if line[j] - line[j + 1] not in possible_steps_descending:
            return False
    return True

def is_safe_with_dampener(line: list[int]) -> bool:
    if check_ascending(line) or check_descending(line):
        return True
    
    for i in range(len(line)):
        new_line = line[:i] + line[i+1:]
        if check_ascending(new_line) or check_descending(new_line):
            return True
    
    return False

if __name__ == '__main__':
    answer = 0
    input_data = [list(map(int, line.split())) for line in read_input('Day 2/data.txt')]
    processed_data = []

    for line in input_data:
        if line[0] - line[1] > 0:
            processed_data.append((line, False))
        else:
            processed_data.append((line, True))

    for i in range(len(processed_data)):
        if is_safe_with_dampener(processed_data[i][0]):
            answer += 1

    print(answer)
