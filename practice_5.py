# -----------------------------------------
# Question 51
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which
# can compute the area.
#
# Hints:
#
# Use def methodName(self) to define a method.


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


# -----------------------------------------
# Question 52
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as
# argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
#
# Hints:
#
# To override a method in super class, we can define a method with the same name in the super class.

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.length = l

    def area(self):
        return self.length**2


# -----------------------------------------
# Question 53
# Please raise a RuntimeError exception.
#
# Hints:
#
# Use raise() to raise an exception.

    # raise RuntimeError('something wrong')


# -----------------------------------------
# Question 54
# Write a function to compute 5/0 and use try/except to catch the exceptions.
#
# Hints:
#
# Use try/except to catch exceptions.

def div_by_zero():
    try:
        return 5 / 0
    except ZeroDivisionError:
        print("division by zero!")
    except Exception as err:
        print('Caught an exception', err)
    finally:
        print('In finally block for cleanup')


# -----------------------------------------
# Question 55
# Define a custom exception class which takes a string message as attribute.
#
# Hints:
#
# To define a custom exception, we need to define a class inherited from Exception.


class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


# OR --from: https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python

class MyAppValueError(ValueError):
    '''Raise when a specific subset of values in context of app is wrong'''
    def __init__(self, message, foo, *args):
        self.message = message # without this you may get DeprecationWarning
        # Special attribute you desire with your Error,
        # perhaps the value that caused the error?:
        self.foo = foo
        # allow users initialize misc. arguments as any other builtin Error
        super().__init__(message, foo, *args)


# -----------------------------------------
# Question 56
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
# user name of a given email address. Both user names and company names are composed of letters only.
#
# Example:
# If the following email address is given as input to the program:
#
# john@google.com
#
# Then, the output of the program should be:
#
# john
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
#
# Use \w to match letters.


def get_user_from_email():
    import re
    email = input('Enter email: ')
    print(re.search(r'(\w+)@', email).group(1))


# -----------------------------------------
# Question 57
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print
# the company name of a given email address. Both user names and company names are composed of letters only.
#
# Example:
# If the following email address is given as input to the program:
#
# john@google.com
#
# Then, the output of the program should be:
#
# google
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
#
# Use \w to match letters.

def get_company_from_email():
    import re
    email = input('Enter email: ')
    print(re.search(r'(\w+)@(\w+).', email).group(2))


# -----------------------------------------
# Question 58
# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of
# digits only.
#
# Example:
# If the following words is given as input to the program:
#
# 2 cats and 3 dogs.
#
# Then, the output of the program should be:
#
# ['2', '3']
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
#
# Use re.findall() to find all substring using regex.

def find_digits_in_sentence():
    import re
    words = input('Enter your sentence: ')
    digits = re.findall(r'\d', words)
    print(digits)


# -----------------------------------------
# Question 59
# Print a unicode string "hello world".
#
# Hints:
#
# Use u'strings' format to define unicode string.


def print_unicode_str():
    print(u'hello world')


# -----------------------------------------
# Question 60
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#
# Example:
# If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 3.55
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# Use float() to convert an integer to a float


def compute_seq_divisions(n):
    if n > 0:
        sum = 0
        while n > 0:
            sum += float(n) / (float(n)+1)
            n -= 1
        print('Result: ', sum)
    else:
        print('Nothing to compute')
        return


# -----------------------------------------
# Question 61
# Write a program to compute:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
#
# with a given n input by console (n>0).
#
# Example:
# If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 500
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# We can define recursive function in Python.


def calc_recursiv(n):
    if n > 0:
        return calc_recursiv(n-1) + 100
    else:
        return 0


# -----------------------------------------
# Question 62
# The Fibonacci Sequence is computed based on the following formula:
#
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program to compute the value of f(n) with a given n input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 7
#
# Then, the output of the program should be:
#
# 13
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints:
# We can define recursive function in Python.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# -----------------------------------------
# Question 63
# The Fibonacci Sequence is computed based on the following formula:
#
#
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
#
# Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given
# n input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 7
#
# Then, the output of the program should be:
#
# 0,1,1,2,3,5,8,13
#
#
# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.
#
# In case of input data being supplied to the question, it should be assumed to be a console input.


def print_fibonacci_seq(n):
    fibo = [str(fibonacci(n)) for n in range(0, n+1)]
    print('Fibonacci sequence: ', ','.join(fibo))


