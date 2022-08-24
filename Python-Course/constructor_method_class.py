class Rectangulo:
    def __init__(self, largo, ancho) -> None:
        self.lar = largo
        self.an = ancho
    def area(self):
        return self.lar * self.an


rec = Rectangulo(8,9)
print(rec.area)
