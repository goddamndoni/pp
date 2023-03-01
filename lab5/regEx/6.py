import re 
txt = input()
find = re.sub("[,. ]",":",txt)
print(find)
