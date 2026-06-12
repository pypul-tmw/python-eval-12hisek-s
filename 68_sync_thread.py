import threading 
import time 

semaphore = threading.Semaphore(5)


def tasks(name):
    print(f"{name} waiting...")

    with semaphore:
        print(f"{name} started")
        time.sleep(2)
        print(f"{name} finished")

threads = []


for i in range(5):
    t = threading.Thread(target=tasks,args=(f"Task {i}",))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

print("All tasks completed")


"""
If, 
semaphore = threading.Semaphore(5)
It shows that the Semaphore is working properly.
--Only 5 threads run at the same time
--Other tasks wait until a slot is free
--When one task finishes, the next one starts
"""