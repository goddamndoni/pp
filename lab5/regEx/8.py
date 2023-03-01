import re
txt = input()
find = re.findall('[A-Z][^A-Z]*',txt)
print(find)