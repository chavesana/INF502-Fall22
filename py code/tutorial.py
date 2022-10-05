# Create a program that stores a set of numbers in a list
# The list will be filled with random numbers. The user needs to be able to:
# 1. Add a number to the list
# 2. Present the number of elements in the list, and list the numbers (one per line)
# 3. Clear the list
# 4. Exit the application

import random

def add(myList):
    n = random.randrange(1, 100)
    print("Adding the number", n, "to the list.....")
    myList.append(n)


def show(myList):
    print("The current list has", len(myList), "elements:")
    for n in myList:
        print(n)


def clear(myList):
    print("Cleaning the list.....")
    myList.clear()
    print("The list is now empty")


def printMenu():
    print("What do you want to do? Here are the options:")
    print("1. add a number to the list")
    print("2. show the number of elements and the list of numbers")
    print("3. clear the list")
    print("4. exit the application")


def main():
    myList = list()
    printMenu()
    op = int(input("Choose your option: "))
    while op != 4:
        if op == 1:
            add(myList)
        elif op == 2:
            show(myList)
        elif op == 3:
            clear(myList)
        else:
            print("Invalid option, please choose an option between 1 and 4")
        op = int(input("Choose your option: "))
    else:
        print("Thanks for playing. The app is now closed")


main()
