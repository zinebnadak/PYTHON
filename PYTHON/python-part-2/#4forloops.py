#For-loops

#1 Write a program that reads in the last integer (n) and calculates sum, 1+4+9+16+...+n^2, but this time use for-loop instead of while loop.
n = int(input("Enter value of n, to calculate sum of squares from 1-n: "))
sum = 0

for i in range (1,n+1,1):  #here it actually starts from 1 and not 0 when run
    sum = sum + (i*i)
print(f"Sum of squares from 1 to {n} is: {sum}")

#2 For loop: the program calculate the value of the expression 2*(x**2)-5*x+1 for each value of x in the range -10 to 10, and prints result in a neat way.
print (f"{"x":<4}{"Result":<10}")
for x in range (-10,11,1):
    result = 2*(x**2)-5*x+1
    print (f"{x:<4}{result:<10}")

#3 While loop: the program calculate the value of the expression 2*(x**2)-5*x+1 for each value of x in the range -10 to 10, and prints result in a neat way.

print (f"{"x":<10}{"Result":<10}")
x = -1.1            #start from -1.1 bcs loop immediately adds 0.1, so the first value of x printed is -1.0.
while x<0.9:           #end at 1.0
    x = x+0.1
    result = 2 * (x ** 2) - 5 * x + 1
    print(f"{x:<10.2f}{result:<10.2f}") #increase x before printing makes you need to make from -1.1 instead of -1.0, and 0.9 istead of just 1.0

#compare
print (f"{"x":<10}{"Result":<10}")
x = -1.0            #start from -1
while x<1.0:           #end at 1.0
    result = 2 * (x ** 2) - 5 * x + 1   #OBS! always need to define terms BEFORE printing
    print(f"{x:<10.2f}{result:<10.2f}")
    x = x+0.1          #runs one time THEN adds 0.1


#4. Nested loops: program that lets user choose number of rows that are going to be printed and for every row prints one more "+" sign is going to be printed, starting with one "+" sign at row one.
rows = int(input("Enter number of rows to be printed: "))

for i in range (1,rows+1,1):      # range controls number of rows. Includes start but excludes stop thats why you need +1
    for x in range (1,i+1,1):     # range controls "+" signs printed, depends on the row number
        print ("+", end="")     # end="" prints plus without newline, bcs print automatiallt creates a new line
    print()                     # after finishing a row, first NOW go to new line

#5 Now reverse it : desired number of rows = number of "+" signs to be printed on first line
rows = int(input("Enter number of rows to be printed: "))

for i in range (rows+1,1,-1):      # range controls number of rows.
    for x in range (1,i,1):     # range controls "+" signs printed, depends on the row number,not now it prints i-1 number of "+" signs. bcs when i = rows+1 in outer loop, the inner loop prints (rows+1)-1 = rows plus signs → correct first row length. Remember!: The system always includes first but excludes last, so always keep an eye on what the last number is included or not!
        print ("+", end="")     # end="" prints plus without newline, bcs print automatiallt creates a new line
    print()

#6 User gets to choose how big the number can possibly be and times of tries user gets.
# Program "thinks" of a random number within 1 and the users choice.
# User must guess number.
# If user guesses too big or too little the program will let user know.
# Check if the user has won or run out of attempts: The program will stop once the user guesses the correct number or runs out of tries.
# OBS! Ensure that the feedback only happens before the last attempt. After the last attempt, the program will simply print the "Sorry, you've run out of attempts" message without repeating any feedback.
import random

max_number = int(input("Enter max number to guess from (eg. 1-...?): "))
max_tries = int(input("Enter amount of tries: "))

answer= int(input(f"Guess the number between 1 and {max_number}: "))

number = random.randint(1,max_number)

for i in range (1,max_tries,1):               #now the program runs exactly three times
    answer = int(input(f"Guess again! Attempts left {max_tries - i}/{max_tries}"))
    if answer == number:
        print(f"You are right! Contratulations, the number was {number}!")
        break
    elif 1 > answer or answer > max_number:
        print(f"Please guess a number between 1 and {max_number}")
    elif answer > number:
        print(f"Too big!")
    elif answer < number:
        print(f"Too small")

print(f"You are out of tries! The number was {number}! ")


#7Write a program that prints a table for the numbers 1 to 12. On each row of the table, the number should be shown, as well as the number squared and the number cubed.

print ("Tal:\tTalet i kvadrat:\tTalet i kubik:")
for i in range (1,12+1,1):
    print (f"{i:<6}\t{i**2:<16}\t{i**3:<}")


#8Write a program that displays a multiplication table according to the following model. The program should be designed so that you read in the number of rows to be printed. Tip: Use nested for-loops.
#1   2   3   4   5   6   7   8   9
#2   4   6   8  10  12  14  16  18
#3   6   9  12  15  18  21  24  27
#4   8  12  16  20  24  28  32  36
#5  10  15  20  25  30  35  40  45
#6  12  18  24  30  36  42  48  54
#7  14  21  28  35  42  49  56  63
#8  16  24  32  40  48  56  64  72
#9  18  27  36  45  54  63  72  81


rows = int(input("Enter number of desired rows: "))

for i in range (1,rows+1,1):            #controlls number of rows
    for j in range (1,rows+1,1):           #controlls number through row
        print(f"{i*j:^3}", end="")                  #loop variable number (j) * row number (i). alignment the number "{:^3)"
    print()

#9. use Boo1 (Boolean).Is used when you want to check conditions (yes/no, on/off, 1/0). A Boolean is a data type that can only be True or False
#Write a program that asks the user for their age and checks if they are old enough to vote (let’s say 18+). Program will always ask "Can vote?" after your input and answer True/False with the bool next to it automatically

age = int(input("Enter your age: "))
can_vote: bool = age >= 18

print (f"Can you vote? {can_vote}")  #can_vote is printed in True or False (bool)

# age >= 18 is a comparison that returns either True or False.
# If age is 18 or more → True
# If age is less than 18 → False
# can_vote stores that result.


#10 Improve "Merry-go-round" by adding a nested loop so that: The program only accepts y or n as valid input. If the user enters anything else, print an error message and repeat the question: Go again? (y/n)o

# First prompt
while True:
    answer = input("🎠 WELCOME to Merry-go-round! Start? (y/n): ").lower()
    if answer == "y":
        break               #exit loop and jump to next while-loop
    elif answer == "n":
        print("Goodbye! 👋")
        exit()
    else:
        print("❌ Invalid input. Please enter y or n.")

# Loop: only show "Merry go around!" from here on
while True:
    print("Merry go around!")

    while True:
        answer = input("Go again? (y/n): ").lower()
        if answer == "y":
            break  # Repeat the outer loop "Merry go again"
        elif answer == "n":#11 Write a program that prints the first five multiplication tables (1×1 to 10×5). Use a nested for-loop.
            print("Ok, bye 👋")
            exit()
        else:
            print("❌ Error! Please answer y or n.")


#11.Write a program that prints the first five multiplication tables (1×1 to 10×5). Use a nested for-loop.
#Write a program that prints the first five multiplication tables (1×1 to 10×5). Use a nested for-loop.

for i in range (1,5+1,1):        #rows

    for j in range (1,10+1,1):   #numbers 1-10

        print(f"{i}x{j}={i*j}",end="\t")       #row number * current loop number j, print all on same line, tab spacing after each loop for alignment

    print()                       #new row after loop j finish

   
# Ask the user to enter a sentence. Use split() to separate the words and print each word on a new line.
sentence = input("Enter a sentence: ")
words = sentence.split()

print("Here are the words in your sentence:")
for i in words:
    print(i)









