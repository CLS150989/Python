from ast import Pass


class Vehiculo():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True  

    def frenar(self):
        self.frena = True
    
    def estado(self):
        print("Marca: ", self.marca , 
        "\nModelo: ", self.modelo, 
        "\n En marcha: ", self.enmarcha,
        "\n Acelera: ", self.acelera,
        "\n Frena: ", self.frena)


class Moto(Vehiculo):
    pass