# -----------------------------------------
# Question 64
# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is
# input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 10
#
# Then, the output of the program should be:
#
# 0,2,4,6,8,10
#
# Hints:
# Use yield to produce the next value in generator.
#
# In case of input data being supplied to the question, it should be assumed to be a console input.

def gen_evens_in_range(n):
    for i in range(n):
        if not i%2:
            yield i


def print_evens_in_range():
    n = 1
    values = []
    while n > 0:
        n = int(input('Enter integer to print even numbers: '))
        for value in gen_evens_in_range(n+1):
            values.append(str(value))
        print('Evens for n={} are: {}'.format(n, ','.join(values)))


# -----------------------------------------
# Question 65
# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in
# comma separated form while n is input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 100
#
# Then, the output of the program should be:
#
# 0,35,70
#
# Hints:
# Use yield to produce the next value in generator.
#
# In case of input data being supplied to the question, it should be assumed to be a console input.


def gen_div_5_7_in_range(n):
    for i in range(n):
        if (not i%7) and (not i%5):
            yield i

def print_divby5_7_in_range():
    n = 1
    values = []
    while n > 0:
        n = int(input('Enter integer to print even numbers: '))
        for value in gen_div_5_7_in_range(n+1):
            values.append(str(value))
        print('Divisible by 5 and 7 for n={} are: {}'.format(n, ','.join(values)))
        # empty list
        del values[:]


# -----------------------------------------
# Question 66
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.
#
# Hints:
# Use "assert expression" to make assertion.

def check_list_evens(list):
    for x in list:
        assert x%2 == 0, 'Not all numbers in list are even'


# -----------------------------------------
# Question 67
# Please write a program which accepts basic mathematic expression from console and print the evaluation result.
#
# Example:
# If the following string is given as input to the program:
#
# 35+3
#
# Then, the output of the program should be:
#
# 38
#
# Hints:
# Use eval() to evaluate an expression.

def simpe_math_calc():
    print('Result: ', eval(input('Enter simple math folmula: ')))


# -----------------------------------------
# Question 68
# Please write a binary search function which searches an item in a sorted list. The function should return the index
# of element to be searched in the list.
#
# Hints:
# Use if/elif to deal with conditions.

def binary_search(sorted_list, item):
    first = 0
    last = len(sorted_list) - 1
    while first < last:
        midpoint = (first + last)//2
        if sorted_list[midpoint] == item:
            return midpoint
        elif sorted_list[midpoint] > item:
            last = midpoint - 1  # Since we have already examined the midpoint
        else:
            first = midpoint + 1  # Since we have already examined the midpoint
    return None


# -----------------------------------------
# Question 69
# Please generate a random float where the value is between 10 and 100 using Python math module.
#
# Hints:
# Use random.random() to generate a random float in [0,1].


def rand_10to100():
    import random
    # Solution 1
    # return random.random()*100
    # or Solution 2
    return random.uniform(10, 100)


# -----------------------------------------
# Question 70
# Please write a program to output a random even number between 0 and 10 inclusive using random module and list
# comprehension.
#
# Hints:
# Use random.choice() to a random element from a list.


def rand_from_range(n1, n2):
    import random
    return random.choice([i for i in range(n1, n2+1) if not i % 2])


# -----------------------------------------
# Question 71
# Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using
# random module and list comprehension.
#
# Hints:
# Use random.choice() to a random element from a list.

def rand_from_range2(n1, n2):
    import random
    return random.choice([i for i in range(n1, n2+1) if i%5==0 and i%7==0])


# -----------------------------------------
# Question 72
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
#
# Hints:
# Use random.sample() to generate a list of random values.

def rand_k_nums_from_range(n1, n2, rn):
    import random
    return random.sample([i for i in range(n1, n2+1)], rn)


# -----------------------------------------
# Question 73
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and
# 1000 inclusive.
#
# Hints:
# Use random.sample() to generate a list of random values.


def rand_5_from_range(n1, n2):
    import random
    return random.sample([i for i in range(n1, n2+1) if i%5==0 and i%7==0], 5)


# -----------------------------------------
# Question 74
# Please write a program to randomly print a integer number between 7 and 15 inclusive.
#
# Hints:
# Use random.randrange() to a random integer in a given range.


def rand_int_in_range(n1, n2):
    import random
    return random.randint(n1, n2)


# -----------------------------------------
# Question 75
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
#
# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.

def cmpress_decomprs():
    import zlib
    data = 'hello world!hello world!hello world!hello world!'
    compressed_data = zlib.compress(data.encode('utf-8'), -1)
    print(zlib.decompress(compressed_data))


