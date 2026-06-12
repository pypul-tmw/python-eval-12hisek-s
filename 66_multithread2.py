import threading
import time 

def task(name,delay):
    print(name,"Started")
    time.sleep(delay)
    print(name,"Finished")

threads = [
    threading.Thread(target=task,args=("API Call",2)),
    threading.Thread(target=task,args=("File upload",3)),
    threading.Thread(target=task,args=("Logging",1)),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("All system tasks completed")