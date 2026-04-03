#TO CHOOSE


#1 What sentence is used for choosing?
#if-command

#2 Write a program that tells you to turn on the heat if the temperature is under 18 degrees
t = float (input("What is the current temperatur?:"))
if t<18:
    print("It is cold, turn on the heat!")

print (f"It is {t:.1f} degrees")

#3 If- sentence is a  "keyword", what else is a keyword?
#import

#4 how does if command work?
# After if-command there needs to be a logical expression after, followed by a ":". Then INSIDE line that tells what to do if the expression is true. The lines of code except if and what is below will always run.

#5 With if command we use many characters like "!=", with equal sign always on the right , what does this mean?
# Not equal to

#6 How do we express either this or this or this using if command, and...?
# if, elif. You can use multiple Elif-parts. Keep in mind to begin the different parts equally in the line as the if command.

#7How to express två alternatives
# with else , is chosen if none of if or elif statements are true

#8Can we add if commands inside if commands?
#yes ofc, but remember to drag the if statement so it is "inside" the main if

#9What is an logic expression, and what is the type of such?
# Expression that is EITHER true or false, type is boo1, we are comparing and using comparing operators like =><! (or logical operators)

#10 What more logical operators are used in logical expressions
# and , or , not
# A and B : true if both are true
# A or B : true if at least one is true
# not A : true if A is false

#11 write a line of code using both comparing operators and logical operators
# not (n==0 or n==100)

#12 why can you combine  comparing operators, logical operators and arithmetic operators without using parenthesis
# Because some operators have higher priority that others
#1 First Arithmetical operators and comparing operators
#2 Then Logical operators
# i + j < k*k and m==n is same as (i+j)>(k*1) and (m==n)

#13 What is speial with haraters "and" "or"
# They are read from left to right, if first is false the second expression is never calculated. Used if you want to avoid to do following calculation if first statement is flase
# k!=0 and

#14 How can you write "1<=x and x<=5" ONLY in Python
# 1 <= x <= 5

#15 How can you create variables with this type boo1?
# billig = True
# barn = False
# billig = pris <= 100
# barn = ålder < 12

#16 There are two cathegories of sentences in python
# simple sentences and compound sentences. The compound sentences can consist of multiple sentences, ex. if/elif/else/for/while-sentences.

#17 what does pass do?
# adds below a command and does nothing

#18 How can you write multiple sentences on the same line?
# using semiolon ;
# a=5 ; b=4 ; =7

# 19 how to continue the same sentence on next row, without actually switching rows?
# use backslash \ at the end of first row

# 20 How can you write this code easier?
# if x > y:
#   z=x        the greater variable will get the name "z"
# else:
#   z=y
#Answer: z = x if x>y else y

#21 What is the act of dragging in code under a for example if-command called?
# To indent


#TO REPEAT
#22 What sentences are used for repeating, and what kind of expressions is combine with them?
# The while-sentence and for-sentence , followed by a logical expression and decides how many times code is repeated. When the logical expression expires and beomes false it exits the loop.

#23 Give an example of a while-loop
# print ("[", end=")
# k = 0         #define variable
#while k<6:     #while + logial expression
    #print (f"{k:2}", end=")        #what will it do if true?
    #k=k+2 or k+=2                  #what will happen each time the loop is started?
#print ("]")

#24 define print("text" ,end=") again!
#Answer:
# #("text" ,end=")
# print("text")         # end=", means no line cchange, and whatever you write next time you call on print will be printed on same line.

#25 What sentence can you use to terminate and exit inside a continous while or for loop?
# use break-sentence, and the program jumps to next sentence after the while-sentence. Used inside if-sentence inside while loop

#26 Give an example when using "While True" and a "break", (combined with if-sentence)
# k = 0
# while True:       #the loop will continue forever
#   print (f"{k:2}", end =")
#   if k>=6:    #when k is bigger or equal to 0 break
#      break
#   k=k+2

#27 How does continue sentence act, differently than break?
# they are simiilar, but continue does not exit the whole while loop, instead it only exits the current loop and something new is commanded.

#28 Write a program only printing divadible numbers
# k=0
#while k<6:
#   k=k+1 or k+=1
#   if k % 2 != 0       #if k is divadable by two, but not equal to 0
#       continue
#   print (f"{k:2}", end=")

