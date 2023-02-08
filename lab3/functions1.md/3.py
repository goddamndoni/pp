def solve(numheads,numlegs):
    chikens = (numlegs -(4*numheads))/-2 
    rabits = numheads - chikens
    
    return "Rabits:" + str(rabits) +"\n" + "Chikens:" + str(chikens) 
a = 35
b = 94
print(solve(a,b))