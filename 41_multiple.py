class Loggermixin:
    def process(self):
        print("Logging transaction...")

        super().process()

class NotificationMixin:
    def process(self):
        print("Sending notifications...")

        super().process()

class account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def process(self):
        print(f"Final processing for {self.name}.")

class savingaccount(Loggermixin,NotificationMixin,account):
    def process(self):
        print("Starting saving account process")
        super().process()

acc = savingaccount("John",1000)
acc.process()