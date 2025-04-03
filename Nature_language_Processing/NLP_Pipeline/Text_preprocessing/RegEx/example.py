import re
# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")	
#   These are regular Expression
# [^a..b$]

# MetaCharacters
# Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

# [] . ^ $ * + ? {} () \ |


# [] bracket

text=" Hello, world!"
# print(re.findall(r"[a-zA-Z]", text))  # Output: ['H', '
pattern='[e-l]'
print(re.match(pattern,text))