# -----------------------------------------
# Question 76
# Please write a program to print the running time of execution of "1+1" for 100 times.
#
# Hints:
# Use timeit() function to measure the running time.


def time_the_f():
    import timeit
    print(timeit.timeit("1+1", number=100))


# -----------------------------------------
# Question 77
# Please write a program to shuffle and print the list [3,6,7,8].
#
# Hints:
# Use shuffle() function to shuffle a list.


def list_shuffle(l):
    from random import shuffle
    print('shuffling')
    shuffle(l)
    print(l)


# -----------------------------------------
# Question 78
# write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the
# object is in ["Hockey","Football"].
#
# Hints:
# Use list[index] notation to get a element from a list.


def sentence_generator(subj, verb, obj):
    for s in subj:
        for v in verb:
            for o in obj:
                print(s + ' ' + v + ' ' + o)


# -----------------------------------------
# Question 79
# write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
#
# Hints:
# Use list comprehension to delete a bunch of element from a list.


def print_remove_evens(l):
    print([x for x in l if x % 2])


# -----------------------------------------
# Question 80
# By using list comprehension, please write a program to print the list after removing delete numbers which are
# divisible by 5 and 7 in [12,24,35,70,88,120,155].
#
# Hints:
# Use list comprehension to delete a bunch of element from a list.


def print_remove_div_by5n7(l):
    print([x for x in l if (x % 5 and x % 7)])


# -----------------------------------------
# Question 81
# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th, 6th numbers
# in [12,24,35,70,88,120,155].
#
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple


def print_lst_remove_at_position(l):
    print([x for (i, x) in enumerate(l) if i % 2])


# -----------------------------------------
# Question 82
# By using list comprehension, please write a program to generate a 3*5*8 3D array whose each element is 0.
#
# Hints:
# Use list comprehension to make an array.


def gen_list_3d_array(d1, d2, d3):
    return [[[0 for col in range(d3)] for col in range(d2)] for row in range(d1)]


# -----------------------------------------
# Question 83
# By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers
# in [12,24,35,70,88,120,155].
#
# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.


def print_remv_at_posit(l, rl):
    print([x for (i, x) in enumerate(l) if i not in rl])


# -----------------------------------------
# Question 84
# By using list comprehension, please write a program to print the list after removing the value 24
# in [12,24,35,24,88,120,155].
#
# Hints:
# Use list's remove method to delete a value.


def print_l_rm_val(l, val):
    l.remove(val)
    print(l)


# -----------------------------------------
# Question 85
# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are
# intersection of the above given lists.
#
# Hints:
# Use set() and "&=" to do set intersection operation.


def intersect(la, lb):
    return list(set(la) & set(lb))


# -----------------------------------------
# Question 86
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
# duplicate values with original order reserved.
#
# Hints:
# Use set() to store a number of values without duplicate.


def rmv_lst_dublicts(l):
    seen = set()
    unique_l = []
    for x in l:
        if x not in seen:
            unique_l.append(x)
            seen.add(x)
    return unique_l


# -----------------------------------------
# Question 87
# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can
# print "Male" for Male class and "Female" for Female class.
#
# Hints:
# Use Subclass(Parentclass) to define a child class.


class Person:

    def getGender(self):
        return 'Unknown'


class Male(Person):

    def getGender(self):
        return 'Male'


class Female(Person):

    def getGender(self):
        return 'Female'


# -----------------------------------------
# Question 88
# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example:
# If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
#
# Hints:
# Use dict to store key/value pairs.
# Use dict.get() method to lookup a key with default value.


def char_freq_strng():
    d = {}
    s = input('Enter string: ')
    for c in s:
        d[c] = d.get(c, 0) + 1
    for k, v in d.items():
        print(k, ',', v)


# -----------------------------------------
# Question 89
# Please write a program which accepts a string from console and print it in reverse order.
#
# Example:
# If the following string is given as input to the program:
#
# rise to vote sir
#
# Then, the output of the program should be:
#
# ris etov ot esir
#
# Hints:
# Use list[::-1] to iterate a list in a reverse order.


def print_s_reverse():
    s = input('Enter string: ')
    print(s[::-1])


# -----------------------------------------
# Question 90
# Please write a program which accepts a string from console and print the characters that have even indexes.
#
# Example:
# If the following string is given as input to the program:
#
# H1e2l3l4o5w6o7r8l9d
#
# Then, the output of the program should be:
#
# Helloworld
#
# Hints:
# Use list[::2] to iterate a list by step 2.


