def add_logging_to_method(method):
    def new_method(self, *args, **kwargs):
        print(f"Calling method {method.__name__}")
        return method(self, *args, **kwargs)
    return new_method


def add_logging_to_all_method(cls):
    for name, method in vars(cls).items():
        if callable(method) and not name.startswith("__"):
            setattr(cls, name, add_logging_to_method(method))
    return cls


@add_logging_to_all_method
class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")


a = MyClass("Abhi")
a.say_hello()