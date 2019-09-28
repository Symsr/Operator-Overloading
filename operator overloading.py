class A: 
    def __init__(self, a): 
        self.a = a 
    def __gt__(self, objek): 
        if(self.a > objek.a): 
            return True
        else: 
            return False
a = A(2) 
b = A(3) 
if(a > b): 
    print("A lebih besar dari B") 
else: 
    print("B lebih besar dari A") 
    
    def __init__(self, a): 
        self.a = a 
    def __lt__(self, objek): 
        if(self.a<objek.a): 
            return "C lebih kecil dari D"
        else: 
            return "D lebih besar dari C"
c = A(2)
d = A(3)
print(c < d)
print(d > c)
