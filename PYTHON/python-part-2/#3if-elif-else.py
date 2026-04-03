
#with if statements you can either write a condition or use a boolean

#IF-STATEMENTS
#1
storlek = input("Välj en storlek (S/M/L): ")
färg = input("Välj en färg(röd/vit/blå): ")

if storlek != "L" :
    print (f"Storlek {storlek} finns att beställa!")
else:
    print(f"Storlek {storlek} är slut tyvärr!")

if färg != "blå":
    print (f"{färg} finns att beställa!")
else:
    print (f"{färg} är slut tyvärr!")


#2 Write a program that calculates price for calling. Program will intake how many minutes someone calls per month and how much it costs per minute . You´ll get 10% discount if you call for at least 30 Euros

minutes = int(input("Price: 0.30€/min\nPlease insert how many minutes you´ve called this month: "))
cost = minutes *0.30
discount = cost * 0.10
total_cost = cost - discount

if cost >= 30:
    print (f"You´ve recieved a 10% discount of {discount}")

print (f"Total price: {cost}")


#3 In a gym you can either buy a year-card or a one-time-ticket. Write a program that reads the price for a year-card, prie for a one-time-tic and the amount of times one intend to train under one year. The program will tell you if it is worth buying a year-card or not

print()
times = int(input("PRICE CHART\none-time-pass: 10€\nyear-card: 300€\nHow many times do you intend to workout this year?: "))
one_time = 10
year_card = 300

total_cost = times*one_time

if total_cost == 300:
    print("Buying one-time-passes and year-cards are the same, choose based on convinience")
if (total_cost > 300):
    print("It it worth buying a year-card for 300€!")
elif total_cost < 300:
    print(f"It is worth buying one-time passes for{total_cost} €")
else:
    print ("invalid input. Please enter a positive whole number!")

#4 Leap years are years that are evenly divisable by 4, with the exception of those that are evenly divisable by 100. However those years that are evenly divisable by 400 are leap years. Write a program that lets user input a year and prints if it is a leap year or not:

year = int(input("Please enter a year: "))


if year % 400 == 0:                  # must check 400 first
    print (f"The year {year} is a leapyear!")

elif year % 100 == 0:                # exception comes after
    print (f"The year {year} is NOT a leap year!")

elif year % 4 == 0:
    print (f"The year {year} is a leapyear!")

else:
    print(f"The year {year} is NOT a leapyear!")

#5 Write a program that reads two decimal numbers from the user and checks which of them is greater.
numbers = input("Please enter two decimal numbers: ")

num1, num2 = numbers.split(",")

num1 = float(num1)          #need to convert later when using split function
num2 = float(num2)

if num1>num2:
    print(f"{num1} is greater than {num2}!")
elif num2>num1:
    print (f"{num2} is greater than {num1}!")
elif num1==num2:
    print ("The numbers are equal!")

#6 The traditional assumption that seven human years correspond to one dog year is a simplification of reality. A more realistic estimate for a medium-sized dog is:
#first dog year = 15 human years
#second dog year = 9 human years
#each subsequent dog year = 5 human years
#Write a program that lets the user enter dog years and calculates the corresponding human years.
print()
dog_years = int(input("Enter dog-years to convert: "))
first_dogyear = 15
second_dogyear = 9

print()
dog_years = int(input("Enter dog-years to convert: "))
first_dogyear = 15
second_dogyear = 9

if dog_years == 1:
    print (f" {dog_years} dog year is equal to {first_dogyear} human years!")

elif dog_years ==2:
    print (f"{dog_years} dog years is equal to {second_dogyear} human years!")

elif dog_years > 2:
    print (f"{dog_years} dog years is equal to {first_dogyear+second_dogyear+((dog_years-2)*5)}")

else:
    print("Please enter a valid positive number! ")         #update to a whileloop for user to "try again"!


#7 # A mobile operator offers three different subscriptions: Basic, Normal, and Plus. When comparing the conditions for the subscriptions, it turns out that the subscription Kontant is cheapest if you call at most 33 minutes per month, Normal is most profitable if you call between 33 and 66 minutes per month, and Plus is most advantageous if you call even more. Write a program that reads the number of minutes you estimate you will call per month. The program should state which subscription you should choose.
print()
minutes = int(input("Approx. how many minutes do you intend to use per month?: "))

if minutes <=33:
    print("Buy a Basic package!")
elif 33<= minutes <=66:
    print("Buy a Normal package!")
elif minutes >66:
    print("Buy a Plus package!")
else:
    print ("Please enter a valid number for minutes!")


#8 (and/or/not) Write a program that asks the user two yes/no questions:
#Is the traffic light green? (yes / no)
#Is there a pedestrian crossing? (yes / no)

#Your program should decide whether the car can GO or must STOP based on these rules:
#If the light is green and there is no pedestrian, print "You can go!"
#If the light is green but there is a pedestrian, print "Wait for pedestrian!"
#If the light is not green or there is a pedestrian, print "Stop!"
print()
trafic_light = input("Is the traffic light green? (yes / no): ").lower()
pedestrian = input ("Is there a pedestrian crossing? (yes / no): ").lower()

if trafic_light == "yes" and pedestrian =="no":
    print ("You can go!")
elif trafic_light == "yes" and pedestrian == "yes":
    print("Wait for pedestrian!")
elif trafic_light == "no":
    print ("STOP!")
else:
    print("Invalid input. Please type 'yes' or 'no'.")


# 9. (Using Boolean) Logged in check:
# Ask the user: “Are you logged in? (yes/no)”
# Store the answer in a boolean variable (True or False).
# If logged in → message "Welcome back!"
# If not → message "Please log in first!"

logged = input("Are you logged in? (yes/no): ").lower()

is_logged_in = (logged == "yes")

if is_logged_in == True:          #this True-step is unneccesary bcs is_logged_in is already True or False
    print ("welcome back!")

else:
    print ("Please log in.")

#10 (Using Pass-command) Password Strength Checker
# Write a program that asks the user for a password.
# Your program should:
# If the password length is less than 6 → just use pass "Password is weak"
# If the password length is between 6 and 10 → print (don’t print anything )..
# If the password length is more than 10 → print "Password is strong".
# Then add a line that prints: "Good password, Please remeber your password or write it down!"

password = input("Please, enter a password (at least 10 characters): ")

if (len(password)) < 6:
    print ("Password is weak")

elif 6 <= (len(password)) >= 10:
    pass

elif (len(password)) > 10:
    print("Password is strong")
    print ("Good password, Please remember your password or write it down!")




