'''___
Write an async function `say_hello()` that waits for 2 seconds and then prints "Hello after 2 seconds".
Call this function using asyncio.run().
___'''
# import asyncio
# async def say_hello():
#   await asyncio.sleep(2)
#   print("Hello after 2 seconds")

# asyncio.run(say_hello())

'''___
Write two async functions: `task1()` and `task2()`. 
Each should print a start message, wait for 1 second using `await asyncio.sleep(1)`, and then print an end message.
Call both functions *concurrently* using `asyncio.gather()`.
___'''
# import asyncio
# async def task1():
#   print("Task 1 started")
#   await asyncio.sleep(1)
#   print("Task 1 ended")

# async def task2():
#   print("Task 2 started")
#   await asyncio.sleep(1)
#   print("Task 2 ended")

# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())

'''___
Create an async function that simulates downloading 3 files.
Each download waits 2 seconds and then prints "Downloaded file X".
Run all downloads in parallel using `asyncio.gather()`.
___'''
# import asyncio

# async def download_file(file_number):
#     print(f"Starting download of file {file_number}")
#     await asyncio.sleep(2)  
#     print(f"Downloaded file {file_number}")

# async def main():
#     await asyncio.gather(
#         download_file(1),
#         download_file(2),
#         download_file(3)
#     )

# asyncio.run(main())

'''___
Write an async function `delayed_sum(a, b)` that waits 1 second and returns the sum of a and b.
Call this function from a `main()` async function and print the result.
___'''
# import asyncio
# async def delayed_sum(a, b):
#   await asyncio.sleep(1)
#   return a + b

# async def main():
#   result = await delayed_sum(3, 5) 
#   print(f"The sum is: {result}")

# asyncio.run(main())

'''___
Modify the following code to use async properly so that it prints all messages without blocking:

# Original (wrong way):
def print_message():
    print("This is a message")

print_message()
print("Done")
___'''
# import asyncio

# async def print_message():
#     print("This is a message")

# async def main():
#     await print_message()
#     print("Done")

# asyncio.run(main())
