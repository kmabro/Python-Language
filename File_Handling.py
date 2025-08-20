# 1.
'''
Create a file named `data.txt` and write the text "This is the first line." into it.
'''
# f = open("data.txt", "w")
# f.write("This is the first line.")
# f.close()
## OR ##
# with open("data.txt", "w") as f:
#   f.write("This is the first line.")

# 2.
'''
Append the text "This is an appended line." to `data.txt`.
'''
# f = open("data.txt", "a")
# f.write(" This is an appended line.")
# f.close()
## OR ##
# with open("data.txt","a") as f:
#   f.write(" This is an appended line.")

# 3.
'''
Read and print the contents of `data.txt` line by line using a loop.
'''
# f = open("data.txt", "r")
# for line in f:
#   print(line)
# f.close()
## OR ##
# with open("data.txt", "r") as f:
#   for line in f:
#     print(line)

# 4.
'''
Overwrite `data.txt` with the sentence "Python is awesome!".
Then read and print the updated content.
'''
# f = open("data.txt", "w")
# f.write("Python is awesome!")
# f.close()
## OR ##
# with open("data.txt", "w") as f:
#   f.write("Python is awesome!")

# 5.
'''
Check if the file `data.txt` exists. If it does, print "File exists", else print "File not found".
(Hint: Use os module)
'''
# f = open("data.txt", "r")
# if f:
#   print("File exists")
# else:
#   print("File not found")
## OR ##
# import os 
# if os.path.exists("data.txt"):
#   print("File exists")
# else:
#   print("File not found")

# 6.
'''
Use the `with` statement to read the first 10 characters of `data.txt` and print them.
'''
# with open("data.txt", "r") as f:
#   print(f.read(10))

# 7.
'''
Count and print how many lines are in `data.txt`.
'''
# f = open("data.txt", "r")
# lines = f.readlines()
# print(len(lines))
# f.close()

# 8.
'''
Write a list of 3 strings into `data.txt`, each on a new line. Use a loop to do this.
'''
# f = open("data.txt", "w")
# for i in range(3):
#   f.write(f"This is line {i+1} \n")

# 9.
'''
Read `data.txt` and store all lines in a list.
Then print the list.
'''
# with open("data.txt", "r") as f:
#     lines = f.readlines()
# print(lines)

# 10.
'''
Read `data.txt` and print only those lines which contain the word "Python".
'''
# with open("data.txt", "r") as f:
#   for line in f:
#     if "Python" in line:
#       print(line)


'''1. Write a Python program to read and print all lines from the file `data.txt` using a while loop and readline().'''
# f = open("data.txt", "r")
# while True:
#   line = f.readline()
#   if not line:
#     break
#   print(line)

'''2. Read all lines from `data.txt` using the readlines() method and print the total number of lines.'''
# f = open("data.txt", "r")
# lines = f.readlines()
# print(len(lines))

'''3. Write a list of 3 lines: ["Line A", "Line B", "Line C"] to `data.txt` using writelines(). Make sure to add newlines manually in the list.'''
# f = open("data.txt", "w")
# lines = ["Line A", "Line B", "Line C"]
# for line in lines:
#   f.writelines(line + "\n")

'''4. Write a Python program to read `data.txt` using readlines() and print only those lines which contain the word "error".'''
# with open("data.txt", "r") as f:
#   for line in f:
#       if "error" in line:
#           print(line.strip())

'''1. Open the file `data.txt` and print the current file pointer position using tell().'''
# f = open("data.txt", "r")
# print(f.tell())
# f.close()

'''2. Read the first 20 bytes from `data.txt`, then print the file pointer position using tell().'''
# with open("data.txt", "r") as f:
#   data = f.read(20)
#   print(f"Data read: {data}")
#   print(f"File pointer position: {f.tell()}")

