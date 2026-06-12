import threading

def count(name):
    x = 0
    for _ in range(10**7):
        x += 1
    print(name,"done")

t1 = threading.Thread(target=count,args=("T1",))
t2 = threading.Thread(target=count,args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()