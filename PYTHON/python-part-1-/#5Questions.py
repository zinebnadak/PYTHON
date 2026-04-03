#TO HANDLE TEXT
#1 What is literals?
# A literal is a fixed value that you write directly in your code. It represents itself (not a variable or expression). ex. numerical literals , string literals, boolean literals. Ex.  42 is a integer literal. or "Eva", Eva is a string literal. COMPARE TO y= x, Here y is not a literal, it’s a variable that refers to the value stored in x.

#2 What does "\" inside a string tell the program?
# That the next character is treated differently ex. x = "His name was \"Mikael\"". character combinations with "\" is called escape-sequenses.

#3 What is a "raw string", and how are they linked to backslashes - "\"
#Normally, in Python, backslashes (\) are used for escape sequences inside strings. A raw string tells Python “don’t treat backslashes as special — just keep them as they are.”
# path = r"C:\new_folder\test.txt"          here \n and \t escapes are ignored
# print(path)                               C:\new_folder\test.txt

#what is Unicode?
# Unicode is a system for representing characters (text) as numbers. It’s like a giant dictionary where every character in every language (letters, numbers, emojis, symbols) has its own unique number called a code point. So computers don’t actually store "😊" — they store 128522 ,  and Unicode tells them how to show it. There is unicode for digits, "0" → U+0030, So "0" as a string is different from the number 0 as an integer. Unicode is used instead of ASCII as a international standard.

#why is Unicode  used instead of ASCII
# ASCII Uses 7 bits → only 128 characters. Unicode Can represent over 1.1 million characters with UTF-8 (one byte), UTF-16 (two bytes) and UTF-32 (four bytes) groups.

#How can you print a character that is not on your keyboard using Unicode?
# use \u inside the string followed by the unicode, then print it
# print("\u03A9")   # Greek capital letter Omega (Ω)

#How can you print a character that is not on your keyboard using the charachters name instead of the unicode?
# use \N            OBS! knowing the official Unicode names is key if you want to use the \N{...} syntax in Python
# print("\N{GREEK CAPITAL LETTER OMEGA}")    # Ω
# to know name import Pythons´s "unicodedata" module
#import unicodedata
#char = "Ω"
#print(unicodedata.name(char))

#8 What are sequences in Python?
# In Python, sequences are ordered collections of items/elements that support indexing, slicing, and iteration.
# Common sequence types include lists, tuples, strings, and ranges.
# They allow you to access elements by position and perform operations like concatenation, repetition, and membership tests.

#9 How does indexing work?
# The items/elements in a sequence are numbered starting from 0 (or backwards from -1), and their number is called index.
#x = "Hello!"    /the letter "H" has index 1, "e" index 2 etc

#10 How can you read the corresponding item/element, by knowing the indexing number. Eg. indexing?
# write the variable then the indexnumber you want to know inside "[]"
# §print(x[0])          /will give you H

#11 How to know how many items/elements are in a sequence? (by using only the variable)
# use function "len" , from length
# print (len (x))   /will give you 6


#12 Unlike other languages ,In python you can use negative indexes to begin counting from backwards.

#13 In indexing you can choose only one item from sequene, How can you selcet multiple?
# By creating a "slice" that becomes the new sequence - ex. sequence [first:last:steps]
# leaving first gives you index 0
# leaving last gives you the sequances lenght /         /you can leave one or two integers empty, but ":" should always be included
# Leaving steps gets you automatically 1
# you can actually go beyond the limits of indexes when slicing , s[1:100] can give you whole sequence

#what is a substring?
#A substring is simply any sequence of characters within a larger string.

# How to find the index (position) of a specific character or number in a sequence without counting manuall?
# my_sentence = "zineb är en kodare!"
print(my_sentence.index("z"))

#Want to find all occurrences of "e"? Use enumerate()
#my_sentence = "zineb är en kodare!"

positions = [i for i, c in enumerate(my_sentence) if c == "e" ]
print(positions)

#Now use "count" to find number of occuring "e":s
#my_sentence = "zineb är en kodare!"

count_my_list =my_sentence.count("e")
print(count_my_list)

#14 How and why can we compare sequences?
# to see if they are equal (same lenght and items gives you True)
# "abc" = "abc"         //give True

