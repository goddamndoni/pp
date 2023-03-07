import os 
def delete(path):
    if os.access(path,os.X_OK) == True:
        os.remove(path)
    if os.access(path,os.X_OK) == False:
        None
a = input()
delete(a)
