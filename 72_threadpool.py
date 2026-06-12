from concurrent.futures import ThreadPoolExecutor
import time 

def task(name):
    print(f"{name},started")
    time.sleep(2)
    print(f"{name},done")
    return f"result for {name}"

names = ["A","B","C","D"]

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(task,names)

print("All tasks are completed")

for i in results:
    print(i)

"""
@Why Thread Pool is better than manual threads
--No need to manually create/join threads
--Better performance control (max_workers)
"""