#15 How can you compare if a sequence is smaller or bigger than another?
# by using lexicographic order/dictionary order
# "abc" < "abcd"    // give True

#16 what is it that gets compare when comparing texts
# When comparing texts (strings) in Python, what gets compared is the Unicode code point (numeric value) of each character, in lexicographic order.
# "å" < "ä"         /gives false, bcs it goes by the numerical code , only letters a-z are in "right order" even numerical.

#17
# When do we use a for-loop?
# When we want to go through all items/elements in a sequence
# For x in range (0,len(s)):      //or//         For x in s:

------------_>#18 what does function "enumerate" do, and how to use it?
# a built-in function that lets you loop over something while keeping track of the index of the current item.
# enumerate(sequence variable, start=0)
#fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
    #print(index, fruit)

#19 How to use operator "in" to find out if an element or text is in a sequence or word?
#string = "happy"
#print ("h" in string)           /gives true
#print ("app" in string)        /gives true

#20 Can you change the text in a sequence by indexing?
# NO! you need to change whole word
# s = "old"
# s[1]= "u"         SyntaxError!
# s = "young"      OK!

#21 How an you create a new sequene by two already existing sequences?
# by using "+" operator
# s1 = "re"
# s2 = "turn"
# s3 = s1 +s2       or   s1+= "play"           /s3 becomes "return", s1 gets new value "replay"

#22 What other operator can be used to create sequences?
# "*" operator
# n = no
# a = n *3          / gives us a = "nonono"

#23 Giive some examples of functions that are common for all types of sequences
# language = "python"

# len (language)   /counts number of characters
# min (language)   /gives smallest item in sequenece  -language
# max (language)    /gives greatest item in sequenece  -language

#sorted (language)  /gives a sorted list , sequence -language does not change
#sum (number)       /gives sum of items in sequence , not for strings

#language.count (p)     /counts how many times "p" is in sequence
#language.count (p, starting index (s), lenght of interval (l))    /counts how many times "p" is in interval l-(s-1) in sequence
#language.index (p)     /gives index for first time "p" in sequence
#language. index (p,p,n)    /gives index for first time "p" in inteval l-(s-1) in sequence

#24 Where can you read more about funtions for strings
# In pythons standard library see page. 98

#25 There are two types of functions that go with strings
# Those that EXAMINES strings
# Those that FORM NEW strings
# !no functions can change in text!

#DATE AND TIME
#26 How to use standard-type "datetime"
# to know current date and time
# import datetime
# then create a variable
# x = datetime.datetime.now()       /datetime written two times
# date = x.date()
# time = x.time()
# datetext = str(date)          print (datetext)      /if want to print date in "yyyy-mm-dd" format
# timetext = str(time)[:8]                            /if want to print time in "hh-mm-ss" format
# year = x.year             / works with .month and .day too
# hour = x.hour             / works with .minutes and .seconds too
# print (date.isoweekday()) /to get the weekday number (1-7)
# print (date.isocalendar()[1]) /to get weeknumber

#27 What is Match-statement, when and how to use?
# Use when you have multiple alternatives and user is going to shoose one of them. It’s useful as a cleaner alternative to long chains of if/elif/else. Patterns can match constants, variable structures, sequences, or even data classes.
# size = input ("what size (XS,S,M,L)?: ").upper
# match size:
    #case "XS":
        #print ("Availiable on shelf 1")
    #case "S":
        #print ("Availiable on shelf 2")
    #case "M" | "L":         # need to use pipe symbol "|" (means or) , Option + 7 on MacBook
        #print ("sold out"
        #print ("can get ordered")
    #case _:                  #if input does not math any of cases comp auto jumps to this "case_"
        #print ("wrong search input")

#28 What is | and _ used in match..case (or switch..case as called in other languages)
# Uses | to match multiple options (| = pipe, Option + 7 on the keyboard)
# Uses _ for a 'default' case (_ = underscore), corresponds to else in an if..elsif..else statement
#ex. 

score = int(input("Enter the grade: "))

match score:
    case 5:
        print("Perfect score!")
    case 4 | 3:
        print("Nicely done!")
    case 2 | 1:
        print("A good effort!")
    case 0:
        print("Some work still needed!")
    case _:
        print("Illegal input!")







