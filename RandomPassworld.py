import random

passlen = int(input("Enter password length "))
passnum = int(input("Enter number of passwords "))

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
numbers = "0123456789"
symbols = "!@#$%^&*()"
layout = lower_case+upper_case+numbers+symbols

for i in range(passnum):
    print(str("".join(random.sample(layout, passlen))))

input()