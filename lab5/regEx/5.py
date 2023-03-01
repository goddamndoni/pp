import re 
txt = input()
find = re.findall('a.*b',txt)
print(find)