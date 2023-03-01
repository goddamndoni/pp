import re
txt = input()
find = re.findall('[A-Z]{1}+[a-z]+',txt)
print(find)