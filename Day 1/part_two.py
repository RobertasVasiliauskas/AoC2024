with open("Day1/data.txt", "r") as myFile:
    text = myFile.readlines()

left = []
right = []

for i in range(len(text)):
    numbers = text[i].strip().split("   ");
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))

count = []

for i in range(len(left)):
    count.append(left[i] * right.count(left[i]))

print(sum(count))
