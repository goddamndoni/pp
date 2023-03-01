import re
txt = input()
find = ("".join(x.capitalize() or '_' for x in txt.split('_')))
print(find)


