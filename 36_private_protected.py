class person:
    def __init__(self,name,age):
        self.name = name
        self._protected_age = age
        self.__private_ssn = "123-456"

    def show_public(self):
        print("Public method called.")

    # protected method
    def _show_protected(self):
        print("Protected method called.")

    # private method
    def __show_private(self):
        print("Private method called.")

    # helper method to access private data safely
    def get_ssn(self):
        return self.__private_ssn


class employee(person):
    def display(self):
        print("\n--- Inside Child Class ---")

        # public: accessible
        print("Name:",self.name)

        # protected: accessible in subclass
        print("Age (Protected):",self._protected_age)
        self._show_protected()

        # private: NOT directly accessible
        try:
            print(self.__private_ssn)
        except AttributeError:
            print("Cannot access __private_ssn directly!")

        # private method also NOT accessible
        try:
            self.__show_private()
        except AttributeError:
            print("Cannot accesss __show_private directly!")

emp = employee("John",30)

print("\n--- Outside Class ---")

# public
print(emp.name)
emp.show_public()

# protected (works but not recommended)
print(emp._protected_age)
emp._show_protected()

# private (fails)
try:
    print(emp.__private_ssn)
except AttributeError:
    print("Cannot access private attribute directly!")

# correct way (getter)
print("Access private via method:", emp.get_ssn())


emp.display()

