# In the state of Arizona (USA), the drinking age is 21 years old.
# Write a Python code that checks the drinking age of a person.

# def canDrink(age):
#   if (age < 0):
#     #a new ValueError will be raised to who called canDrink
#     my_error = ValueError("{0} is not a valid age ". format(age))
#     raise my_error
#   result = True if (age >= 21) else False
#   return result

print("Are you authorized to drink in AZ?")

success = False

while not success:
    try:
        age = input("Type your age: ")
        age = int(age)   # In this case, if the user input a non-integer data (a character for example),
                         # this line will result in an error
    except ValueError:  # Catpure the cast error
        print("The value typed is not an integer.")
    else:
        # if canDrink(age):
        if age > 21:
            print("You can drink.")
        else:
            print("You cannot drink.")
        success = True
