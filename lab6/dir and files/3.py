import os
def ifExist(path):
    if os.path.exists(path)==True:
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                print(i)
    if os.path.exists(path)==False:
        print("no such path")
a = input()
ifExist(a)        
