import re 

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def filter_unnecessary_characters(data):
    possible_characters = set('mul(),0123456789')
    return ''.join([char if char in possible_characters else ' ' for char in data])

def extract_digits(data):

    numbers = []
    numbers = [tuple(map(int, re.findall(r"mul\((\d+),(\d+)\)", s)[0])) for s in data]
    return numbers
    
def mul(a, b):
    return a * b


if __name__ == '__main__':

    answer = 0


    input_data = read_input('Day 3/data.txt')
    filtered_data = filter_unnecessary_characters(input_data)
    matches = re.findall(r"mul\(\d+,\d+\)", filtered_data)
    extracted_digits = extract_digits(matches)
    
    for numbers in extracted_digits:
        answer += mul(numbers[0], numbers[1])
    
    print(answer)