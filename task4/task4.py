
file_name = input()

with open(file_name, "r") as file:
    numbers = file.read()
    numbers = numbers.split("\n")
    #print(numbers)

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

numbers.sort()
num_len = int(len(numbers))

if len(numbers) % 2 != 0:
    numbers_median = numbers[int((num_len + 1)/ 2 - 1)]
else:
    numbers_median = round(numbers[int(num_len / 2 - 1)] + numbers[int(num_len / 2)] / 2) 

#print(numbers_median)
result = 0

for number in numbers:
    result += abs(int(numbers_median) - int(number))

print(result)
input()