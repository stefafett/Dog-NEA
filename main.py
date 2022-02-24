import sys
import random
import linecache
#dog name and stats genaration
def dognames():
    global inta
    global exer
    global friend
    global drool
    f = open("dogs.txt", "r")
    y=random.randint(5,31)
    exer = random.randint(1, 10)
    inta = random.randint(1, 100)
    friend = random.randint(1, 10)
    drool = random.randint(1, 10)
    particular_line = linecache.getline('dogs.txt', y)
    print(particular_line,"exercise",exer, "intelligence", inta, "friendliness", friend, "drool", drool)
    w=input("please hit enter to continue")

#function for intalect

def intelligence():
    global inta2
    inta2 = random.randint(1, 100)
    if inta2 < inta:
            print("player wins!\n")
    else:
        print("computer wins!\n")
    print("the computers dog had an of intelligence of ", inta2)

#function for exercise

def exercise():
    global exer2
    exer2 = random.randint(1, 10)
    if exer2<exer:
        print("player wins!\n")
    else:
        print("computer wins!\n")
    print("the computers dog had an exercise rating of ", exer2)

#function for friendliness

def friendliness():
    global friend2
    friend2 = random.randint(1, 10)
    if friend2<friend:
        print("player wins!\n")
    else:
        print("computer wins!\n")
    print("the computers dog had a friendliness rating of ", friend2)

#function for drool

def drooll():
    global drool2
    drool2 = random.randint(1, 10)
    if drool2 > drool:
        print("player wins!\n")
    else:
        print("computer wins!\n")

    print("the computers dog had an drool rating of", drool2)
def computer():
    if drool2<drool:
        compwins()
    if friend2<friend:
        compwins()
    if exer2<exer:
        compwins()
    if inta2<inta:
        compwins()
def compwins():
    print()


#menu code

while True:
    menu = input("do you want to start?""\n""enter y for yes or n for exit.")
    if menu == "y":
        break
    elif menu == "n":
        print("good bye")
        sys.exit()
    else:
        print("please retry")
while True:
    num= int(input("please enter a number between 4 and 30 for the size of the deck"))
    if num in range(4, 31):
        if num % 2 == 0:
            break
        else:
            print("please select an even number")
    else:
        print("please select another integer")

#the plyers cards and win
won=int()
cards= num
num=num /2
x=0

while x<num:
    cards=cards-2
    x=x+1
    dognames()
    pc=input("which characteristic do you want to choose?\n please enter I for intelligence. \n please enter E for exercise. \n please enter F for friendliness \n please enter D for Drool")
    pc = pc.upper()
    if pc == "I":
        intelligence()
    elif pc == "E":
        exercise()
    elif pc== "F":
        friendliness()
    elif pc == "D\n":
        drooll()
    print("there are", cards, "cards in the deck\n\n")
    if cards==0:
        sys.exit()


    ex= input("do you want to continue?""\n""enter y for yes or n for exit.")
    ex=ex.lower()
    if ex=="n":
        print("good bye")
        sys.exit()
    else:
        pass








