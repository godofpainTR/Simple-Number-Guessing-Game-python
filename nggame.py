from random import randint as ran
import os
import time
print("Welcome to the number guessing game!")
while True:
    numlimit = int(input("Write your desired upper limit:"))
    if numlimit <= 6:
        print("You can't set the upper limit less than the amount of lives. You sneaky cheater!")
        continue
    else:
        break
def clear():
    os.system("cls" if os.name == "nt" else "clear")
print("Ok then, let's play!")
lives = 6
trueanswer = ran(0, numlimit)
while True:
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
        print("Congratulations, you won at",6-lives,"attempts!")
        time.sleep(4)
        break
    elif abs(useranswer - trueanswer) > 100:
        print("You are pretty far off, try again.")
        lives = lives - 1
        input()
        clear()
        continue
    elif 50 < abs(useranswer - trueanswer) < 100:
        print("Your number is less than 100 away from the answer!")
        lives = lives - 1
        input()
        clear()
        continue
    elif 10 < abs(useranswer- trueanswer) <50:
        print("Getting closer, less than 50 away from the answer!")
        lives = lives - 1
        input()
        clear()
        continue
    elif abs(useranswer - trueanswer) < 10:
        print("You are very close! The correct answer is less than 10 away!")
        lives = lives - 1
        input()
        clear()
        continue

