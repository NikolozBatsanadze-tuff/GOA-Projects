numbers = []

number = int(input("how many numbers to add to list? "))

for i in range(number):
    numbers_1 = int(input("Whats ur number: "))
    numbers.append(numbers_1)
print(numbers)

for i in numbers:
    print(i)
print(len(numbers))