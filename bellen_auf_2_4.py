from unicodedata import name


class Hund:
    
    def __init__(self,name, gewicht):
        self.__name=name
        self.__gewicht=gewicht    
    
    def Bellen(self):
        print("WOW WoW")
        
wiking=Hund("Tob", 11)
wiking.Bellen()        
       