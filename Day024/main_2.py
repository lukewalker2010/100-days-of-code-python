# Reading and writing files
# using the with open as file we don't have to worry about closing the file

with open("Day024/my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open ("Day024\my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# Relative and Absolute File Paths
# Absolute start relative to the root
# Relative file paths
# Working directory is folder you are working from 
# ./ for current folder
# ../ to above folder
