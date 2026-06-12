import os

class set_env_var:
    def __init__(self,var_name,new_value):
        self.var_name = var_name
        self.new_value = new_value

    def __enter__(self):
        self.original_val = os.environ.get(self.var_name)
        os.environ[self.var_name] = self.new_value

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.original_val is None:
            del os.environ[self.var_name]
        else:
            os.environ[self.var_name] = self.original_val

def show_temperature():
    if os.environ.get("TEMP_UNIT") == "F":
        return "Temperature: 98.6°F"
    else:
        return "Temperature: 37°C"




os.environ["TEMP_UNIT"] = "C"

print("Before:", show_temperature())

with set_env_var("TEMP_UNIT","F"):
    print("Inside:",show_temperature())

print("After:",show_temperature())