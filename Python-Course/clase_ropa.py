from html.entities import name2codepoint
import nturl2path


class Ropa:
    def __init__(self):
        self.marca = "willow"
        self.talla = "M"
        self.color = "rojo"
camisa = Ropa()
print(camisa.talla)
print(camisa.marca)


class Calculadora:
    def __init__(self, n1 , n2) -> None:
        self.suma = n1 + n2
        self.resta = n1 - n2  
        self.productoi = n1 * n2 
        self.division = n1 / n2 
    
        pass
Calc = Calculadora(2, 6)
print(Calc.resta)
