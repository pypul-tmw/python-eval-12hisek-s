import threading
import time 

balance = 1000
lock = threading.Lock()

def withdraw(user,amount):
    global balance

    print(f"{user} trying to withdraw {amount}")

    with lock:
        if balance >= amount:
            time.sleep(1)
            balance -= amount
            print(f"{user} withrawal successful. remaining balance: {balance}")
        else:
            print(f"{user} insufficient balance. current balance:{balance}")

users = [
    ("A",400),
    ("B",500),
    ("C",300),
    ("D",300),
    ("E",1200)
]

threads = []
for u,amt in users:
    t = threading.Thread(target=withdraw, args=(u,amt))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Final balance:", balance)