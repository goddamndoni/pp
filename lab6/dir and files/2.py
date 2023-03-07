import os
def readabilty(path):
    print(os.access(path,os.R_OK))
def writeability(path):
    print(os.access(path,os.W_OK))
def executability(path):
    print(os.access(path,os.X_OK))
a = input()
readabilty(a)
writeability(a)
executability(a)