#29 Why should we avoid using break and continue sentences?
# they can make the code difficult to understand

#30 Then When can it be natural to use a break sentence?
# when the user himself WANTS to terminate the loop, inside while loop use:
# n= int(input("n?"))

#31 Program that calculates sum of n as an input: 1+2+3+.....+n
#while True:
    #n=int(input("n?"))
    #if n <=0:
        #break
    #sum = 0
    #k=1
    #while k<=n:
        #sum=sum+k   #add sum with k
        #k=k+1       #add k with 1
    #print ("the sum is", sum)

# 32 Give an example when we give an assignment in the beginning of a while loop. Example: Keep asking for input until user types 'exit'
while (user_input := input("Type something (or 'exit' to quit): ")) != "exit":      #:= walrus operator, used when combine assignment and condition
    print(f"You typed: {user_input}")           #if user_input is not equal to "exit" print....

#33 When is a for-loop used? give an example
#Use when you know in advance:
#how many times you want to loop, or
#you want to go through a sequence (like a list, string, range, etc.)
print ("[", end="")
for k in range (0,6,2):
    print(f"{k}", end="")
print("]")

#34 How can you make the range count all numbers from 10-1 ,but backwards?
#Answer
for k in range (10,0,-1): #adding -1 makes the program count backwards in range, OBS! you must add the following number "0" to get the number 1 included in range
    print(end="[")
    print(f"{k:1}", end="]")


######CLASS NOTES#####

x = int(input ("hur många äpplen har du?:"))
children =5
apples = x
whole_apples = apples// children
leftover_apples = apples% children

print ("Varje barn får", whole_apples, "hela äpplen")
if leftover_apples !=0:             # om leftover_apples inte är noll, alltså om det blir rester, så delas den mellan antal barn.
    print ("och dessutom", leftover_apples, "/", children, "av ett äpple")

#35 Explain the parts in an "for-in" statement
# for i in range (firstnum, lastnum, steps):    # i is a loop variable that take on different values as the loops run,and is defined on first loop, after loop 1 i becomes firstnum+ steps
#       followed by one or multiple indentated statements
#leaving steps means 1
#entering only one num means lastnum

#36 How can you define range (n) in other words?
# for i in range (n) , is the same as for i in range (0,n,1)

#37 Write a program that reads two decimal numbers from the user and checks which one is larger, use if, elif, and else
#Answer:
num1, num2 = (input("Enter two decimal numbers:" )). split ("and")
# convert string to float
num1 = float (num1)
num2 = float (num2)

if num1 > num2:
    print (f"{num1} is greater than{num2}")
elif num1 < num2:
    print (f"{num1} is smaller than {num2}")
else:
    print ("The decimals are equal")

#write same program but without split.() function
value_1 = float(input ("Enter value 1:"))
value_2 = float(input ("Enter value 2:"))

if value_1 > value_2:
    print (f"{value_1} is greater than{value_2}")
elif value_1 < value_2:
    print (f"{value_1} is smaller than {value_2}")
else:
    print ("The decimals are equal")


# Write a program that lets the user enter dog years and calculates the corresponding human years. 7 human years equals to one dog year. Every dog year after the second counts as 5 human years each.

dog_years  = int(input("Enter number of dogyears?:"))

if dog_years == 1:
    human_years = 15
elif dog_years == 2:
    human_years = 15 + 9
elif dog_years > 2:
    human_years = 15 + 9 + (dog_years-2)*5
else:
    human_years = 0     #for neg values or 0

print (f"human years:{human_years}")

# Write a program that lets the user write a number and prints three lines with the following line after the prevoius ontaining one more "+" sign .
n = int(input("Enter desired number of lines:"))

for i in range (1,n+1):
    for j in range (1,i+1):
        print ("+", end="")
    print()       #terminates line

#This program consists of two for-loops
#The outer loop runs n times , every loop represents one line printed
#in the beginning i has value 1, means variable j is going to run between 1 and 1, the inner for loop has been runned only once the first time.
#second time i has value 2, whih means j will run between 1 and 2, the inner for loop runns two times, the "+" sign will be printed two times on this line, and THE SAME LINE is what end="" means
#etc








