# This program will not stop unless user give the correct answer

# Write a program which prints the sum of numbers from 1 to 101 ( 1 and 101 are included) that are divisible by 5

number = 0
sum_of_number = 0
while number <= 101:
    if number % 5 == 0:
        sum_of_number = sum_of_number + number
    number = number + 1
print(sum_of_number)
