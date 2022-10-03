'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.
random.choice
3.  Create a program that simulates a magic 8-ball
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good

#Dice Roll
import random
roll = input("Would you like to rolls the dice y/n? ")#Ask User
if roll == 'y':
    print(f"You rolled a {random.randint(1, 6)}")#RNG
elif roll == 'n':
    print("Too bad!")
    print(random.randint(1, 6))#RNG
else:
    print("I'm not even sure what that means.")
'''
#Magic 8-Ball
playing = True
while playing == True:
    import random
    response = ['Yes', 'No', 'Most Likely No', 'Most Likely Yes', 'Maybe', 'Outlook Is Not Good', 'Ask Again Later']#Response List
    q = input("Ask the Magic 8-Ball a question: ")#User's Question
    print(random.choice(response))#Print Random Response
    play = input("Would you like to ask another question, Y/N? ")
    if play == 'Y':
        print("")
    elif play == 'N':
        print("Okay, bye-bye!")
        playing = False
        break
    else:
        print("No, I'm gonna choose for you since you cant follow directions.")
        playing = False
        break
