class Kunde:
    def __init__(self,id, kontostand):
        self.__id=id
        self.__kontostand= kontostand
     
    def printinfo(self):
         print(self.__id, self.__kontostand)
    
class Privatkunde(Kunde):
    def __init__(self,id,kontostand,vorname):
        super().__init__(id, kontostand)
        self.vorname=vorname
        
    # def printinfo(self):
    #   print(self.__id, self.__kontostand, self.vorname)  
      
      
      
Pazzo=Privatkunde(1,20000000000,"Patrick")
print(Pazzo)    