import random
rando = random.randint(1, 100)
userguess = None
guesses = 0

while (userguess != rando):
    userguess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if (userguess > rando):
        print('May be something less than this number')
    elif (userguess < rando):
        print('May be something more than this number')

if guesses == 1:
    print("Yayy! You Guessed it right on the 1st guess...")
else:
    print(f'Finally you guessed it right! after {guesses} guesses')

score = guesses

with open("Hiscore.txt")as f:
    hiscore = f.read()

if hiscore == "":
    with open("Hiscore.txt", "w") as f:
        f.write(str(score))
        print("Yayy! You have broken your record!")
elif int(hiscore) > score:
    with open("Hiscore.txt", "w") as f:
        f.write(str(score))
        print("Yayy! You have broken your record!")
