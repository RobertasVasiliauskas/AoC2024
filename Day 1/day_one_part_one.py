with open("Day1/data.txt", "r") as myFile:
    text = myFile.readlines()

left = []
right = []

for i in range(len(text)):
    numbers = text[i].strip().split("   ");
    left.append(numbers[0])
    right.append(numbers[1])

left.sort()
right.sort()

answer = 0;

for i in range(len(left)):
    answer += abs(int(left[i]) - int(right[i]))

print(answer)