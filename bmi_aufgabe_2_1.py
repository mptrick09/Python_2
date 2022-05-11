class UserDataTogetBmi:
  def __init__(self,name):
    self.name = name
    
  def __str__(self):
    return str(self.name) + ': ' + str(self.BMI)
  
  def GiveData(self,gewicht,groesse):      
      self.BMI = round(gewicht/(groesse**groesse))

      

  def GetTheBmiResulte(self):
      return  self.BMI

pp1=UserDataTogetBmi("Patrick")

pp1.GiveData(100,1.9)       
print(pp1) 
        
        
    