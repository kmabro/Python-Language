# import requests
# response = requests.get("https://www.iba-suk.edu.pk/")
# print(response.text)

'''___
Write a program using the `requests` module that sends a GET request to "https://api.github.com".
Print the status code and the first 200 characters of the response text.
___'''
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(response.text[:200])

'''___
Write a script that sends a POST request to "https://httpbin.org/post" with the JSON data: {"name": "Ali", "city": "Karachi"}.
Print the returned JSON response.
___'''
# import requests
# url = "https://httpbin.org/post"
# data = {"name": "Ali", "city": "Karachi"}
# response = requests.post(url, json=data)
# print(response.json())

'''___
Ask the user to enter a URL. Then send a GET request to that URL using the `requests` module.
If the status code is 200, print "Success", else print the status code.
___'''
# import requests
# url = input("Enter a URL: ")
# response = requests.get(url)
# if response.status_code == 200:
#     print("Success")
# else:
#     print(response.status_code)

'''___
Use the `requests` module to get JSON data from "https://jsonplaceholder.typicode.com/todos/1".
Parse and print the 'title' and 'completed' values from the JSON response.
___'''
# import requests
# url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(url)
# print(response.json()['title'], response.json()['completed'])

'''___
Create a Python program that:
1. Takes a GitHub username from the user,
2. Sends a GET request to "https://api.github.com/users/<username>",
3. Displays the number of public repos and followers for that user.
(Hint: Use `.json()` method)
___'''
# import requests

# username = input("Enter GitHub username: ")
# url = f"https://api.github.com/users/{username}"

# response = requests.get(url)
# data = response.json()

# print("Public repos:", data['public_repos'])
# print("Followers:", data['followers'])

