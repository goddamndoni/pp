import re
txt = input()
find =  ('_'.join(
re.sub('([A-Z][a-z]+)', r' \1',
re.sub('([A-Z]+)', r' \1',
txt.replace('-', ' '))).split()).lower())
print(find)