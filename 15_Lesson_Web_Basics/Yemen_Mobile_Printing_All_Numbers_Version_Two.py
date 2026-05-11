'''
Docstring for 15_Lesson_Web_Basics.Yemen_Mobile_Printing_All_Numbers
Prints Numbers From 770000000 To 779999999 and all the numbers between them 
are "Ten Million" number with a CPU timing 
'''
import time as t

#start time of the program
start_time = t.time()

#function to calculate the total time of the program
def diff_time(time1,time2):
    return time2-time1

#printing all numbers from 770000000 to 77999999999
#heavy task
#Faster version 
start = 770000000
end = 779999999

with open("numbers.txt", "w") as file:
    for num in range(start, end + 1):
        file.write(f"{num}\n")

print("Done.")

#end time of the program
end_time = t.time()
#function calling
total_time = diff_time(start_time,end_time)


print(f"The for spend {total_time} second")
# The for spend 480.14234590530396 second