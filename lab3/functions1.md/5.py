import itertools

def permutations(string):
  perms = [''.join(p) for p in itertools.permutations(string)]
  return (*perms, )
a = input()
print(permutations(a))