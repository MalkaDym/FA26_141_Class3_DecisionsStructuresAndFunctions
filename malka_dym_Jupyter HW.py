# MCON 141 — Homework 3
# Class 3 Concepts: if statements and Boolean logic
#
# Name: Malka Dym
# Date: Septeber 24, 2026
#
# DIRECTIONS
# 1. Open this file in Pyzo and save it with your own name in the filename.
# 2. Type your solution directly below each exercise's comment block.
# 3. For every exercise that asks for user input, place the input/conversion
#    statements in a try / except ValueError block.
# 4. Test every solution. If you do not use a function, leave comments stating
#    the additional tests you ran, because only the final run is visible.
# 5. All code must run without errors.
#
# EXTRA CREDIT (up to 2 points)
# Write your solutions inside functions where appropriate. For example:
#
# def check_weather(temperature):
#     if temperature > 80:
#         return "It is hot outside."
#     elif temperature < 60:
#         return "It is cold outside."
#     else:
#         return "The weather is mild."
#
# print(check_weather(75))  # should print: The weather is mild.
# print(check_weather(85))  # should print: It is hot outside.
# print(check_weather(50))  # should print: It is cold outside.


# ================================================================
# Exercise 1: What is x relative to y?
#
# Two variables are named x and y. Set y to 10 and x to 20.
#
# Write an if / elif / else statement that compares x and y:
# - If x is less than y, print: "x is less than y"
# - If x is equal to y, print: "x is equal to y"
# - If x is greater than y, print: "x is greater than y"
#
# In a comment within your code, explain the result and why it occurs.
# Also test at least two other values of x and/or y, and document those tests.
y=10
x=20
if x<y:
   print("x is less than y")
elif x==y:
   print("x equals y")
elif x>y:
    print("x is greater than y")
#result: x is greater than y, why? because we stored x at a greater value
# I tried x=8 y=10, result: x is less than y and I tried x=8 y=8, result: x equals y
# ================================================================
# Exercise 2: Is x odd or even?
#
# Use x = 20 (or define x again so this exercise runs independently).
#
# If x is even, print: "x is even"
# Otherwise, print: "x is odd"
#
# In a comment within your code, explain the result and why it occurs.
# Test at least one odd value as well.
x=20
if x%2==0:
    print("x is even")
else:
    print("x is odd")
#the result of %2 from an even number is 0 and from an odd number is remainder, my result: x is even, since x is stored as an even number. However when I tested the value, I tried a few numbers and when I tested x=21,result: x is odd


# ================================================================
# Exercise 3: Polynomials
#
# Two factors, when multiplied together, can produce a binomial.
# Given (x + a) * (x + b), where a and b are integers:
#
#      x + a
#  *   x + b
# -------------
#        xb + ab
#   x^2 + xa
# -------------
#   x^2 + (xb + xa) + ab
#
# Write a program named polynomial that asks the user for integers a and b,
# then computes and prints the expanded binomial.
#
# Example: (x + 2) * (x + 3) = x^2 + 5x + 6
#
# Remember: x^2 means "x squared."
# Use try / except ValueError for user input.
try:
    a= int(input("enter a:"))
    b= int(input("enter b:"))

    result= (x+a)*(x+b)
    result_2= x^2+(((x)*(b))+((x)*(a)))+((a)*(b))
    if a>=0 and b>=0:
        print("(x+a)*(x+b)=x^2+(((x)*(b))+((x)*(a)))+((a)*(b))")
        print(result_2)
    if a<0 or b<0:
        raise ValueError("We require a positive value")
except ValueError as e:
  print (f"ERROR {e}, the value you entered is negative")



# ================================================================
# Exercise 4: Analyze the polynomial
#
# Given integers a and b, expand (x + a)(x + b) into:
# x^2 + (xb + xa) + ab
#
# Then determine whether:
# - the middle-term coefficient (a + b) is positive, negative, or zero; and
# - the constant (a * b) is positive, negative, or zero.
#
# You may reuse your values of a and b from Exercise 3, but make this exercise
# run independently if possible. Use try / except ValueError for user input.

try:
    a= int(input("enter a:"))
    b= int(input("enter b:"))

    result_2= x^2+(((x)*(b))+((x)*(a)))+((a)*(b))
    print("(x+a)*(x+b)=x^2+(((x)*(b))+((x)*(a)))+((a)*(b))=",result_2)

    if (a+b)>0:
        print("positive coefficient")
    if (a+b)<0:
        print("negative coefficient")
    if (a*b)>0:
        print("positive constant")
    if (a*b)<0:
        print("negative constant")
    if a==0 or b==0:
        raise ValueError("The constant will be zero")
except ValueError as e:
  print (f"ERROR {e},since the value you entered is zero")


# ================================================================
# Exercise 5: Explore the and statement
#
# Ask the user to enter integers val1 and val2.
#
# - If both values are positive, print: "val1 and val2 are positive"
#   and print the values.
# - If both values are negative, print: "val1 and val2 are negative"
#   and print the values.
# - Otherwise, print: "The values are not both positive or both negative"
#   and print the values.
#
# Use try / except ValueError for user input.

