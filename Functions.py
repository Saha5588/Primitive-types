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