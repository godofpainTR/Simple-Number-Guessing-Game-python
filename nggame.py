from random import randint as ran
import os
import time
print("Welcome to the number guessing game!")
time.sleep(1)
print("You'll now be prompted to enter an amount of lives and an upper limit of numbers you will play with.")
print("Your options will determine your score multiplier.")
time.sleep(4)
for i in range(0,10):
    print("")
defaultmultiplier = round(1000/6,3)
lives = int(input("How many lives do you need(default: 6)?"))
print("")
setlives = lives
while True:
    numlimit = int(input("Write your desired upper limit(default: 1000):"))
    print("")
    if numlimit <= lives:
        print("You can't set the upper limit less than the amount of lives. You sneaky cheater!")
        continue
    else:
        break
usermultiplier = round(round(numlimit/lives,3)/defaultmultiplier,3)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
print("Ok then, let's play! Your score multiplier is: ",usermultiplier,"X")
trueanswer = ran(0, numlimit)
while True:
    attempts = setlives - lives


    if lives == 0:
        print("I'm sorry, but you've no attempts left. The correct number was ",trueanswer," . Game over, thanks for playing!")
        time.sleep(4)
        break
    print(" ")
    print("Remaining lives:",lives,"Number limit:",numlimit)
    useranswer = int(input("Guess a number :"))
    if useranswer > numlimit:
        print("Mate, that's higher than the limit you've just set. Are you drunk or something?")
        continue
    if useranswer == trueanswer:
        print("Congratulations, you won at",attempts,"attempts!")
        print("Your multiplier was: ",usermultiplier,"X")
        #TODO: put a more sensible scoring formula here
        userscore = (1/attempts)*1000*usermultiplier
        print("Therefore, your score is:",userscore)
        time.sleep(4)
        break
    elif abs(useranswer - trueanswer) > 1000:
        print("You are pretty far off, try again.   Press ENTER")
        lives = lives - 1
        input()
        clear()
        continue
    elif 1000 > abs(useranswer - trueanswer) > 100:
        print("You are closer than 1000. I guess that's something.   Press ENTER")
        lives = lives - 1
        input()
        clear()
        continue
    elif 50 < abs(useranswer - trueanswer) < 100:
        print("Your number is less than 100 away from the answer!   Press ENTER")
        lives = lives - 1
        input()
        clear()
        continue
    elif 10 < abs(useranswer- trueanswer) <50:
        print("Getting closer, less than 50 away from the answer!")
        print("Therefore the number might be between:",useranswer-49,"-",useranswer+49)
        print("Press ENTER")
        lives = lives - 1
        input()
        clear()
        continue
    elif 5 < abs(useranswer - trueanswer) < 10:
        print("You are very close! The correct answer is less than 10 away!")
        print("Therefore the number might be between:", useranswer - 9, "-", useranswer + 9)
        print("Press ENTER")
        lives = lives - 1
        input()
        clear()
        continue
    elif 3 < abs(useranswer - trueanswer) < 5:
        print("Almost there now! Only 5 away!")
        print("Therefore the number might be between:", useranswer - 4, "-", useranswer + 4)
        print("Press ENTER")
        lives = lives -1
        input()
        clear()
    elif abs(useranswer - trueanswer) < 3:
        print("Only 3 away!")
        print("Therefore the number might be between:", useranswer - 2, "-", useranswer + 2)
        print("Press ENTER")
        lives = lives -1
        input()
        clear()

