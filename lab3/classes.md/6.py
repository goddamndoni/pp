class FilterPrime():
    def Prime(self, num):
        if(num < 2):
            return False
        else:
            for i in range(2,num):
                if(num % i == 0):
                    return False
        return True
    def Filter(self, listPrime):
        return filter(lambda x: self.Prime(x), listPrime)
l = []
a = int(input())
while a!=0:                          
    l.append(a)
    a = int(input())
p = FilterPrime()
p1 = list(p.Filter(l))
print(p1)

