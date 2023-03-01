import re
txt = input()
find = re.findall('[A-Z][a-z]*',txt)
print(' '.join(find))