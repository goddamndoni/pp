def reverseSentence(s):
    l = list(s.split())
    l = l[::-1]
    for i in l:
        print(i, end = ' ')
a = input()
print(reverseSentence(a))