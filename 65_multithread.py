import threading
import time 

def send_email(user):
    print("Sending email to", user)
    time.sleep(2)# take 2 sec to send email
    print("Email sent to", user)

users = ["A","B","C","D"]

therads = []

for u in users:
    t = threading.Thread(target=send_email,args=(u,))
    t.start()
    therads.append(t)

for t in therads:
    t.join()

print("All email sent")