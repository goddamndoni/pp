import re
a = input()
find = re.findall('a[b]{2,3}', a)
print(find)