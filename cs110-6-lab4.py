
####Daniel Ortega
####7/20/24
####cs110 summer2024 week6 lab3

def average(numbers):
    if len(numbers) == 0:
        return None
    else:
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)
list = [3, 5, 6, 8]
print("The average of list is " , average(list))