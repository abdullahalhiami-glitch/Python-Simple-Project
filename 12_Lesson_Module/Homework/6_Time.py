import time as t

start_time = t.time()

def diff_time(time1,time2):
    return time2-time1

for i in range(1,500000):
    print(i)

end_time = t.time()


print(f"The for spend {diff_time(start_time,end_time)} second")