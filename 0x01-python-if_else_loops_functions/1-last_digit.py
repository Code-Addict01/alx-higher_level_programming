#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
<<<<<<< HEAD
    last_digit = ((-number % 10) * -1)
=======
    last_digit = ((-number % 10) * -1) 
>>>>>>> a635f55a510ba968f7b7da739c34c3030ef76239

print("Last digit of {} is {}".format(number, last_digit), end='')

if last_digit > 5:
    print(" and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(" and is less than 6 and not 0")
else:
    print(" and is 0")
