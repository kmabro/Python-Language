'''
Write a program that asks the user to input two numbers.
Use time.time() to calculate how long it takes the user to provide both inputs.
Print the total time taken in seconds.
'''
# import time
# print("Please enter two numbers")
# start_time = time.time()
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# end_time = time.time()
# total_time = end_time - start_time
# print(f"Total time taken: {total_time:.2f} seconds")

'''
Create a program that counts down from 5 to 1 using time.sleep().
Display each number with a 1-second pause between them.
Finally, print "Time's up!" after the countdown ends.
'''
# import time
# for i in range(5, 0, -1):
#   print(i)
#   time.sleep(1)
# print("Time's up!")

'''
Write a Python program that prints the current time in the format:
"Today is: Monday, 29 July 2025 - 03:22 PM"
(Hint: Use time.strftime() with appropriate format codes)
'''
# import time
# print("Today is:", time.strftime("%A, %d %B %Y - %I:%M %p"))

'''
Create a program that prints "Processing..." 3 times, with a 0.5-second delay between each print.
Before and after the loop, show the timestamps using time.time().
Also, print the total time the loop took to run.
'''
# import time
# print(f"Start time: {time.time():.2f}")
# start_time = time.time()

# for i in range(3):
#   print("Processing...")
#   time.sleep(0.5)
  
# end_time = time.time()
# print(f"End time: {time.time():.2f}")

# total_time = end_time - start_time
# print(f"Total loop duration: {total_time:.2f} seconds")

'''
Create a simple digital clock that shows the current time in HH:MM:SS format.
Update the time every second for 10 seconds using a loop and time.sleep().
'''
# import time
# from time import strftime

# for i in range(10):
#   current_time = strftime("%H:%M:%S")
#   print(current_time)
#   time.sleep(1)

'''
Display a sentence to the user and ask them to type it exactly.
Use time.time() to measure how long they take to type it.
At the end, print how many seconds they took and whether their input was correct.
'''
# import time
# start_time = time.time()
# sc = input("Please type the following sentence exactly: \n\"The quick brown fox jumps over the lazy dog.\"\n=>")
# end_time = time.time()
# total_time = end_time - start_time
# if(sc == "The quick brown fox jumps over the lazy dog."):
#   print(f"Correct!, you took {total_time:.2f} seconds")
# else:
#   print(f"Incorrect!, you took {total_time:.2f} seconds")

'''
Ask the user to enter a number of seconds.
Use time.sleep() to wait for that many seconds.
After the wait, print a message like: "⏰ Time’s up! Take your break."
'''
# import time
# sec = int(input("Enter the number of seconds: "))
# time.sleep(sec)
# print("⏰ Time’s up! Take your break.")

'''
Write a program that keeps checking the system time.
When the system time reaches 30 seconds past the current minute (e.g., xx:xx:30), print "⏳ Action time!" and stop.
(Hint: Use time.strftime() to get seconds, and time.sleep() to avoid checking too often.)
'''
# import time 
# from time import strftime
# print("Waiting for the clock to reach 30 seconds...")
# while True:
#   current_time = strftime("%S")
#   if(current_time == "30"):
#     print("⏳ Action time!")
#     break
#   time.sleep(1)

'''
Print "Get ready..." and wait for 3 seconds.
Then randomly wait between 1 to 5 seconds and print "GO!".
Measure how quickly the user presses Enter after "GO!" appears.
Display their reaction time in seconds.
(Hint: Use input() and time.time())
'''
# import time
# import random
# print("Get ready...")
# time.sleep(3)

# time.sleep(random.randint(1, 5))
# print("GO!")

# start_time = time.time()
# input()
# end_time = time.time()
# total_time = end_time - start_time

# print(f"Your reaction time is {total_time:.2f} seconds")

