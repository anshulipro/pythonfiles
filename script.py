i = int(input())

if i%2==0: print("even")
else: print("odd")

class anshul():
    def __init__(self,name,y):
       self.name = name
       self.y = y
    def display(self):
       print(self.name, self.y)

k = anshul(10,9)

k.display()