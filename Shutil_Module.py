'''___
Write a program that asks the user for a file name and a destination name.
Use `shutil.copy()` to copy the file to the destination.
Print a success message after the copy is complete.
___'''
# import shutil
# file_name = input("Enter the file name: ")
# destination_name = input("Enter the destination name: ")
# shutil.copy(file_name, destination_name)
# print("File copied successfully!")

'''___
Ask the user for a file name and a new location (including the new name).
Use `shutil.move()` to move and rename the file.
Show a confirmation message to the user.
___'''
# import shutil
# file_name = input("Enter the file name: ")
# new_location = input("Enter the new location (including the new name): ")
# shutil.move(file_name, new_location)
# print("File moved and renamed successfully!")

'''___
Create a script that takes the name of a directory from the user.
Use `shutil.rmtree()` to delete the entire directory and its contents.
Warn the user before deleting and confirm with input.
___'''
# import shutil
# dir_name = input("Enter the directory name: ")
# print(f"Are you sure you want to delete {dir_name} and all its contents? (y/n)")
# if input() == "y":
#   shutil.rmtree(dir_name)
#   print("Directory deleted successfully!")
# else:
#   print("Operation cancelled.")



