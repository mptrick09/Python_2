from pickletools import markobject


class Auto:
    def __init__(self,marke,preis,model,baujahr):
        self.__marke=marke
        self.__preis=preis
        self.__model=model
        self.__bauhajr=baujahr        
    
    def setMarke(self,marke):
        self.__marke= marke         
   
        
    def setPreis(self,preis):    
        self.__preis=preis 
        
    
    def setModel(self,Model):          
        self.__model=Model
        
    def SetBaujahr(self,baujahr):   
        self.__baujahr=baujahr     
       
        
    def getMarke(self): 
        return self.marke 
    
    def getPreis(self): 
        return self.preis
         
    def getModel(self):
        return self.model 
          
    def getBaujahr(self):
        return self.baujahr    
                  


chech1=Auto("Ford",4500,"Fuga",2006)  
chech1.SetBaujahr(2009)
print(chech1.bauhajr)
print(chech1.getModel(), " |", chech1.getMarke(), " |",chech1.getBaujahr())     