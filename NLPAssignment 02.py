# -*- coding: utf-8 -*-


# Pgm no 01 Create the Half Diamond pattern using nested for loop in Python. 
    
rows = int(input("Enter the number of rows "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(1, i - 1):
        print("*", end=' ')
    print(" ")
    
# Pgm no 02 - write a Python program to reverse a word after accepting the input from the user.

word = input("Enter the word to be reversed:")
word [::-1]
