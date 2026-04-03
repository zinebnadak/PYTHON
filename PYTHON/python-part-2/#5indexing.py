
#1 Write a program  that lets the user input a text and then finds the first whitespace character in the text
text = input("Please write a sentence: ")

i = 0  # used as counter

for x in text:
    if x == " " or x == "\t":
        break   # scan through each character in the string until a whitespace is found
    i = i + 1   # then add it to i
if i < len(text):  # if the counter is less than the length of the text (which means we found a whitespace)
    print(f"First white space on place {i + 1}")  # counts on exactly what place is the white space on?
else:
    print("No white space!")            #it means the whole string was scanned and no whitespace was found, i will end up equal to len(text)

#2 Now write a program that instead finds the last whitesspace character in a text
text = input("Please write a sentence: ")

last_space = 0

for x, char in enumerate(text):         #enumerate gives a tuple (index, character) answer, for each iteration goes through the string character by character, i: the index (position), char: the character
    if char == " " or char == "\t":
        last_space = x                 # update position whenever we find whitespace

print (f"The last white space is at place {last_space+1} ")


#3 write a new version of the program that finds first white space, usa a for-loop with range, and an else part
text = input("Please write a sentence: ")

for i in range(len(text)):          #Loop over the numbers from 0 up to, but not including, the length of the text." So if len(text) is 5, range(len(text)) generates the sequence: 0, 1, 2, 3, 4. These are the valid index positions of the characters in text
    if text[i] == " " or text[i] == "\t":       #text[i] means: look at the character at position i in the string text.
        print(f"First white space is on place {i+1}")
        break
else:
    print ("No white space!")

#4 Write a program that translates dates  from USA style (mm/dd/yy) to swedish style (yyyy/mm/dd)

a = input("Write an american date as mm/dd/yy: ")

#use indexing to fetch characters from a
month = a[:2]      #gives mm (start-1)
day = a[3:5]        #gives dd (3-4)
year = a [6:]       #gives yy (6-end)

s= (f"20{year}-{month}-{day}")
print(f"The american date {a} is {s} in swedish date format!")


#5 Write program that reads in text. Program will delete all white spaces from text and print result. Tip! You can change a parttext with text with lenght "0"
text = input("Enter a sentence: ")

no_spaces = " "         #new empty string created

for i in text:
    if i != " ":
        no_spaces= no_spaces+i  # Add only non-whitespace characters

print("Text without whitespaces:", no_spaces)

#6 Write a program that shows current date and time like this:
#Todays date: yyyy/mm/dd
#Current time: hh:mm:ss
#Replace dashes - in the date with slashes /
#Remove microseconds from the time (i.e., .123456
import datetime

dt = datetime.datetime.now()    #date and time right now

year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
minute = dt.minute
second = dt.second

print (f"Todays date: {year}/{month:02}/{day:02}\nCurrent time: {hour}:{minute}:{second}")


#7 Assume variable "a" is assigned name and personnumber for a person:
# a = "Zineb Nadak 990314-2714"
# you now nónly want to pick out the birthdate "990314" and put it into a new variable "b"
person_num = "990314-2714"      #only strings, lists, and other sequence types can be sliced — not numbers --> use quotemarks

b = person_num[:6]
print (b)


#8 Change last exercise so you get the birthdate in format dd/mm (so 14/03)
person_num = "990314-2714"
b = (person_num[4:6]+"/"+person_num[2:4])
print(b)
#or
person_num = "990314-2714"
print(person_num[4:6]+"/"+person_num[2:4])
#or use f-string instead of "+"

#9 Write a program that reads in a simple message consisting of at least two words.
# The program should then print out both how many words were written and how many characters (letters, digits, and other symbols) the message contains.
# You can assume that there is exactly one blank space between each word and that there are no blank spaces before the first or after the last word.

message = input("Enter at least two words of choice: ")

#char
characters = 0
for c in message:
    if c == " ":        #ignore rest of loop
        continue
    characters = characters + 1
    #but not spaces

#words
w = message.split()     #splits message into words
words = len(w)      #counts how many words

print (f'The words: "{message}" are {words} words, and has {characters} characters.')



# The .replace() method in Python is used to replace parts of a string with something else.
# variable.replace(old, new)

#10 Write a program that reads in a personal identity number and determines whether the person is a man or a woman.
# The next-to-last digit is odd for men and even for women
person_num = input("Enter your person number: ")    #let input take letters as answer
digit = int(person_num[9])  #convert to integer for  calculations

if digit % 2 == 0:
    print ("You are a Woman!")
else:
    print ("You are a Man!")


#11 Write a program that reads in a text and translates it into so-called “robber language.”
# In this language, every consonant is doubled, with an “o” inserted in between.
# Vowels and other characters remain unchanged. #“Hohejoj! Kokomom inon.”

message = input("Write me a message, and I will translate it into robber language: ")

vowels = "aeiouAEIOU"    #check vowels in both cases instead of using .lower(), so output is preserved
result = ""              #create empty string

for i in message:
    if i == " ":
        continue
    elif i not in vowels:
        result = result + (i + "o" + i)
    else:
        result = result + i

print (f'The message "{message}" in robber language is {result}')


#12 Write a program that reads in two time points in the form tt:mm. The program should state how many minutes there are between the two time points. You can assume that the second time point always occurs after the first one, and at the latest within the following 24 hours.
# The program should state how many minutes there are between the two time points.
# You can assume that the second time point always occurs after the first one, and at the latest within the following 24 hours.
from jupyter_core.migrate import migrate_one

time = input('Enter two timepoints tt:mm (separate by "and"): ').split("and")

# Step 2: Clean whitespace around each time
time1 = time[0].strip()
time2 = time[1].strip()

#separate hours from minutes and convert to int to calculate. OBS! You can't convert a whole list to an int directly.
time_one = time1.split(":")
time_two = time2.split(":")

#Extract hours and minutes using indexing, and convert to int
h_one = int(time_one[0])
m_one = int(time_one[1])
h_two = int(time_two[0])
m_two = int(time_two[1])

# Convert both times to total minutes
total_minutes_one = h_one *60 + m_one
total_minutes_two = h_two *60 + m_two

difference = total_minutes_two - total_minutes_one

#covert minutes to hours and minutes
hours = difference//60
minutes = difference%60

print (f"Between {time1} and {time2} is {hours} hour/s and {minutes} minute/s")


#13 A personal identity number, e.g. 561231-1234, consists of ten digits. After the birthdate, the next three digits are a birth number, and the last digit is a control digit. The control digit is calculated as follows: The first nine digits of the personal identity number are multiplied alternately by 2 and 1, starting from the left. The digits in each product are then added together, and finally, all the results are summed up. The control digit is the number that needs to be added to this sum in order to make it evenly divisible by 10.
#Example:
#Personal identity number 561231123 gives the following sum:
#5 \times 2 + 6 \times 1 + 1 \times 2 + 2 \times 1 + 3 \times 2 + 1 \times 1 + 1 \times 2 + 2 \times 1 + 3 \times 2 = 10 + 6 + 2 + 2 + 6 + 1 + 2 + 2 + 6 = 37.
#(Notice that 10 counts as 1 + 0.)
#The control digit should then be 3, because 37 + 3 = 40 is divisible by 10.
#Write a program that reads in a personal identity number and checks if it is correct.



