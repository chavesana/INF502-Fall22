# Write a program which repeatedly reads integers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than an integer, print an error message and skip to the next number.

def main():
    myList = list()
    op = input("Type a number or done to exit: " )
    while op != "done":
        if op.isdigit():
            myList.append(int(op))
        else:
            if op != "done":
                print("Invalid option, please try again")
        op = input("Type a number or done to exit: ").lower()
    else:
        print("The total is", sum(myList))  # python function that sums the list
        print("The list has", len(myList), "elements")
        print("The average is", sum(myList)/len(myList))
main()