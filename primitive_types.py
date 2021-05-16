import math
student_count = 1000
rating = 4.99
is_published = False
course_name = "python programming"
print(len(course_name))
print(course_name[0])
print(course_name[0:-1])
print(course_name[:-1])
print(course_name[0:3])
print(course_name[:3])
print(course_name[:])
# Formatted string : we can put any valid expressions in
#  between the curly braces
first = "Madhurjya"
last = "Saha"
full_name = f"{first} {3+2}"
print(full_name)
# String Methods
course = "Python Programming"
print(course.upper())
# .upper() transforms all the characters in the string to upper case.
print(course.lower())
# .lower() transforms all the characters in the string to lower case.
print(course.title())
# .title() transforms only the first character of every string into capital.
print(course.strip())
# .strip() removea the white space from the begining or the end of the strings.
print(course.lstrip())
# .lstrip() removes the white space from begin of the string.
print(course.rstrip())
# .rstrip() removes the white space from the end of the string.
print(course.find("pro"))
# .find() is used to find the index of the characters mentioned in double quotes.
print(course.replace("P", "j"))
# .replace() is used to replace a character or a sequence of a character with something else.
print("Pro" in course)
# [in] is an operatoe that is used to find existence of a character if its
# we will get a boolean value True and if its not there it will return False.
print("swift" not in course)
# [not in] confirms that the charcters are there or not in the string if its there
# it will return False if its not there it will return True.
print("Pro" not in course)
# the above code returned False as the characters "Pro" is there in the string


# In python we have three types of numbers integers [x = 1]
#  , floats [x = 1.1]
#  & complex numbers [x = a + bj] where j is imaginary
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
# we get a floating point number by the division so if we want an integer we
# need to add // instaed of /
print(10 // 3)
print(10 % 3)
# % is used to find the remainder of a division
print(10 ** 3)
# ** is used as exponent which is left to  the power of right

x = 10
x = x+3
print(x)
# the above code is same as the argumented sign operator shown below
x = 10
x += 3
print(x)
# we can use all the above operator as argumented signs for eg. *= , /= ,**=


# FUNCTIONS FOR NUMBERS
print(round(2.9))
# [round] is used to round up numbers
print(abs(-2.9))
# [abs] returns the absolute value of a number like posetive 2.9 instead of -2.9
print(math.ceil(2.2))

# TYPE CONVERSION
x = int(input("x: "))
y = x + 1
print(y)

x = input("x: ")
print(type(x))

# Falsey values for bool(x)
# "" empty strings are counted as Falsey
# 0 counted as Falsey
# None counted as Falsey
print(bool(""))
