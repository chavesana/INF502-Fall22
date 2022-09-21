### READING A FILE

# Example 1: observe the extra linebreak between the lines
file_handler = open('../data/lines.csv', 'r')
for line in file_handler.readlines():
   print(line)
file_handler.close()

# Example 2: removing the linebreaking with rstrip
# file_handler = open('../data/lines.csv', 'r')
# for line in file_handler.readlines():
#    print(line.rstrip('\n'))   # remove the extra linebreaking
# file_handler.close()

# Example 3: list of columns with split()
# file_handler = open('../data/lines.csv', 'r')
# for line in file_handler.readlines():
#    line = line.rstrip('\n')
#    field = line.split(',')  # break the string into a list (split – comma)
#    print(field)
# file_handler.close()

### WRITING A FILE

# Example 1: writing on a single row
# file_handler = open('../data/other.csv', 'w')
# list_1 = ('banana', 'carrot', 'avocado', 'orange', 'grapefruit')
# file_handler.writelines(list_1)
# file_handler.close()

# Example 2: writing one element per row
# file_handler = open('../data/other.csv', 'w')
# list_1 = ('banana', 'carrot', 'avocado', 'orange', 'grapefruit')
# for item in list_1:
#    file_handler.write(item + '\n')
# file_handler.close()

# Example 3: adding to the end with the 'a' mode
# file_handler = open('../data/other.csv', 'a')
# list_2 = ('strawberry', 'lemon', 'guava')
# for item in list_2:
#    file_handler.write(item + '\n')
# file_handler.close()

### REMOVING A FILE
# import os
# os.remove("other.csv") ## WATCH OUT! this removes the file permanently!