class Kreis:
    def __init__(self,Radius):
        self.setValue()
        
    def getFlaeche(self):    
        return 3.1415 * self.Radius ** 2
    
    def getUmfang(self):
        return 3.1415 * self.Radius * 2    
    
    def setValue(self,Radius):
        self.Radius=float(input("Enter the Radius: "))
        
        
class Rechteck:
    def __init__(self,length,depth):
        self.setValue()
    def getFlaeche(self):
        return self.length * self.depth
    
    def getUmfang(self):
        return (self.length + self.depth)*2
    
    def setValue(self,length,depth):   
        self.length=float(input("Enter the length: "))
        self.depth=float(input("Enter the depth: "))     
                   
                    
class Quadrat:
    def __init__(self,lenght):
        self.setValue()
        
    def getFlaeche(self):
        return self.length ** 2
    
    def getUmfang(self):
        return self.length * 4
    
    def setValue(self,length):
        self.lenght=float(input("Enter the lenght: "))

    
    
class GeometrieRechner:
    def __init__(self):
         self.setFigur()
         
    def setFigur(self):
        figur=None
        
        self.figur=str(input("choose the figure: "))
        if figur == 'Kreis':
            
            self.figur=Kreis()           
            
        elif figur == 'Quadrat':
             
             self.figur= Quadrat()
        
        elif figur == 'Rechteck':
             
            self.figur = Rechteck()  
        else:
            
          print('Diese Figur kenne ich nicht!')

    def getFlaeche(self):
        return self.figur.getFlaeche() 
        
        
    def getUmfang(self):
        return self.figur.getUmfang()
    
    


Calculate=GeometrieRechner()
Calculate.setFigur()
print("Fleache", Calculate.getFlaeche())
print("Umfang",Calculate.getUmfang())
        