def iter_lst_stp_2():
    s = input('Enter string: ')
    print(s[::2])


# -----------------------------------------
# Question 91
# Please write a program which prints all permutations of [1,2,3]
#
# Hints:
# Use itertools.permutations() to get permutations of list.


def permute_lst(l):
    import itertools
    print(list(itertools.permutations(l)))


# -----------------------------------------
# Question 92
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many
# chickens do we have?
#
# Hint:
# Use for loop to iterate all possible solutions.


def solve_puzzle(nheads, nlegs):
    for i in range(nheads + 1):
        if i * 2 + (nheads - i) * 4 == nlegs:
            return i, (nheads - i)
    return None, None


if __name__ == '__main__':

    # Question 51
    # -----------
    # square = Rectangle(2,2)
    # print(square.area())

    # Question 52
    # -----------
    # square = Square(3)
    # print(square.area())

    # Question 53
    # -----------
    # raise RuntimeError('something wrong')

    # Question 54
    # -----------
    # div_by_zero()

    # Question 55
    # -----------
    # error = MyError('something wrong')

    # Question 56
    # -----------
    # get_user_from_email()

    # Question 57
    # -----------
    # get_company_from_email()

    # Question 58
    # -----------
    # find_digits_in_sentence()

    # Question 59
    # -----------
    # print_unicode_str()

    # Question 60
    # -----------
    # compute_seq_divisions(5)

    # Question 61
    # -----------
    # print('Result of recursive function: ', calc_recursiv(5))

    # Question 62
    # -----------
    # print('Result of Fibonacci calulation: ', fibonacci(7))

    # Question 63
    # -----------
    # print_fibonacci_seq(7)

    # Question 64
    # -----------
    # print_evens_in_range()

    # Question 65
    # -----------
    # print_divby5_7_in_range()

    # Question 66
    # -----------
    # check_list_evens([2,4,6,8])

    # Question 67
    # -----------
    # simpe_math_calc()

    # Question 68
    # -----------
    # sl = [1,2,3,6,9,13,45,89,98,122]
    # indx = binary_search(sl, 98)
    # print('Index: ', indx, ' Item: ', sl[indx] if indx is not None else 'not found')

    # Question 69
    # -----------
    # print(rand_10to100())

    # Question 70
    # -----------
    # print(rand_from_range(0, 10))

    # Question 71
    # -----------
    # print(rand_from_range2(0, 100))

    # Question 72
    # -----------
    # print(rand_k_nums_from_range(100, 200, 5))

    # Question 73
    # -----------
    # print(rand_5_from_range(1, 1000))

    # Question 74
    # -----------
    # print(rand_int_in_range(7, 15))

    # Question 75
    # -----------
    # cmpress_decomprs()

    # Question 76
    # -----------
    # time_the_f()

    # Question 77
    # -----------
    # lst = [3, 6, 7, 8]
    # list_shuffle(lst)

    # Question 78
    # -----------
    # sentence_generator(["I", "You"], ["Play", "Love"], ["Hockey", "Football"])

    # Question 79
    # -----------
    # print_remove_evens([5, 6, 77, 45, 22, 12, 24])

    # Question 80
    # -----------
    # print_remove_div_by5n7([12, 24, 35, 70, 88, 120, 155])

    # Question 81
    # -----------
    # print_lst_remove_at_position([12, 24, 35, 70, 88, 120, 155])

    # Question 82
    # -----------
    # print(gen_list_3d_array(3, 5, 8))

    # Question 83
    # -----------
    # print_remv_at_posit([12, 24, 35, 70, 88, 120, 155], [0, 4, 5])

    # Question 84
    # -----------
    # print_l_rm_val([12, 24, 35, 24, 88, 120, 155], 24)

    # Question 85
    # -----------
    # print(intersect([1, 3, 6, 78, 35, 55], [12, 24, 35, 24, 88, 120, 155]))

    # Question 86
    # -----------
    # print(rmv_lst_dublicts([12, 24, 35, 24, 88, 120, 155, 88, 120, 155]))

    # Question 87
    # -----------
    # a_Male = Male()
    # a_Female = Female()
    # print(a_Male.getGender())
    # print(a_Female.getGender())

    # Question 88
    # -----------
    # char_freq_strng()

    # Question 89
    # -----------
    # print_s_reverse()

    # Question 90
    # -----------
    # iter_lst_stp_2()

    # Question 91
    # -----------
    # permute_lst([1, 2, 3])

    # Question 92
    # -----------
    print(solve_puzzle(35, 94))