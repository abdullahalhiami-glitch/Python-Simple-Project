import os
import random
from datetime import datetime

#this method can reveal all the module methods inside any module
# print(dir(os))
# #and it works with any datatype that was built-in
# print(dir(random)) 
# print(dir(int))
# print(dir(str))

#this is a function that returns the Current Working path of the file you are working on and it will be like this C:\Users\ZBOOK 15 G6\Desktop\Coding\Python\Python_Course
# print(os.getcwd()) 
# os.chdir('C:/Users/ZBOOK 15 G6/Desktop/Coding/Python/')#this changes the path of the current working file
# print(os.getcwd()) 
os.chdir('C:/Users/ZBOOK 15 G6/Desktop/Coding/Python/Python_Course/11_Lesson_OS')
print(os.getcwd()) 

#this will print all the files that exists in that path or folder
print(os.listdir())

#this will create folders on your desktop we have two ways
#1. os.mkdir("here is the name of the folder") with this method we can't create a sub-folder it will give us an error
#1. os.mkdir("name of a folder / name of the sub folde") with this method we can't create a sub-folder it will give us an error
#2. os.makedirs("name of a folder / name of the sub folder")
# os.makedirs('12_lesson/13_lesson') # if we try to run it again it will give us an error because it can't create a file or a folder that already exists

#deleting or removing is the same as creating, but more dangerous than creating them
#1.os.mrdir("here is the name of the folder")
#2. os.removedirs("name of a folder / name of the sub folder")
# os.removedirs('12_lesson/13_lesson')

#rename any thing here just 
# os.rename('4.pdf','Abdullah.pdf')

# #printing out all file information from a file
# print(os.stat('Abdullah.pdf'))
# print(os.stat('Abdullah.pdf').st_size) #size of a file in bytes
# print(os.stat('Abdullah.pdf').st_mtime) #last modified time for this document
# #to convert it to a readable time we do the following
# mod_time = os.stat('Abdullah.pdf').st_mtime
# mod_time2 = os.stat('2.jpg').st_mtime
# #this will show the last modified time of that file
# print(datetime.fromtimestamp(mod_time))
# print(datetime.fromtimestamp(mod_time2))
# print(os.listdir())

#printing the desktop tree file system
# os.chdir('C:/Users/ZBOOK 15 G6/Desktop/')
# for dirpath, dirnames, filenames in os.walk('C:/Users/ZBOOK 15 G6/Desktop/'):
#     print(f"Current Path: {dirpath}")
#     print(f"Directories: {dirnames}")
#     print(f"Files: {filenames}")
#     print()

