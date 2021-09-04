# Question 20
# Level 3
#
# Question:
# Define a class with a generator which can iterate the numbers, which are
# divisible by 7, between a given range 0 and n.
#
# Hints:
# Consider use yield


def gen_divby_svn(rangeupper):
    for i in range(rangeupper):
        if not i%7:
            yield i


# ------------------------------
# Question 21
# Level 3
#
# Question:
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after
# a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

from math import sqrt

def get_robot_moves():
    moves = []
    while True:
        move = input('Enter robot moves (Direction Steps): ')
        if move:
            moves.append(tuple(move.split()))
        else:
            break

    return moves


def distance_calc(moves):
    point = [0,0]
    for move in moves:
        if move[0] == 'UP':
            point[1] += int(move[1])
        elif move[0] == 'DOWN':
            point[1] -= int(move[1])
        elif move[0] == 'LEFT':
            point[0] -= int(move[1])
        else:
            point[0] += int(move[1])

    return sqrt(point[0]**2 + point[1]**2)


# -----------------------------------------
# Question 22
# Level 3
#
# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
#
# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.


def get_txt_usrinpt():
    lines = []
    while True:
        line = input('Enter line input: ')
        if line:
            lines.append(line)
        else:
            break
    return lines


def create_wordfreq_dict(content):
    d = {}
    if len(content) > 0:
        try:
            for line in content:
                for w in line.rstrip().split():
                    d[w] = d.get(w,0) + 1
        except:
            for w in content.rstrip().split():
                d[w] = d.get(w, 0) + 1
    else:
        return None
    return d


def pprint_lst_or_dict(arrayinpt):
    try:
        a = sorted([(k,v) for k,v in arrayinpt.items()])
        for x, y in a:
            print('{}:{}'.format(x, y))
    except Exception as e:
        print('In exception: ', e)


# -----------------------------------------
# Question 23
# level 1
#
# Question:
#     Write a method which can calculate square value of number
#
# Hints:
#     Using the ** operator


def calc_num_square(num):
    """Return the square value of the input number.

    The input number must be integer.
    """
    try:
        return num**2
    except:
        print(num, 'Is not a number...')
        return None


# -----------------------------------------
# Question 24
# Level 1
#
# Question:
#     Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
#     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#     And add document for your own function
#
# Hints:
#     The built-in document method is __doc__


def pfunc_doc(func_to_print):
    # Use exec to convert string to source code.
    exec('print('+func_to_print+'.__doc__)')


# -----------------------------------------
# Question 25
# Level 1
#
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later


class Person:
    # This class variable is common to ALL instances of the class.
    name = 'Person'

    def __init__(self, name = None):
        # self.name here is the instance parameter that is initialized when a new object instance is created.
        self.name = name


# -----------------------------------------
# Question 26:
# Define a function which can compute the sum of two numbers.
#
# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.


def sum_nums(n1, n2):
    return n1 + n2


# -----------------------------------------
# Question 27
# Define a function that can convert a integer into a string and print it in console.
#
# Hints:
#
# Use str() to convert a number to string.

def print_int(n):
    print(str(n))


# -----------------------------------------
# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in
# console.
#
# Hints:
#
# Use int() to convert a string to integer.


def print_sumvalues(s1, s2):
    print(int(s1)+ int(s2))


# -----------------------------------------
# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.
#
# Hints:
#
# Use + to concatenate the strings


def print_str_concat(s1, s2):
    print(s1+s2)


# -----------------------------------------
# Question 30
# Define a function that can accept two strings as input and print the string with maximum length in console. If two
#  strings have the same length, then the function should print al l strings line by line.
#
# Hints:
#
# Use len() function to get the length of a string

def pr_longest_str(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    else:
        print(s2)


# -----------------------------------------
# Question 31
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is
# even, otherwise print "It is an odd number".
#
# Hints:
#
# Use % operator to check if a number is even or odd.


def tell_even_odd(n):
    if n%2:
        print('It is an odd number')
    else:
        print('It is an even number')


# -----------------------------------------
# Question 32
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the
# values are square of keys.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

def pr_dict():
    d = dict()
    d[1] = 1
    d[2] = 2**2
    d[3] = 3**2
    print(d)


# -----------------------------------------
# Question 33
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the
# values are square of keys.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.


def pr_dict_loop():
    d = {}
    for key in range(1, 21):
        d[key] = key**2
    print(d)


# -----------------------------------------
# Question 34
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
# values are square of keys. The function should just print the values only.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


def pr_vals_dict_loop():
    d = {}
    for key in range(1, 21):
        d[key] = key**2
    for k, v in d.items():
        print(v)


# -----------------------------------------
# Question 35
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the
# values are square of keys. The function should just print the keys only.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


def pr_keys_dict_loop():
    d = {}
    for key in range(1, 21):
        d[key] = key**2
    for k, v in d.items():
        print(k)


# -----------------------------------------
# Question 36
# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both
# included).
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.


def pr_lst_loop():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst)


# -----------------------------------------
# Question 37
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


def pr_lst_rng():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst[:5])


# -----------------------------------------
# Question 38
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


def pr_lst_rng_last():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst[-5:])


# -----------------------------------------
# Question 39
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

def pr_lst_rng_notfirst():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    print(lst[5:])


# -----------------------------------------
# Question 40
# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both
# included).
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.

def gen_prnt_tpl():
    lst = []
    for i in range(1, 21):
        lst.append(i ** 2)
    print(tuple(lst))


# -----------------------------------------
# Question 41
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last
# half values in one line.
#
# Hints:
#
# Use [n1:n2] notation to get a slice from a tuple.


def tpl_p_halfhalf(tpl):
    print(tpl[0:int(len(tpl)/2)])
    print(tpl[int(len(tpl)/2):])


