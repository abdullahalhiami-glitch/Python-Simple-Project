# commit: import the time module to measure execution duration
import time

# commit: define a heavy task that sums numbers from 1 to 1,000,000
def heavy_task():
    total = 0
    for i in range(1, 1_000_001):
        total += i
    return total

if __name__ == '__main__':
    # commit: record the start time before running the heavy task
    start_time = time.time()

    # commit: run the heavy task
    result = heavy_task()

    # commit: record the end time after the task completes
    end_time = time.time()

    # commit: compute elapsed time in seconds and print it
    elapsed_seconds = end_time - start_time
    print(f"Sum result: {result}")
    print(f"Elapsed time: {elapsed_seconds:.6f} seconds")








# import time

# def heavy_task():
#     total = 0
#     for i in range(1, 1_000_001):
#         total += i
#     return total

# if __name__ == "__main__":
#     start = time.time()
#     heavy_task()
#     end = time.time()
#     print("Elapsed time:", end - start, "seconds")
