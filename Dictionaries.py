'''# 1️⃣ Create a dictionary with name, age, and city of a person. Print the entire dictionary.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic)

'''# 2️⃣ Access and print the value of 'name' using square bracket syntax from the dictionary.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic['name'])

'''# 3️⃣ Use the `get()` method to access and print the value of 'city'.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic.get('city'))

'''# 4️⃣ Try to access a key that does not exist using square brackets. Observe the error.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic['height']) #KeyError: 'height'

'''# 5️⃣ Use the `get()` method to access a non-existing key and set a default value like "Not Found".'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic.get("height")) #None

'''# 6️⃣ Print all values from the dictionary using the `values()` method.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic.values())

'''# 7️⃣ Print all keys from the dictionary using the `keys()` method.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic.keys())

'''# 8️⃣ Use the `items()` method to print all key-value pairs from the dictionary.'''
# dic = {'name': 'Khan Muhammad', 'age':19, 'city':'Sukkur'}
# print(dic.items())

##### DICTIONARY METHODS #####

'''# 1️⃣ Update a student's age and add their grade using `update()`.
student = {'name': 'Ali', 'age': 17}
# Task: Update age to 19 and add a new key 'grade' with value 'A'.'''
# student = {'name': 'Khan Muhammad', 'age': 17}
# student.update({'age':19})
# student.update({'grade':'A'})
# print(student)

'''# 2️⃣ Remove the 'eligible' key from this dictionary using `pop()`.
info = {'name': 'Sara', 'age': 22, 'eligible': True}
# Task: Remove the 'eligible' field and print the updated dictionary.'''
# info = {'name': 'Sara', 'age': 22, 'eligible': True}
# info.pop('eligible')
# print(info)

'''# 3️⃣ Write a program to clear all entries in a dictionary of products using `clear()`.
products = {'apple': 5, 'banana': 8, 'cherry': 12}
# Task: Clear the dictionary and print it.'''
# products = {'apple': 5, 'banana': 8, 'cherry': 12}
# products.clear()
# print(products)

'''# 4️⃣ Simulate a user session dictionary and remove the last session using `popitem()`.
sessions = {
    'session_1': '10.0.0.1',
    'session_2': '10.0.0.2',
    'session_3': '10.0.0.3'
}
# Task: Remove the last session using popitem and print the remaining dictionary.'''
# sessions = {
#     'session_1': '10.0.0.1',
#     'session_2': '10.0.0.2',
#     'session_3': '10.0.0.3'
# }
# sessions.popitem()
# print(sessions)

'''# 5️⃣ You are managing a dictionary of IP bans.
# Delete an IP manually using the `del` keyword.

banned_ips = {'192.168.1.10': 'spam', '172.16.0.5': 'abuse', '10.0.0.7': 'brute force'}
# Task: Remove IP '172.16.0.5' using del and print the dictionary.'''
# banned_ips = {'192.168.1.10': 'spam', '172.16.0.5': 'abuse', '10.0.0.7': 'brute force'}
# del banned_ips['172.16.0.5']
# print(banned_ips)

'''# 6️⃣ You receive a list of user actions in the form of a dictionary.
# Remove a specific key if it exists, otherwise do nothing.

actions = {'login': 1, 'logout': 1, 'download': 3}
# Task: If 'upload' exists, remove it; if not, leave the dictionary unchanged.'''
# actions = {'login': 1, 'logout': 1, 'download': 3}
# if 'upload' in actions:
#     del actions['upload']
# print(actions)

'''# 7️⃣ Cybersecurity Twist:
# Simulate a log dictionary that stores counts of events by category.
# Update the log with new data and print the combined result.

log = {'INFO': 10, 'WARNING': 5}
new_data = {'ERROR': 2, 'INFO': 5}
# Task: Merge new_data into log using update().'''
# log = {'INFO': 10, 'WARNING': 5}
# new_data = {'ERROR': 2, 'INFO': 5}

# for key in new_data:
#     if key in log:
#         log[key] += new_data[key]
#     else:
#         log[key] = new_data[key]

# print(log)

'''# 8️⃣ Build a dictionary from a list of usernames and login attempts.
# Then remove users with 0 login attempts.

data = [('alice', 0), ('bob', 3), ('eve', 0), ('charlie', 2)]
# Task: Create a dictionary from this and remove entries where value == 0.'''
# data = [('alice', 0), ('bob', 3), ('eve', 0), ('charlie', 2)]
# users = dict(data)
# if 0 in users.values():
#     for key, value in list(users.items()):
#         if value == 0:
#             del users[key]
# print(users)
