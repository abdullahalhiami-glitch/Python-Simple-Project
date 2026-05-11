import time as t

#start time of the program
start_time = t.time()

#function to calculate the total time of the program
def diff_time(time1,time2):
    return time2-time1

#heavy task
for i in range(1,500000):
    print(i)

#end time of the program
end_time = t.time()

#function calling
total_time = diff_time(start_time,end_time)

print(f"The for spend {total_time} second")