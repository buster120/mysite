from concurrent.futures import ThreadPoolExecutor
import time

def sleep_task(sleep_time):
    print(f"sleep {sleep_time} s")
    time.sleep(sleep_time)
    print(f"sleep {sleep_time} s")

executor=ThreadPoolExecutor(max_workers=2)
task1=executor.submit(sleep_task,2)
time.sleep(1)
print(task1.done())