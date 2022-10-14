
class Rectangulo:
    def __init__(self, largo, alto, prof):
        self.largo = 0
        self.alto = 0 
        self.set_alto(alto)
        self.set_largo(largo)
      
    
    
    def set_alto(self, num):
        if (not(isinstance( num, int)and(num > 0))):
            raise ValueError("altura invalida {}".format(num))
        self.alto = num
    

    def set_largo(self, num):
        if(not(isinstance(num, int)and(num > 0))):
            raise ValueError("longitud inválida: {}".format(num))
        self.largo = num 
    
    def get_area(self):
        return self.largo * self.alto



r1 = Rectangulo(-3, -7)
print(r1.get_area())



