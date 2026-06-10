import re
text = " John doe: john.doe@example.com, Jane doe: jane.doe@example.com"

emails = re.findall(r'\b\w+\.\w+@\w+\.\w+\b',text)
emails_pattern= re.findall(r'(\b\w+)\.(\w+)@(\w+)\.(\w+)\b',text)      
print(emails)
print(emails_pattern)