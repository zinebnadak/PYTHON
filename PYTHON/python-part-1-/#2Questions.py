#1 How does the rounding when converting float number to integer work
#Answer: Floats are always rounded downwards :y= 2.7, print(int(y)) gives you 2

#2 Give me two ways to determine the amounts of deciamls in rouded value
#Answer:
# by using round and adding ,1 after variable: _pi = 3.14 - print(round(_pi, 1))
# using f string:_pi =3.14 - print (f"{x:.1f}")

#3 Write a program that calculates Volume V and Area A for a sphere of radius r. Print the values of the variables with a precision of 3 decimal places.
#Answer:
import math
# Be användaren om radien
r = float(input("Ange radien r: "))
# Beräkna volym och area
v = (4 * math.pi * (r ** 3)) / 3
a = 4 * math.pi * (r ** 2)
# Skriv ut resultat med 3 decimalers noggrannhet
print(f"Volymen är: {v:.3f}")
print(f"Arean är: {a:.3f}")

#7 How can you shorten this code to only two lines code?
#data = input("Enter a number: ")
#data = float(data)                 # Converts string "3.14" that input returns to number 3.14
#print("The number is ", data)

#Answer:
#data = float(input("Enter a number: "))
#print("The number is ", data)

^#8 How can you input multiple data, though input only reads in one string of data?
#Answer:
#value1 = input("Skriv in tre värden: ")
#value2 = input()
#value3 = input()
#print("Du skrev in:", value1, value2, value3)

#9 What is split used for, and how to use?
#Answer: splits one string of text into smaller parts. Used to input multiple values on the same string. Used with pointsyntax.  Can combine split with input.
# text = "Hello world this is ChatGPT"
#words = text.split()
#print(words)
#Output:
#['Hello', 'world', 'this', 'is', 'ChatGPT']

^#10 How can you combine split with input?
#Answer:
# answer = input("Enter three values: ")
#value1, value2, value3 = answer.split() 
# print("You wrote:", value1, value2, value3)
#eller
# answer = input("Skriv in tre värden: ").split()
# print("You wrote:", value1, value2, value3)

#11 what does () in ".split()" tell us?
#Answer: the different values of inputs are separated by blank space

#12 How can you change that?
#Answer: by specifying the separator inside the parenthesis
#ex. answer.split(":")        # Specify : as separator with quote sign

#12 For what practical things use split syntax? give example
# For processing using data of ex. time or date.
# Ex. Date:
# answer = input("Enter a time (HH:MM:SS): ")
# hours, minutes, seconds = answer.split(":")  # Specify ':' as separator
# print("You entered:", hours, minutes, seconds)

# 13 Exercise: Write a program that lets the user enter their birthdate in the format DD/MM/YYYY. Use input and split. Store the answer in three separate variables. What happens if the user only enters two values, or uses the wrong separator?
#Answer:

#14 What is sep="  and how is it used inside string?
#Answer: defines the separator that is inserted between the items you're printing.
# print("2025", "08", "25", sep="-")

^#15 Exercise: birthday calculation program. Calculate how old the person has become this year/will be in 10 years
#Answer:
print()
birthdate = input("When were you born? (DD/MM/YYYY): ") #Ask the user for their birthdate in the format DD/MM/YYYY
day, month, year = birthdate.split("/")
todays_year = int(input("What year is it now?:")) #Ask what year it is now
age = todays_year - int(year)   #Calculate how old the person is
print (f"You turned {age} years old {int(day)}/{int(month)}/{todays_year}")#Calculate how old the person has become this year and Print the result using an f-string

#Calculate how old the person will become in specified future year
print()
birthdate = input("When were you born? (DD/MM/YYYY): ") #Ask the user for their birthdate in the format DD/MM/YYYY
age_in_question = int(input("In what year do you want to know your age?:")) # Ask target year

day, month, year = birthdate.split("/") # Split the date into day, month, and year
birth_year = int(year) # Convert year to integer
age_in_that_year = age_in_question - birth_year
print (f"In {age_in_question}, you will be {age_in_that_year} years old!" )


#16 Explain what each symbol in the f-string mean?
#Answer: (f"text1{value:y.x}")
#f = formatted string
#{what:how}
# y.x where x is number of decimals and y is for padding

#17 How is tripple quotes """ used
#ANswer: to create a string that spans multiple lines




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
