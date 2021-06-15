# Creating a function requires a  very specific syntax, including the def keyord,
# correct intendation, and proper struture.
# def name_of_function(): here def keyword standing for the word defination and
# then the name of the function and here by general convention we use under score
# after every word that is called snake casing and all lower case letters in between
# then we have parenthesis so that we can pass arguments and parameters in between
# the parenthesis. Arguments and parameters are just word saying take this varriable
# and pass it into the function in order to work within the function.
# '''   ''' this is the optinal multiline string to describe a function  this is called
# a doc string it doesent get executed defining the work of the function.
# after everything getting intdented we can print the funtiom and call it back by
# calling the name of the function and it wll print the string
#
from random import shuffle
from typing import NamedTuple


def say_hello():
    print("hello")


say_hello()

# now funtions can be a little bit complicated by mentioning the argument or parameter
# the parenthesis in the first line contains the variable which we can call any name
# but we have to change it in the following lines also.


def say_hello(name='default'):
    print(f'hello {name}')


say_hello()
# So in funtions we are actually gonna use the return keyword rather than print
# the main differnece between print and return is in case of return the output is
# going to be saved them as a  varriable


def add_num(num1, num2):
    return num1+num2


message = add_num(10, 20)
print(message)


def print_result(a, b):
    print(a+b)


def return_result(a, b):
    return a+b


result = print_result(10, 20)

result = return_result(10, 20)
print(result)

# suppose you want to print and return the statement simultaniously then after
# the first line you can write both print and return statemnt for e.g


def my_func(a, b):
    print(a+b)
    return a + b


result = my_func(20, 30)
print(result)

# FUNTIONS WITH LOGIC


def even_check_list(number_list):
    for numbers in number_list:
        if numbers % 2 == 0:
            return True
        else:
            pass
    return False


print(even_check_list([5, 9]))


def even_check(num_list):

    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(even_check([2, 3, 4]))
# TUPLE UNPACKING WITH PYTHON FUNCTION
stock_prices = [('APPL', 200), ('GOOGL', 300), ('MOSEFT', 400)]
for item in stock_prices:
    print(item)
for ticker, prices in stock_prices:
    print(prices+(prices*0.1))

students_marks = [('SAM', 60), ('RAJ', 95), ('JOHN', 80)]


def student_check(students_marks):

    passing_marks = 50
    student_of_the_year = ''
    for students_name, marks in students_marks:
        if marks > passing_marks:
            passing_marks = marks
            student_of_the_year = students_name
        else:
            pass
    return(student_of_the_year, passing_marks)


print(student_check(students_marks))

work_hours = [('abby', 100), ('billy', 400), ('cassie', 800)]


def employee_check(work_hours):

    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    return(employee_of_the_month, current_max)


result = employee_check(work_hours)
name, hours = employee_check(work_hours)
print(result)
print(name)
print(hours)


#args and xargs
def my_function(a, b, c=0):
    return sum((a, b, c)) * 0.05


print(my_function(20, 34))

# So here we use  *args after the astrecs sign we can use any arbitary word
# we can say *spam and any word after that astrecs. here args returns
# tuples


def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60, 100, 1, 34))

# here in this code we use ** because it defines a dictionary with its keys
# and its values


def myfunc(**kwargs):
    if "fruit" in kwargs:
        print('My choise of fruit is {}'.format(kwargs['fruit']))
    else:
        print("i did not find any fruit here")


print(myfunc(fruit='apple', veggies='lettuce'))


def myfunc(**jellly):
    if "fruit" in jellly:
        print('My choise of fruit is {}'.format(jellly['fruit']))
    else:
        print("i did not find any fruit here")


print(myfunc(fruit='apple', veggies='lettuce'))


def myfunc(*args, **kwargs):
    print('I would like to have {} {}'.format(args[0], kwargs['snacks']))


print(myfunc(10, 20, 30, fruit='oranges', food='eggs', snacks='chips'))
# **kwargs full form is keyword arguments
# *args are just arguments


def myfunc(*args):
    even_numbers = []
    for numbers in args:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
        else:
            pass
    return even_numbers


print(myfunc(1, 52, 20, 5, 9, 4, 89, 4, 6, 2, 6, 65))


def myfunc(word):
    resulte = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            resulte += letter.lower()
        else:
            resulte += letter.upper()
    return resulte


print(myfunc('abhfbihbad'))

# FUNCTION PYTHON PROBLEM


def myfunc(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(myfunc(4, 6))
# we can clean this up a lot and use min function


def myfunc(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(myfunc(5, 6))

# write a function that takes two word string and returns true if both
# words begin with same letter


def animal_cracker(text):
    wordlist = text.upper().split()

    first = wordlist[0]
    second = wordlist[1]
    return first[0] == second[0]


print(animal_cracker('Levelheaded Llama'))
print(animal_cracker('Crazy cat'))

# Given two intergers, returns True if the sum of the integer is 20 or
# if one of the integer is 20.If not,return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False


def makes_twenty(a, b):
    if a + b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False


print(makes_twenty(5, 10))

# But we can write much cleaner code than this


def makes_twenty(a, b):
    return a + b == 20 or a == 20 or b == 20


print(makes_twenty(10, 10))

# level 1 Problem
# Write a function that capitalize the first and fourth letters of a
# name


def make_capital(name):

    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest


print(make_capital('madhurjyasaha'))
# we can use a capitalize method


def make_capital(name):
    first_half = name[:3]
    seconed_half = name[3:]

    return first_half.capitalize() + seconed_half.capitalize()


print(make_capital('macdonalds'))
# here the name is divided into two halfs and then the first two letters
# are capitalized. capitalize() Converts the first character to upper case

# Given a sentence, return a sentence with the words reversed


def master_yoda(text):
    wordlist = text.split()
    reverse_wordlist = wordlist[::-1]
    return ' '.join(reverse_wordlist)


print(master_yoda('My name is Sunny'))

# Given an integer n , return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(104))


# level 2 problem
# Given a list of ints, True if the array contains a 3 next to a somewhere.
