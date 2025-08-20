'''# 1️⃣ Basic: Loop through a list of numbers and print each number.
# After the loop ends, print "All numbers printed successfully."

nums = [2, 4, 6, 8]
# Use for loop + else'''
# nums = [2, 4, 6, 8]
# for num in nums:
#     print(num)
# else:
#     print("All numbers printed successfully.")

'''# 2️⃣ Use a while loop to count from 1 to 5.
# After counting is done, print "Counting completed."

# Use while + else'''
# i = 1
# while(i<=5):
#     print(i)
#     i+=1
# else:
#   print("Counting completed.")  

'''# 3️⃣ Loop through a list of names. If you find your name, print "Found!"
# If the loop completes without finding your name, print "Not found".

names = ["Alice", "Bob", "Charlie", "David"]
target = "Zara"
# Use for loop + if + break + else'''
# names = ["Alice", "Bob", "Charlie", "David"]
# for name in names:
#     if name == "Zara":
#         print("Found!")
#         break
# else:
#     print("Not found")

'''# 4️⃣ Check if a number is prime using a loop.
# If it's prime, print "Prime number".
# Else, print "Not a prime".

num = 17
# Use for-else loop'''
# num = 12
# for i in range(2, num):
#     if num % i == 0:
#         print("Not a prime")
#         break
# else:
#     print("Prime number")

'''# 5️⃣ Loop through a string and check if it contains any digits.
# If a digit is found, break the loop and print "Contains number".
# If no digits are found, print "No numbers in string".

s = "helloWorld42"
# Use for-else loop'''
# s = "helloWorld42"
# for i in s:
#     if i.isdigit():
#         print("Contains number")
#         break
# else:
#     print("No numbers in string") 

'''# 6️⃣ Use a while loop to simulate 3 login attempts.
# If password is correct, print "Access granted" and stop.
# If all attempts fail, print "Account locked".

correct_password = "admin123"
# Use while + break + else'''
# attempts = 0
# max_attempts = 3
# correct_password = "admin123"
# while attempts < max_attempts:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Access granted")
#         break
#     else:
#         print("Incorrect password")
#         attempts += 1
# else:
#     print("Account locked")

'''# 7️⃣ Cybersecurity Twist:
# Simulate scanning ports from 20 to 30.
# Stop scanning if port 22 is found closed. Otherwise, print "Scan complete".

closed_ports = [22]
# Use for loop + break + else'''
# closed_ports = [22]
# for i in range(20, 31):
#     if i in closed_ports:
#         print("Port 22 is closed")
#         break
# else:
#     print("Scan complete")

'''# 8️⃣ Cybersecurity Twist:
# Loop through log messages to detect any 'ERROR'.
# If an error is found, print "Error found". Otherwise, print "System clean".

logs = ["INFO", "WARNING", "INFO", "DEBUG"]
# Use for-else loop'''
# logs = ["INFO", "WARNING", "INFO", "DEBUG"]
# for log in logs:
#     if log == "ERROR":
#         print("Error found")
#         break
# else:
#   print("System clean")

'''# 9️⃣ Cybersecurity Twist:
# Brute-force pin guessing: loop from 1000 to 1005.
# If pin matches, break and print "PIN found".
# Else, print "PIN not found" after trying all.

real_pin = 1003
# Use for loop + break + else'''
# real_pin = 1003
# for i in range(1000, 1006):
#     if i == real_pin:
#         print("PIN found")
#         break
# else:
#     print("PIN not found")  

'''# 🔟 Challenge:
# Loop through multiple login attempts.
# If any username is blacklisted, break.
# Else, allow access if all usernames are clean.

usernames = ["alice", "bob", "root", "admin"]
blacklist = ["root", "hacker"]
# Use for loop + break + else'''
# usernames = ["alice", "bob", "root", "admin"]
# blacklist = ["root", "hacker"]
# for username in usernames:
#     if username in blacklist:
#         print("Access denied")
#         break
# else:
#     print("Access granted")