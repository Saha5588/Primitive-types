# CONDITIONAL STATEMENT
# Here after every if conditional statement we have to give :[colon] so that
# the next line of the code is intended
temperature = 25
if temperature > 30:
    print("its warm")
    print("drink some water")
elif temperature > 20:
    print("its nice")
else:
    print("its cold")


# TERNARY OPERATOR
age = 17
if age >= 18:
    print("eligible")
else:
    print("not eligible")
# or you we can do the same thing in a differnet way
age = 23
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)
# hence it worked now we can write the whole conditional statements in a single line
age = 18
message = "Eligible" if age >= 30 else "Not Eligible"
print(message)
# the above code gave the required output that we needed
cgpa = 95
statement = "qualified" if cgpa >= 70 else "not qualified"
print(statement)


# LOGICAL OPERATOR
# and
# or
# not


# and operator
high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

# or operator
high_income = True
good_credit = False
student = True
if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligble")
# when its student is True the not student becomes False so its not eligible
# but when student is False the nopt student becomes True so its eligible

# not operator
no_symptoms = True
negative_report = False
asymptomatic = True
if (no_symptoms or negative_report) and not asymptomatic:
    print("CAN BOARD AIRCRAFT")
else:
    print("NOT ALLOWED TO BOARD AIRCRAFT")
# when asymptomatic is True the not asymptomatic becomes False so it gives the
# message as NOT ALLOWED TO BOARD AIRCRAFT
# when asymptomatic is False the not asymptomatic becomes True and hence it
# gives the meassage CAN BOARD AIRCRAFT

covid_posetive = True
if not covid_posetive:
    print("yes allowed")
else:
    print("not allowed")
# when covid_posetive is True then the not covid_posetive becomes False and
# it says not allowed
# when covid_posetive is False then the not covid_posetive statment becomes
# True and hence it says yes allowed
# Airline Pilot Job
ground_training = True
cpl = True
A320_type_rating = True
B737_type_rating = False
proper_eyesight = False
having_specs = True
smoker = False
if (ground_training and cpl and (proper_eyesight or having_specs) and (A320_type_rating or B737_type_rating)) and not smoker:
    print("YOU ARE HIRED AS 1ST OFFICER")
else:
    print("PLEASE WORK ON YOUR SKILLS")

# SHORT-CIRCUIT EVALUATION
high_income = True
good_credit = False
student = False
if high_income and (good_credit or not student):
    print("Eligible")
else:
    print("Not Eligble")
# here in these code the python code checks for the first boolean value if its
# True or False and if True it stops processing the code there and continues
# to print the final output as per condition
# but if the first boolean value is False then python expects the seconed boolean
# value to be True and continues so on


# CHAINING COMPARISON OPERATORS:-it is used to write a clean code rather than
# mentioning logical operators
# Q] age should be between 20 to 70
age = 55
if 20 <= age < 70:
    print("eligible")

 # QUIZ
if 10 == "10":
    print("a")
elif"bag" > "apple" and "bag" > "cat":
    print("B")
else:
    print("c")


# FOR LOOPS
# for loops are used to repeat things like we send messages as long as it doesnt
# gets delivered
# ages here we have taken an example
# we want to repeat the message 3 times thats why we write range(3) and an
# intendetion after the line like if statement.
# and the range is divided into three parts those are [start,stop,step]
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# FOR ELSE
# Considering the fist scinario we now want the message to be send at the
# very first attempt and if not we wont wait for its three attempts but we
# will terminate the process and we will try to display a message to the user
successful = True
for number in range(1, 4):
    print("Attempt", number)
    if successful:
        print("successful")
        break
else:
    print("Attempted three times but failed")

# NESTED LOOP
# This loops are used to store one loop under another loop so that we can
# get some interesting results.

for x in range(2):
    for y in range(3):
        print(f"{x}, {y}")
# for this code we have to see x as an outer loop and y as an inner loop
# here python interpreter works in a very different way it opens the outer
# loop and then starts executing the inner loop like here it once the outer
# loop is open all it comes as value of {x} is 0 till it reaches the end of
# the range{y} as 3. Then after getting the last value it goes back to the
# outer loop again and stars the loop until it reaches the end of the inner loop

# WHILE LOOPS
X = 0
while X < 5:
    print(f"The current value of {X}")
    X = X + 1


# ITERABLES
print(type(5))
print(type(range(5)))

# PRACTICE
for number in range(1, 4):
    print("attempt", number, number * ".")

for x in range(3):
    for y in range(5):
        for z in range(7):
            print(f"{x}, {y}, {z}")
successful = False
for number in range(1, 4):
    print("Attempt", number)
    if successful:
        print("successful")
        break
else:
    print("Attempted three times but failed")
for x in "python":
    print(x)
# write a code to show even numbers between 1 to 10 and show a message at the
# end that We have 4 even numbers
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")

for num in range(2, -5, -1):
    print(num, end=", ")

#
x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
#
a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')
