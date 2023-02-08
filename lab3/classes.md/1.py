class String:
    def getString(self):
        self.Input = input()
    def printString(self):   
        print(self.Input.upper())
x = String()
x.getString()
x.printString()