try:
    val1= int(input("insert an integer for val1"))

    val2= int(input("insert an integer for val2"))


    if val1 >0 and val2 >0:
        print("val1 and val2 are positive")
        print(val1,val2)
    elif val1<0 and val2<0:
        print("val1 and val2 are negative")
        print(val1,val2)
    else:
        raise ValueError("The values are not both positive or both negative")

except ValueError as e:
    print (f"{e}")





# ================================================================
# Exercise 6: Explore the or statement
#
# Ask the user to enter integers val1 and val2.
#
# - If val1 or val2 is positive, print: "At least one value is positive"
#   and print the values.
# - If val1 or val2 is equal to zero, print: "At least one value is zero"
#   and print the values.
# - Otherwise, print: "At least one value is negative"
#
# Use try / except ValueError for user input.
try:
    val1= int(input("insert an integer for val1"))

    val2= int(input("insert an integer for val2"))

    raise ValueError("Please enter whole numbers")
except:

    if val1 >0 or val2 >0:
        print("At keast one value is  positive")
        print(val1,val2)
    elif val1==0 or val2==0:
        print("At least one value is equal to 0")
        print(val1,val2)
    else:
        print("At least one value is negative")
        print(val1,val2)




# ================================================================
# Exercise 7: Explore not
#
# Set the following variables:
# a = True
# b = True
# c = False
#
# Evaluate and print the results of these expressions:
# 1. not (a and b)
# 2. not a or not c
# 3. not ((a and c) and b)
#
# Include a comment explaining each result.

a= True
b= True
c= False

print(not (a and b)) #result is False, with 'and' if one is false, all are false
print(not a or not c) #'or' works differently- if even one thing is true, it is true
print(not(a and c)and b) #the not is only on the a and c
#the 'not'definitly has an affect on the results

# ================================================================
# Exercise 8: Voting Age and Citizenship
#
# Ask the user for their age and whether they are a citizen (yes or no).
#
# - If they are 18 or older AND a citizen, print:
#   "You are eligible to vote."
# - If they are under 18 OR not a citizen, print:
#   "You are not eligible to vote."
#
# Hint: use and for the eligibility requirements. Use try / except ValueError
# for the age input.
try:
    age= int(input("What is your age?"))
    citizenship=str(input("Are you a citizen? yes/no")).lower()

    if age>=18 and citizenship=="yes":
        print("You are eligable to vote")
    if age < 18 or citizenship=="no":
        raise ValueError("You are not eligable to vote")
except ValueError as e:
    print({e})
else:
  print("Please speak to staff")

# ================================================================
# Exercise 9: Number Classification
#
# Ask the user for an integer.
#
# - If it is positive and even, print: "Positive even number."
# - If it is positive and odd, print: "Positive odd number."
# - If it is negative or zero, print: "Not a positive number."
#
# Hint: combine and and or. Use try / except ValueError for user input.
number= int(input("choose a number"))


if number >=0 or number %2==0:
  print("Positive even number")
elif number>=0 or number %2 > 0:
  print("Positive odd number")
else:
  print("Not a positive number")



# ================================================================
# Exercise 10: Triangle Check
#
# Ask the user for three side lengths: a, b, and c.
#
# Print "Valid triangle." only if all sides are greater than 0 AND:
# - a + b > c
# - a + c > b
# - b + c > a
#
# Otherwise, print "Not a valid triangle."
#
# Hint: chain multiple and conditions. Use try / except ValueError for input.
try:
    a= int(input("enter length a"))
    b= int(input("enter length b"))
    c= int(input("enter length c"))
    length=((a + b) > c) and ((a + c) > b) and ((b + c) > a)

    if a>0 and b>0 and c>0 and length== True:
        print("Valid triangle")
    else: 0>=a and 0>=b and 0>=c
    raise ValueError("Your entered value does not fit the requirement")
except ValueError as e:
    print(f"ERROR {e}, this is not a valid triangle")



# ================================================================
# Exercise 11: Weekend Plan Decision Tree
#
# Ask the user two questions:
# - Is it the weekend? (yes or no)
# - Do you have homework? (yes or no)
#
# Build a decision tree that prints:
# - Weekend and no homework: "Go have fun!"
# - Weekend and homework: "Do your homework first, then relax."
# - Not weekend and homework: "Focus on schoolwork."
# - Not weekend and no homework: "It's a regular day, keep learning!"
#
# Consider converting responses to lowercase so Yes, YES, and yes all work.

weekend= str(input("Is it the weekend? yes or no")).strip().lower()
homework= str(input("Do you have homework? yes or no")).strip().lower()


if weekend=="yes" and homework=="no":
  print("Go have fun!")
elif weekend=="yes" and homework=="yes":
  print("Do your homework first, then relax.")
elif weekend=="no" and homework=="yes":
  print("Focus on schoolwork")
elif weekend=="no" and homework=="no":
  print("It's a regular day, keep learning!")