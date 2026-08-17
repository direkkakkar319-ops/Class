# READING FROM FILE:-
f = open("data.txt", "r")
print(f.read())# read()-->reads entire file at once
print(f.readline())# readline()-->read one line at a time
print(f.readlines())# readlines()-->read all lines into a list
f.close()

# WRITING IN A FILE
f = open("data.txt", "w")
f.write("Hello Python")# write()-->writing text in a in file by deleting the previuos content
f.close()

# APPEDING A FILE
f = open("data.txt", "a")# "a"--> new content will be added without deleting old content 
f.write("\nNew Line")
f.close()

# USING with STATEMENT
# The with statement is used for automatic resource management.
# When working with files, it opens the file and automatically closes it after the block ends.
with open("data.txt", "r") as f:
    print(f.read())
with open("data.txt" , "a") as f:
    f.write("fuck you")

# FILE POINTER (tell() AND seek())
# tell()-->returns current position
f = open("data.txt")
print(f.tell())
# seek()-->moves cursor to specific position
f.seek(0)
# file.seek(offset, reference)
# offset → number of bytes
# reference
# 0 → beginning of file
# 1 → current position
# 2 → end of file

# HANDLING BINARY FILES
# here we copied text from one binary file to other
# reading the data
with open("image.jpg", "rb") as f:
    data = f.read()
# writing information
with open("copy.jpg", "wb") as f:
    f.write(data)
# another way of copying the file
with open("binary.txt", "rb") as file:
    with open("copy_binary.txt", "wb") as copyFile:
        copyFile.write(file.read())

# CHECKING FILE EXISTENCE
import os
print(os.path.exists("data.txt"))

# FILE HANDLING WITH EXCEPTION HANDLING
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError as e:
    print(e)
finally:
    f.close()

# COPYING CONTENT FROM ONE FILE TO ANOTHER
with open("a.txt", "r") as src:
    with open("b.txt", "w") as dest:
        dest.write(src.read())