# -----------------------------------------
# Question 42
# Write a program to generate and print another tuple whose values are even numbers in the given
# tuple (1,2,3,4,5,6,7,8,9,10).
#
# Hints:
#
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.


def evens_from_tpl(tpl):
    lst = []
    for i in tpl:
        if not i%2:
            lst.append(i)
    print(tuple(lst))


# -----------------------------------------
# Question 43
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise
# print "No".
#
# Hints:
#
# Use if statement to judge condition.

def check_yes_str(str):
    if str is 'yes' or str is 'YES' or str is 'Yes':
        print('Yes')
    else:
        print('No')


# --- OR (similar way) ---


def check_yes_str_re(str):
    import re
    if re.match("yes$", str, flags=re.I):  # re.I == re.IGNORECASE
        print('Yes')
    else:
        print('No')


# -----------------------------------------
# Question 44
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
#
# Hints:
#
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.


def filter_even_from_list(unfiltered_list):
    # OR lambda x: x%2 == 0
    return filter(lambda x: not x%2, unfiltered_list)


# -----------------------------------------
# Question 45
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
#
# Hints:
#
# Use map() to generate a list.
# Use lambda to define anonymous functions.


def map_make_squares(inpt_list):
    return map(lambda x: x**2, inpt_list)


# -----------------------------------------
# Question 46
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
#
# Hints:
#
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


def filter_range_nums(n1, n2):
    return filter(lambda x: not x%2, range(n1, n2+1))


# -----------------------------------------
# Question 47
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
#
# Hints:
#
# Use map() to generate a list.
# Use lambda to define anonymous functions.


def map_sqrs_in_range(n1, n2):
    return map(lambda x: x**2, range(n1, n2+1))


# -----------------------------------------
# Question 48
# Define a class named American which has a static method called printNationality.
#
# Hints:
#
# Use @staticmethod decorator to define class static method.

class American:

    @staticmethod
    def printNationality():
        print('American')


# -----------------------------------------
# Question 49
# Define a class named American and its subclass NewYorker.
#
# Hints:
#
# Use class Subclass(ParentClass) to define a subclass.

class NewYorker(American):
    pass


# -----------------------------------------
# Question 50
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute
# the area.
#
# Hints:
#
# Use def methodName(self) to define a method.


class Cirlce:
    def __init__(self, radius):
        self.r = radius

    def circle_area(self):
        from math import pi
        return pi * self.r**2


if __name__ == '__main__':

    # Question 20
    # -----------
    # numsmod7 = []
    # for value in gen_divby_svn(300):
    #     numsmod7.append(value)
    # print(numsmod7)

    # Question 21
    # -----------
    # print('The robot\'s distance is: ', int(round(distance_calc(get_robot_moves()))))

    # Question 22
    # -----------
    # pprint_lst_or_dict(create_wordfreq_dict(get_txt_usrinpt()))

    # Question 23
    # -----------
    # print('Square of {} is {}'.format('5', calc_num_square(5)))

    # Question 24
    # -----------
    # pfunc_doc('abs')
    # pfunc_doc('int')
    # pfunc_doc('input')
    # pfunc_doc('calc_num_square')

    # Question 25
    # -----------
    # christos = Person('Christos')
    # print('{} name is {}'.format(Person.name, christos.name))
    #
    # eleni = Person()
    # eleni.name = 'Eleni'
    # print('{} name is {}'.format(Person.name, eleni.name))

    # Question 26
    # -----------
    # print(sum_nums(3,2))

    # Question 27
    # -----------
    # print_int(13)

    # Question 28
    # -----------
    # print_sumvalues('3', '4')

    # Question 29
    # -----------
    # print_str_concat('3','4')

    # Question 30
    # -----------
    # pr_longest_str('one', 'three')

    # Question 31
    # -----------
    # tell_even_odd(7)

    # Question 32
    # -----------
    # pr_dict()

    # Question 33
    # -----------
    # pr_dict_loop()

    # Question 34
    # -----------
    # pr_vals_dict_loop()

    # Question 35
    # -----------
    # pr_keys_dict_loop()

    # Question 36
    # -----------
    # pr_lst_loop()

    # Question 37
    # -----------
    # pr_lst_rng()

    # Question 38
    # -----------
    # pr_lst_rng_last()

    # Question 39
    # -----------
    # pr_lst_rng_notfirst()

    # Question 40
    # -----------
    # gen_prnt_tpl()

    # Question 41
    # -----------
    # tpl_p_halfhalf((1,2,3,4,5,6,7,8,9,10))

    # Question 42
    # -----------
    # evens_from_tpl((1,2,3,4,5,6,7,8,9,10))
    # evens_from_tpl((13, 12, 14, 16, 20, 40, 32, 11, 9))

    # Question 43
    # -----------
    # check_yes_str('yes')
    # check_yes_str_re('YES')

    # Question 44
    # -----------
    # print(','.join(str(e) for e in filter_even_from_list([1,2,3,4,5,6,7,8,9,10])))

    # Question 45
    # -----------
    # print(','.join(str(e) for e in map_make_squares([1,2,3,4,5,6,7,8,9,10])))

    # Question 46
    # -----------
    # print(','.join(str(e) for e in filter_range_nums(1,20)))

    # Question 47
    # -----------
    # print(','.join(str(e) for e in map_sqrs_in_range(1, 20)))

    # Question 48
    # -----------
    # americano = American()
    # americano.printNationality()
    # American.printNationality()

    # Question 49
    # -----------
    # americano = American()
    # newyorker = NewYorker()
    # print(americano)
    # print(newyorker)

    # Question 50
    # -----------
    c = Cirlce(2)
    print(c.circle_area())