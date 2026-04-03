#1 #Write a program that reads in integers n and calculates sum, 1+2+3+4+...+n

n = int(input("Enter value of n: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

print (f"Sum of integers up to {n} is {sum}")

#2 Write a program that reads in integers n and calculates sum, 1+4+9+16+...+n^2
print()

n = int(input("Enter value of n: "))

sum = 0
z = 1

while z <= n:
    sum = sum+(z*z)
    z = z+1

print (f"Sum of squared integers up to {n} is {sum}")

#3 Suppose a ball is dropped onto a floor and with each bounce it loses 30% of its height. Write a program that calculates how many times such a ball bounces before it comes to rest. (By “comes to rest,” we mean that it no longer bounces higher than 1 cm.) As input, the program should let the user specify the height, measured in meters, from which the ball is dropped.
height = float(input("Enter the height the ball is dropped from (in meters): "))
original_height = height # save the starting height so that When you run your code, you’re not printing height at the end
bounces = 0

while height >= 0.01:
    height = height * 0.70
    bounces = bounces + 1

print(f"If you drop a ball from {original_height} it will bounce {bounces} times before stopping!")


#4 Write a program that lets you choose your goal, and by entering your daily salary lets you know how many days it will take you to surpass you goal
salary = float (input("Enter your daily salary: "))
goal = float(input("Enter your goal: "))

current_day = 1
total_money_so_far = salary

while total_money_so_far<goal:
    total_money_so_far=total_money_so_far+salary
    current_day=current_day+1

years=current_day // 365
days=current_day % 365

print(f"For you to reach {goal}€, you´ll have to work {years} years and {days} days!")


#5 Write a program that lets the user specify a multiplication table and then prints it out. Use a while loop.

table = int(input("Enter desired multiplication table: "))

variable = 1
answer = table

while variable>table:
    answer=variable*table
    variable=variable+1

    print (f"{variable}*{table}={answer}")

#6 Write a program that lets the user specify a multiplication table and then prints it out. Use a while loop.

table = int(input("Enter desired multiplication table: "))
variable = 0
while variable <= table:
    while variable < 9:
        variable = variable + 1
        answer = variable * table
        print(f"{variable}*{table}={answer}")

#7 Suppose that the grade in a course is determined by a number of assignments. The maximum score on each assignment is 10 points. If, for example, there are 4 assignments, each assignment will contribute 25% of the total grade. Write a program that lets the user enter scores for a student and then calculates the total percentage. Use a while loop to read the scores from the assignments. The loop should update a variable that contains the sum of the scores entered so far. The program should allow the user to enter scores until the letter ‘a’ is entered. We assume that the user only enters numerical values between 0–10, and ‘a’.
print ("Enter points for student, end with \"a\": ")

Assignment = 1          #first Assignment number
points = 0              #No input from user yet
Total_points = 0        #No calculations of sum of points yet


points = input(f"Assignment {Assignment}: ")            #read input as a string

while points != "a":
    points = int(points)                #covert safely to integer to do calculations ,only if input is not "a"
    Total_points = Total_points + points

    Assignment = Assignment +1
    points = input(f"Assignment {Assignment}: ")

Max_ponits = (Assignment-1)*10
Score_percentage = (Total_points/Max_ponits)*100

print()
print (f"Totalpoints: {Total_points}/{Max_ponits} or {Score_percentage}% ")

#for more efficient code use while True and break statement
print ("Enter points for student, end with \"a\": ")
Assignment = 1
Total_points = 0

while True:
    points = input(f"Assignment {Assignment}: ")           #will ask this to user forever
    if points == "a":                                      #breaks if user enters "a", if not...
        break
    points = int(points)                                   #convert user input to integer to make calculations
    Assignment = Assignment + 1                            #next assignment updates number
    Total_points = Total_points + points                   #updated counter to users input

Max_ponits = (Assignment-1)*10                             #Assignment-1 to not count with assignment when user enters "a",  each assignment max 10 points.
Score_percentage = (Total_points/Max_ponits)*100           #score in percentage

print()
print (f"Totalpoints: {Total_points}/{Max_ponits} or {Score_percentage:.0f}% ")      #result printed in end

#8 Write a program that prints the first five multiplication tables (1×1 up to 10×5). Use a nested while loop.
table = 1  # start from table 1
result = 0

while table <= 5:  # controls table
    variable = 0  # reset variable for each table

    while variable <= 9:  # controls variable
        variable = variable + 1
        result = variable * table
        print(f"{variable} * {table} = {result}")
    print()  # blank line after each table
    table = table + 1       #By placing table = table + 1 after the inner loop, the outer loop will: Start with table = 1, Run the inner loop for table = 1, Then increment → table = 2.



#9 Number Guessing Game: Pick a secret number in your code. Ask the user to guess a number until they get it right. Stop the loop immediately when the correct number is guessed (use break).
secret_num= 3

guess = int(input("Guess the secret number from 1-10: "))           #the first question is only asked once like this

while True:
    guess = int(input("Guess again!: "))                            #the second question is different than the first if user don´t get it right, question inside loop repeats.
    if guess == secret_num:
        break

print(f"Congratulations! The secret number was {secret_num}!")



#10 Odd Numbers Printer: Start counting from 1 up to 20. Use a loop to go through the numbers. Skip printing even numbers (use continue). Only print the odd numbers.
i=0

while i<20:
    i = i + 1
    if i%2==0:
        continue
    print(i)






















#+ se on några av "merforwhile" filen kan lösas med while