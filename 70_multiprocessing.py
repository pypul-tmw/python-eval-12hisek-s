import multiprocessing 
import time 

def tasks(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=tasks, args=("Process 1", ))
    p2 = multiprocessing.Process(target=tasks, args=("Process 2", ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed")