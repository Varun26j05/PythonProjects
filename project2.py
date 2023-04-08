import random

def game(comp,player):
    if comp == player:
        return None
    elif comp == "r":
        if player == "p":
            return True
        elif player == "s":
            return False
    elif comp == "p":
        if player == "s":
            return True
        elif player == "r":
            return False
    elif comp == "s":
        if player == "r":
            return True
        elif player == "p":
            return False

rando = random.randint(1,3)

if rando == 1:
    comp = "r"
elif rando == 2:
    comp = "p"
elif rando == 3:
    comp = "s"

print("Computer's Turn: ")
import time
time.sleep(2)
print("XXXXX")

you = input("Your Turn: rock(r) | paper(p) | scissors(s) : \n")
a = game(comp,you)

if you == "r":
    end_you = "Rock"
elif you == "p":
    end_you = "Paper"
elif you == "s":
    end_you = "Scissors"

if comp == "r":
    end_comp = "Rock"
elif comp == "p":
    end_comp = "Paper"
elif comp == "s":
    end_comp = "Scissors"

print("You Chose: " + end_you)
print("Computer Chose: " + end_comp)

if a is None:
    print("Tie")
elif a is True:
    print("You Win!")
else: 
    print("You Loose!")


#or 

'''import random


def game(player,computer):
    if player==computer:
        return None
    elif player == "r":
        if computer == "p":
            return False
        else:
            return True
    elif player == "p":
        if computer == "r":
            return True
        else:
            return False
    elif player == "s":
        if computer == "r":
            return False
        else:
            return True

a= random.randint(1,3)
if a == 1:
    comp = "r"
elif a==2:
    comp="p"
else:
    comp="s"

f= input("E:\n")
g=game(f,comp)

if g == None:
    print("Tie")
elif g == True:
    print("Win")
else:
    print("Loose")

print(f'comp={comp}')
print(f'you={f}')'''