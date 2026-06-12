import os

class set_env_var:
    def __init__(self, var_name, new_value):
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

os.environ["MODE"] = "Production"
print("Before:",os.environ["MODE"])

with set_env_var("MODE","Development"):
    print("Inside:",os.environ["MODE"])

print("After:",os.environ["MODE"])