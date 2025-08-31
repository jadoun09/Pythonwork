#  How take input from the user
# 1. Using input() function - This function is use to give values to the function/variables. Its like what we are asking the user to enter a value
# There are various types of input functions in python. The most common one is input() function.
# ** The sign of the program is ended now is when at last in terminal it shows
#    the name of the Flder/File.
#    For Example 
# name = input ("enter your name:")
# print("Welcome", name)
# in outpot when we provide name to the system it will show the output as:
# Welcome Abhishek Singh PS D:\Education\Python Developer> ((This menas that program is ended here because now the folder name is displaying at the end))

# NOTE - The input function always takes the input in string format. So if you want to take the input in any other format, you have to convert it into that format.
# HOW TO CONVERT THE INPUT INTO OTHER FORMATS
# We use type casting 
# Type Casting - It is the process of converting one data type into another.
# There are different types of type casting in python. The most common ones are:
# For Example : 
# int ("5")
# val = float(input("enter soem value "))
# print(type(val))
# Output -> enter soem value 25
#           <class 'float'>
#           PS D:\Education\Python Developer> 

#  Question: Write a Program to input 2 numbers and print their sum.
a = float (input("Enter first number :"))
b = float (input("Enter second number :"))
sum = a + b
print("The sum of", a, "and", b, "is", sum)












