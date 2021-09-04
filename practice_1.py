# -*- coding: utf-8 -*-
# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

# ----------------------------------------#
# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a
# single line.

# Hints:
# Consider use range(#begin, #end) method


def question1(div, nomulti, rbegn, rend):

    nums = []
    for i in range(rbegn, rend+1):
        if (i % div == 0) and not (i % nomulti == 0):
            nums.append(str(i))
    print(','.join(nums))


#question1(7, 5, 2000, 3200)

# ---------------------------------------- #
# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to
# be a console input.


def factorial(num):

    if num == 0:
        return 1
    return num * factorial(num-1)


# x = int(input("Enter integer for factorial: "))
# print(factorial(x))

# ---------------------------------------- #
# Question 3
# Level 1

# Question:
# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n
# (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints:
# In case of input data being supplied to the question, it should be assumed to
# be a console input.
# Consider use dict()


def integral(num):
    ingal = {}
    for i in range(1, num+1):
            ingal[i] = i*i
    return ingal


# y = int(input("Enter integer for integral: "))
# print(integral(y))

# ----------------------------------------#
# Question 4
# Level 1
#
# Question:
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to
# be a console input.
# tuple() method can convert list to tuple


def numstolist(numstring):
    return numstring.split(',')


# nstr = input("Enter comma-separated numbers: ")
# nlist = numstolist(nstr)
# ntpl = tuple(nlist)

# print(nlist, "\n", ntpl, sep="")

# ----------------------------------------#
# Question 5
# Level 1
# 
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# 
# Hints:
# Use __init__ method to construct some parameters


class IOStringOps():

    def __init__(self):
        self.s = ""

    def getstring(self):
        self.s = input("Enter a string: ")

    def printstring(self):
        print(self.s.upper())

# strobject = IOStringOps()
# strobject.getstring()
# strobject.printstring()

# ----------------------------------------#
# Question 6
# Level 2
# 
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# 
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

# import math
# 
# 
# C = 50
# H = 30
# # ------------- My solution --------------------
# numsinp = tuple(map(int, input("Enter comma-separated numbers for SQRT: ").split(','))) 
# for i in range(len(numsinp)):
#     D = numsinp[i]
#     Q = int(math.sqrt((2*C*D)/H))
#     if i < len(numsinp)-1:
#         print("{0},".format(Q),end='')
#     else:
#         print("{0}".format(Q),end='')
# # ----------------------------------------------
# print()
# # -------------- Proposed solution ------------
# value = []
# items = [x for x in input("Enter numbers SQRT: ").split(',')]
# # print(items)
# for d in items:
#     value.append(str(int(round(math.sqrt(2*C*float(d)/H)))))
# print(','.join(value))

#----------------------------------------#
# Question 7
# Level 2
# 
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# 
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


# dims = [a for a in input('Enter X,Y array dimensions: ').split(',')]
# dimsarray = [[r*c for c in range(int(dims[1]))] for r in range(int(dims[0]))]
# print(dimsarray)


# ----------------------------------------#
# Question 8
# Level 2
# 
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# words = [w for w in input('Enter comma separated sequence of words: ').split(',')]
# print(','.join(sorted(words, key=str.lower)))


#----------------------------------------#
# Question 9
# Level 2
# 
# Question
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# lines = []
# while True:
#     line = input("Enter sequence of lines: ")
#     if line:
#         lines.append(line)
#     else:
#         break
# for line in lines:
#     print(line.upper())


#----------------------------------------#
# Question 10
# Level 2
# 
# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.


# words = [w for w in input("Enter whitespace separated words: ").split(' ')]
# print(' '.join(sorted(list(set(words)), key=str.lower)))
 

#----------------------------------------#
# Question 11
# Level 2
# 
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# bnums = [n for n in input("Enter sequence of comma sep 4-digit binary nums: ").split(',')]
# mod5list = []
# for num in bnums:
#     if not (int(num,2) % 5):  # if NOT True, ie. if there is no remainder to the division so the remainder is 0.
#         mod5list.append(num)
# # print(','.join(mod5list))
# print(*mod5list, sep=',')

#----------------------------------------#
# Question 12
# Level 2
# 
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# numrng = [int(n) for n in input("Enter 2 comma-separated integers for range: ").split(',')]
# evends = []
# for num in range(numrng[0], numrng[1]+1):
#     if all(int(i)%2 == 0 for i in str(num)):
#         # print("Num is:", num)
#         evends.append(num)
# 
# print(*evends, sep=',')

#----------------------------------------#
# Question 13
# Level 2
# 
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# inpstr = input("Enter a sentence with letters and digits: ")
# digits = 0
# alphas = 0
# for i in inpstr:
    # if i.isdigit():
        # digits += 1
    # elif i.isalpha():
        # alphas += 1
# print('LETTERS', alphas)
# print('DIGITS', digits)


#----------------------------------------#
# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# inpstr = input("Enter a sentence: ")
# caps = 0
# lower = 0
# for i in inpstr:
    # if i.isupper():
        # caps += 1
    # elif i.islower():
        # lower += 1
# print('UPPER CASE',caps)
# print('LOWER CASE',lower)


#----------------------------------------#
# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# a = input("Enter number to calulate formula: ")
# print(int(a)+int(2*a)+int(3*a)+int(4*a))


#----------------------------------------#
# Question 16
# Level 2

# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# nums = [x for x in input("Enter comma-separated integers: ").split(',') if int(x)%2]
# print(*nums, sep=',')

#----------------------------------------#

# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# ¡­
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# lines = []
# while True:
    # line = input("Enter sequence of lines: ")
    # if line:
        # lines.append(line)
    # else:
        # break

# net = 0
# for line in lines:
    # if line.split()[0] == 'D':
        # net += int(line.split()[1])
    # else:
        # net -= int(line.split()[1])
# print(net)

print("\n\nEnd of Practice!\n\n")

