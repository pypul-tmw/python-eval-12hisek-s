import xml.etree.ElementTree as ET 

tree = ET.parse("employees.xml")

root = tree.getroot()

for employee in root.findall("employee"):
    emp_id = employee.find("id").text
    name = employee.find("name").text
    salary = employee.find("salary").text

    print(emp_id,name,salary)