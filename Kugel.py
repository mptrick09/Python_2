class BelowZeroError(Exception):
    def __str__(self):
        return "Der übergebene Radius ist an die Klasse Kugel < 0 "
    
    
class Kugel:
    def __init__(self,Radius):
     self.__Radius=Radius 
     
     
    
    
    def getVolumen(self):
        
        if self.__Radius < 0:
                raise BelowZeroError()
        else: 
            result= 4/3*3.14*self.__Radius**3
            print(result)  
        
try:
    Kugel(4)    
    
      
except:    
    print(BelowZeroError())
        
        
    
    
Test=4  
print(Kugel(T))       