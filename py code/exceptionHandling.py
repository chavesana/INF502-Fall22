# Let the exception occur
# import os
# os.remove("other.csv")

# Capturing the exception
import os

filename = "other.csv"
try:    # try to remove the file "other.csv"
    os.remove(filename)
except FileNotFoundError: # if a FileNotFoundError happens when it tries...
    print("There is no file named", filename)  # Log the problem
else:
    print("File", filename, "removed.")
finally:
    print("End of the program.")