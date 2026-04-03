# Questions week 1

#1 What is a variable, why is it used?
#Answer: when you give a name to a value, and store that value for later use

#2 How do you differentiate the type of an integer and a string?
#Answer: An integer is a number, whilst strings are marked with " and cannot be calculated.

#3 How do you test the type of a variable?
# Answer: Run       print(type(variable ex.a))

#4 How is "multiple assignment" used, give example
#Answer: Name multiple variables simultaniously.    person1, personb = "zineb", "mariam"

#5 what is end="" used for?
#Answer: used during print("", end= "") ,what is printed after the command will appear at the same line

#6 what is the opposit to "end=" command
#Answer: \n, so each statement prints on a new line. print("Hello\nWorld\nHow are you?")

#7 What are these type of characters called, can you give more examples?
#Answer: Escape characters, ex. \t inserts like pressing a tab key, \\ lets you print one backlash character, \" and \' let you include quotation marks inside strings,\"hello!\"", \b backspace deletes one charachter backward, \a bell - *may play a sound on some systems, /r carriage returs reset the cursor to the beginning of line and prints the word after command again. It keeps printing over the same line, creating an animation-like effect.

#8 What and How is "input()" command used?
#Answer: asks the user to type something, and it stores that input as a string. name = input("What is your name? ") print("Hello, " + name + "!"). You can use it with int or float to get numbers.

#9 What is an f-string, and how is it used?
#Answer: Formatted string , tells program to insert VALUE of variable directly inside string using {}. value = 3.14159 print(f"{value}")

#10 How do you round numbers with f-strings?
#Answer: using ":.2f)" inside the curly bracets. value = 3.14159 ,print(f"{value:.2f}"). :.2f means round to 2 decimal places

#11 How do you specify how many space characters the answer is going to be printed out on with f-strings?
#Answer: using this syntax f"{value:width}". ex. print (f"{name:10}!") will give you space between name and ! You can also use padding with 0:s for numbers to fill upp space. print (f"{number:05}"). Program will use 5 spaces and those not used will be padded with 0:s.

#12 How can adding allignment symbols in f-strings, be used for neater looks?
#Answer: print(f"{value:<10}") — Left-align (default for strings). print(f"{value:>10}") — Right-align (default for numbers). print (f"{value:^10}") — Center-align.

#13 What does adding "=" after variable in f-string do?
#Answer: prints both the variable name and its value , print (f"{i=}")

#14 What is difference between numerical operands and numerical expressions?
#Answer:Operands are the values or variables involved in a calculation ex. In 3 + 4, the operands are 3 and 4. An expression is a combination of operands and operators (like +, -, *, /) that produces a value. Together they form an expression.

#15 Why do we need to import the math module, give example of how it works?
#Answer: there are Pythons built in functions of basic math but for more advanced mathematical operations we need to import the math module. import math - number = 16 - square_root = math.sqrt(number) - print(square_root)

#16 What can we use to skip writing .math all the time?
#Answer: use: from math import sqrt, pi etc. print(sqrt(16)) ,print(pi)

#17 How can you print empty line in python?
#Answer: print ()

#18 what is important to remember for shorter code?
#Answer: use multiple parenthesis print(math.sqrt(math.cos(math.radians(45))))

#19 "You need to store the "newer/calculated value of x" in a variable before using it, so you get the updated verion of x" Give an example of how its done
#Answer:
# wrong version:
# x = 10
# x * 2         # You dubbled it, but didn’t store it
# print(x)

# right version:
# x = 10
# dubble_x = x * 2     # Store the updated value back in x
# print(dubble_x)

#20 print ("Hello"+123) gives you error, write a correct version, according to PEP8
#Answer: print("Hello", 123)

#21 What is PEP, and PEP8?
#Answer: It’s a document that suggests new features, improvements, or guidelines for the Python language. PEP8 tells you how to write clean, readable, and consistent Python code.

#22 Explain the other built in Aritmetical operations: //, ‰ and **
#Answer:// gives us exact value of a calculation, % give us the remainder after division, ** a number (= to the power of) a second number

#23 How to use // and ‰ together?
#Answer:Converting minutes to hours and minutes
# total_minutes = 135

#hours = total_minutes // 60     # 2 hours
#minutes = total_minutes % 60    # 15 minutes

#print(f"{hours} hours and {minutes} minutes")

#24 What does == mean?
#Answer: == compares values, checks if True or False. It’s different from = which is used for assignment (giving a value to a variable).

#25 What is "def" function in Python? And what is it used for?
#Answer: def is used to define a function. def part1 () tells Python: "Here starts the code for a function named part1. The () after the function name can hold parameters (inputs), or be empty. Used to To organize code into reusable blocks, To avoid repetition, To make code easier to read and maintain. To run the only desired part type part1() at the end

#26 Program that calculates an items price, incl. tax.. The tax is in percent-format (%) and 25.5% of the items value. The result is printed in a neat way.
#Answer: see #2Notes.py

#27 Program that reads the inserted number of seconds into a variable called "time". Input should be an Integer, representing total number of seconds. The program calculates how many hours,minutes and secondsthis corresponds to. Number of minutes and seconds should be only between 0-59.
#Answer: see #2Notes.py

#28 Explain the "random" module, and how it is used. random, randint, choice, shuffle
#Answer: It’s a built-in Python module that lets you generate random numbers or make random choices. Useful for games, simulations, testing, and anywhere you need unpredictability.
# First import ramdom
#random.uniform (a,b) gives random number between a<x<b
#random.randint (a,b) gives random integer number a<x<b
#random.shuffle (lis) shuffles the elements in the list lis
#random.sample (sek,n) gives a list with n numbers of random elements from sequence sek

#29 What is an augmented assignment
#Answer: It’s a shortcut way to update the value of a variable by combining an operation and assignment in one step. Instead of writing something like x = x + 5, you can write x += 5.
#x = 10
#x += 5      # Same as x = x + 5
#print(x)    # Outputs 15

#30 What does it mean that Python is an dynamically typed language
#Answer: variables don´t have a fixed type. The type of the value a variable holds is determined at runtime. The type of x can change during the program.
# x= 5       x is an integer
# x= "hello"        x is now a string

#31 What is pyright in Python used for?
#Answer : is a typechecker, controls if the types used in program correctly. By running > pyright filename.py


