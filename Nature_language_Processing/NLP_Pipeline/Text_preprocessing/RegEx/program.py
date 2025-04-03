import re 
# name = 'I am 81 years old and i make money 100 online, that 500 arround 1000 dollars a month'

# Program to extract numbers from a string

string = 'I am 81 years old.i make money 100 online, that 500 arround 1000 dollars a month'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# result=re.findall(pattern='\d+',name)
# print(result)
