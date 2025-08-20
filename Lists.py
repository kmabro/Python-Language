'''Create a list of five fruit names and print the third fruit.'''
# fruits = ["Apple","Banana","Cherry","Date","Elderberry"]
# print(fruits[2])

'''Given colors = ["Red", "Green", "Blue", "Yellow", "Green"], use:

Positive indexing to print "Blue".

Negative indexing to print the last "Green".'''
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# print(colors[2])
# print(colors[-1])
# #print(colors[len(colors)-1])

'''Ask the user to enter a color. If the color exists in the colors list, print "Color found", otherwise print "Color not found".'''
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# color = input("Enter a color: ").strip().capitalize()
# if color in colors:
#      print("Color found")  
# else:
#      print("Color not found")

'''Given users = ["admin", "guest", "root", "sysadmin"], write a program to:

Ask the user to input a username.

If the name is "root" or "admin", print “Restricted access”.

Else, print “Access allowed”.'''
# users = ["admin", "guest", "root", "sysadmin"]
# username = input("Enter a username: ")
# if "root" or "admin" in users:
#     print("Restricted access")
# elif "guest" or "sysadmin" in users:
#     print("Access allowed")
# else:
#     print("Invalid username")

'''devices = ["router", "switch", "firewall", "loadbalancer", "access point", "modem", "bridge"]

Print all devices from index 2 to 5.

Print the last 3 devices using negative indexing.

Print every second device from the list.'''
# devices = ["router", "switch", "firewall", "loadbalancer", "access point", "modem", "bridge"]
# print(devices[2:6])
# print(devices[-3:]) #print(devices[len(devices)-3:])
# print(devices[::2])

'''You’re given a list of usernames. Only allow usernames longer than 6 characters and not containing the word "admin".
usernames = ["john", "admin_root", "alice123", "bob", "superuser", "admin"]
Use a list comprehension to filter valid usernames and print them.'''
# usernames = ["john", "admin_root", "alice123", "bob", "superuser", "admin"]
# valid_usernames = [user for user in usernames if len(user) > 6 and "admin" not in user]
# print(valid_usernames)

'''Given a list of email addresses:
emails = ["alice@example.com", "bob@test.com", "admin@site.com", "user123@mail.com"]

Create a new list that includes only those emails containing "@" and ending with .com.

Filter out any email containing the word "admin".'''
# emails = ["alice@example.com", "bob@test.com", "admin@site.com", "user123@mail.com"]
# v_e = [email for email in emails if "@" in email and email.endswith(".com") and "admin" not in email]
# print(v_e)

'''Create a list of integers. Print only the even numbers using list comprehension.'''
# ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# even_nums = [num for num in ints if num%2==0]
# print(even_nums)

'''Write a program that:

Asks the user to enter 5 numbers (store them in a list).

Then prints the maximum and minimum numbers using max() and min().'''
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))
# num5 = int(input("Enter 5th number: "))
# nums = [num1,num2,num3,num4,num5]
# print(nums)
# maxi = max(nums)
# mini = min(nums)
# print("Maximum number is:",maxi)
# print("Minimum number is:",mini)
##### Enhanced Version #####
# nums = []
# for i in range(1,6):
#   num = input("Enter a number: ")
#   nums.append(num)
# print(nums)
# print("Maximum number is:",max(nums))
# print("Minimum number is:",min(nums))

'''passwords = ["admin123", "welcome", "123456", "safePass", "rootaccess", "letmein"]
Use list comprehension to filter out passwords shorter than 8 characters or that contain "123".'''
# passwords = ["admin123", "welcome", "123456", "safePass", "rootaccess", "letmein"]
# v_p = [password for password in passwords if len(password) >= 8 and "123" not in password]
# print(v_p)

################## List Methods ##################
'''colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
# Sort this list in ascending and descending order.'''
# colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
# print("Original list:",colors)
# colors.sort()
# print("ascending order: ", colors)
# colors.sort(reverse=True)
# print("descending order: ",colors)

'''numbers = [10, 20, 30, 40, 50]
# Print the list in reverse order using reverse() method.'''
# numbers = [10, 20, 30, 40, 50]
# numbers.reverse()
# print(numbers)

'''users = ["admin", "guest", "root", "admin", "sys"]
# Find the index of the first occurrence of "admin"'''
# users = ["admin", "guest", "root", "admin", "sys"]
# print(users.index("admin"))

'''attempts = [1, 2, 3, 1, 4, 2, 2, 5]
# Count how many times 2 occurs'''
# attempts = [1, 2, 3, 1, 4, 2, 2, 5]
# print(attempts.count(2))

'''passwords = ["admin123", "letmein", "secure#2023"]
# Make a copy of the list and add a new password in the copy.
# Ensure the original list remains unchanged.'''
# passwords = ["admin123", "letmein", "secure#2023"]
# c_passwords = passwords.copy()
# c_passwords.append("dummy_password")
# print(c_passwords)

'''alerts = ["scan started", "scan completed"]
# Insert "malware detected" between the two logs.'''
# alerts = ["scan started", "scan completed"]
# alerts.insert(1,"malware detected")
# print(alerts)

'''raw_logs = ["[ALERT]", "[OK]", "[ALERT]", "[INFO]", "[ALERT]"]
# Count how many alerts are there.
# Remove all entries except "[ALERT]" using slicing or filtering.'''
# raw_logs = ["[ALERT]", "[OK]", "[ALERT]", "[INFO]", "[ALERT]"]
# print(raw_logs.count("[ALERT]"))
# for i in raw_logs:
#     if i != "[ALERT]":
#         raw_logs.remove(i)
# print(raw_logs)

'''tcp_services = ["http", "https", "ftp"]
udp_services = ["dns", "snmp"]
# Combine both lists using + and also using extend().'''
# tcp_services = ["http", "https", "ftp"]
# udp_services = ["dns", "snmp"]
# t = tcp_services + udp_services
# print(t)
# tcp_services.extend(udp_services)
# print(tcp_services)

'''menu = ["Login", "Register"]
# Add "About", "Help", and "Contact" using extend()
# Then reverse the menu and print it.'''
# menu = ["Login", "Register"]
# menu.append("About")
# menu.append("Help")
# menu.append("Contact")
# menu.reverse()
# print(menu)

'''scores = [50, 70, 90, 85, 95, 90, 100]
# Sort scores and print the highest 3 scores (no duplicates).'''
scores = [50, 70, 90, 85, 95, 90, 100]

'''suspicious_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.2"]
logs = ["192.168.1.10", "192.168.1.11", "10.0.0.5", "127.0.0.1"]
# Count how many suspicious IPs are in the logs using count() or a loop'''
# suspicious_ips = ["192.168.1.10", "10.0.0.5", "172.16.0.2"]
# logs = ["192.168.1.10", "192.168.1.11", "10.0.0.5", "127.0.0.1"]
# count = 0
# for ip in suspicious_ips:
#     if ip in logs:
#         count += 1
# print("Number of suspicious IPs found in logs:", count)


