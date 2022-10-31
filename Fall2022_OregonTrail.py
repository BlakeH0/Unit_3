# Blake Harrington
# 21 October, 2022
# Oregon Trail


import random




# Travel/Rest Variables
travel_distance = [30, 60]


# Food/Health
current_food = 500
current_health = 5
sickness = False

# Location Variables

IM = 0
distance_left = 2000
control_distance = distance_left

OC = 2000
end = OC

# Date
current_month = ["March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
month = 0
current_day = 1
months_30_days = [4, 6, 9, 11]
months_31_days = [3, 5, 7, 8, 10, 12]




# Add_Day Function 
def add_day(days):
    global current_month
    global current_day 
    global month
    current_day += days

    if current_month in months_30_days:
        if current_day > 30:
            month += 1
            current_day -= 30
            return f"It is now {current_month[month]} {current_day}! "
        else:
            return f"It is now {current_month[month]} {current_day}! "
    else:
        if current_day > 31:
            month += 1
            current_day -= 31
            return f"It is now {current_month[month]} {current_day}! "
        else:
            return f"It is now {current_month[month]} {current_day}! "

# Dysentary Function
def dysentary_func():
    global current_health
    global sickness
    days_traveled = random.randint(3, 7)
    days_rested_hunted = random.randint(2,5)
    if sickness == True:
        if days_traveled >= 5 or days_rested_hunted == 5:
            current_health -= 1
            return "Your dysentary has decreased your health by 1!"

# Health Lost Function
def health_lost():
    global current_health
    days_traveled = random.randint(3, 7)
    days_rested_hunted = (2, 5)
    if days_traveled >= 7:
        current_health -= 1
        return "You lost one health due to traveling."
    elif days_rested_hunted == 5:
        current_health -= 1
        return "You lost one health from hunting so much!"
    
# Lose Food Function
def food_lost(days):
    global current_food
    current_food -= (days * 5)
    return f"and ate {days * 5}lbs of food"



# Travel Function
def travel():
    global sickness
    global distance_left
    days_traveled = random.randint(3, 7)
    dysentary = random.randint(1, 95)
    if distance_left > 0 and dysentary != 6 and sickness == False:
        distance_left -= random.randint(30, 60)
        print(add_day(days_traveled))
        print(f"You traveled {control_distance - distance_left} miles, {food_lost(days_traveled)}!")
        return health_lost()
    elif distance_left > 0 and sickness == True:
        distance_left -= random.randint(30, 60)
        print(add_day(days_traveled))
        print(f"You traveled {control_distance - distance_left} miles, {food_lost(days_traveled)}!")
        return dysentary_func() and health_lost()
    elif sickness == False and dysentary == 6:
        sickness = True
        distance_left -= random.randint(30, 60)
        print(add_day(days_traveled))
        return "On your journey you contracted dysentary from the rivers you drank from! you will lose one health every 5 days you have not recovered. " and health_lost()
    

# Rest Function
def rest():
    global current_health
    day_rested = random.randint(2, 5)
    if current_health < 5:
        current_health += 1
        print(add_day(day_rested))
        print(dysentary_func())
        return f"You rested for {day_rested} days, gained 1 health, {food_lost(day_rested * 2//5)}. "
    else:
        print(add_day(day_rested))
        print(dysentary_func())
        return f"You rested for {day_rested} days, {food_lost(day_rested * 2//5)}, but were already at full health! "

# Hunt Function
def hunt():
    global current_food
    days_hunted = random.randint(2, 5)
    current_food += 100
    print(add_day(days_hunted))
    print(f"You hunted for {days_hunted} days, {food_lost(days_hunted * 15//5)}, but got 100lbs of food!")
    print(dysentary_func())
    return health_lost()


# Status Function
def status():
    global current_food
    global current_health
    global current_month
    global current_day
    global distance_left
    return (f"Food: {current_food} \n"
    f"Health: {current_health} \n"
    f"You are {distance_left} miles from Oregon City!\n"
    f"Date: {current_month[month]} {current_day}")

# Help Function
def help():
    return ("Travel: Travels character between 30-60 miles, and takes 3-7 days.\n"
    "Rest: Increases health by 1 (up to 5 total), and takes 2-5 days.\n"
    "Hunt: Adds 100lbs of food to your inventory, and takes 2-5 days.\n"
    "Status: Lists current food, health, distance traveled, and day.\n"
    "Help: Lists all comands and displays their individual functions.\n"
    "Quit: Will end the game upon the confirmation from the player. ")

# Quit Function
def quit():
    quit_conf = input("Are you sure you would like to quit the game? Progress will not be saved. (y/n) ")
    global running
    if quit_conf == "y":
        running = False
        return "Okay! Goodbye..."
    elif quit_conf == "n":
        return "That's what I like, perseverance!"
    else:
        return "Please answer with 'y' or 'n'! "
        
# Introduction
print("         Welcome to the Oregon Trail! Your goal is to travel from Independence, Missouri \n"
"         to Oregon City, Oregon! It is a 2,000 mile trip, with obstacles throughout it. \n"
"         You'll begin with 500lbs of food & 5 health, but both decrease as you journey. \n" 
"         You will have 9 months to complete your journey without dying, starting March \n"
"         1st and ending before December 31st. Be prepared for everything! You will have \n"
"         to conquer the expected and unexpected to survive... But do you have the skills \n"
"         necessary to complete this grueling task? ")
input()

# Name
user_name = input("What is your name? ")

running = True
while running:
    control_distance = distance_left



    # Player Decision
    print()
    choice = input(f"What would you like to do {user_name}? Travel, rest, hunt, status, help, or quit?  ")
    print()
    if current_month[month] != "December" and current_day != 31:
        if distance_left > 0:
            if current_health > 0:
                if choice == "travel":
                    print(travel())
                elif choice == "rest":
                    print(rest())
                elif choice == "hunt":
                    print(hunt())
                elif choice == "status":
                    print(status())
                elif choice == "help":
                    print(help())
                elif choice == "quit":
                    print(quit())
                else:
                    print("Please enter a valid command! Make sure ALL words are lowercase/spelled correctly! ")
            else:
                print("Sadly, you have perished and could not finsih your journey to Oregon. RIP")
        else:
            print(f"Good job {user_name}, you made it to Oregon in time! You have succesfully conquered The Oregon Trail!")
    else:
        print("Sadly you ran out of days. You ended up freezing to death as the cold front came through, about 10 miles from Oregon City.")