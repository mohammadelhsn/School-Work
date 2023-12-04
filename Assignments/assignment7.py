#############################################################################
#Author: Mohammad El-Hassan
#Description: Assignment 7
#Date Created: 2021/10/12
#Date Modified: 2021/10/12
#############################################################################

name = input("What is your name? ")
name_len = len(name)
first_letter = name[0]
no_decimal = int(input("Enter a random number, no decimals "))
one_decimal = float(input("Enter a number with one decimal "))
three_decimal = float(input("Enter a number with 3 decimal places "))
max_num = max(no_decimal, one_decimal, three_decimal)
min_num = min(no_decimal, one_decimal, three_decimal)
sum_num = round((no_decimal + one_decimal + three_decimal + name_len),3)
sub_num = round((no_decimal - one_decimal), 2)
mult_num = name_len * no_decimal
div_num = round(no_decimal / one_decimal,2) 
power_num = no_decimal ** 2
to_int = int(one_decimal)
round_num = round(three_decimal, 2)

print(f"Hello there, {name}")
print(f"Your name is {name_len} character(s) long")
print(f"Your first letter is {first_letter}")
print(f"The max number is {max_num}")
print(f"The min number is {min_num}")
print(f"After adding the numbers, including the name length, the sum is {sum_num}")
print(f"After subtracting {no_decimal} and {one_decimal} the answer is {sub_num}")
print(f"After multiplying {name_len} (length of your name) times {no_decimal}, the answer is {mult_num}")
print(f"{no_decimal} divided by {one_decimal} is {div_num}")
print(f"{no_decimal} to the power of 2 is {power_num}")
print(f"I rounded the three decimal place number, {three_decimal} to two decimal places and got {round_num}")
print(f"I have changed the number 1 decimal place number ({one_decimal}), to an integer and got {int(one_decimal)}")