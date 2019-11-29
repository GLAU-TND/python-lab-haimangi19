class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        return (self.v)
def Xyz(a,b):
    return a+b
a=int(input())
b=int(input())
c=Xyz(a,b)
if c<150:
    raise MyException("Custom Exception Occurred")
else:
    print(c)   


            
    
