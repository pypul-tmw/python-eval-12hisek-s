import threading 
import time 
barrier = threading.Barrier(3)

def worker(name):
    print(f"{name} is working...")
    time.sleep(2)
    
    print(f"{name} reached barrier")
    barrier.wait()
    
    print(f"{name} passed barrier")

threads = []

for i in range(3):
    t = threading.Thread(target=worker,args=(f"Task {i}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All tasks completed")

