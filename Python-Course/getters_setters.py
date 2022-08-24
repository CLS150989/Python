# métodos accesorios
# get siempre devuelve un valor
# 
# 
# get_ + atributo
# get get_estudo()
#
# 
#
# set envián valor hacia el interior de la clase
# 
# 
# set_ + atributo
# set_estudo()   con esta funcion siempre se envía un valor
# set_estudo(valor)

class Rectangulo:

    def __init__(self, longitud, altura):
        self.longitud = 0
        self.altura = 0
        self.longitud(longitud)
        self.altura(altura)

    @property
    def altura(self):
        return self.altura

    @altura.setter
    def altura(self, num):
        if(not (isinstance(num, int)and (num > 0))):
            raise ValueError("altura inválida: {} ".format(num))
        self.altura = num

    @property
    def longitud(self):
        return self.longitud


    @longitud.setter
    def longitud(self, num):
        if (not(isinstance(num, int) and (num > 0))):
            raise ValueError("longitud inválidad:  {}" .format(num))
        self.longitud = num

    @property
    def area(self):
        return self._altura * self._longitud




    r = Rectangulo(5 , 10)


    r.

    # altura = property(fget=_get_altura, fset=_set_altura)
    # longitud = property(fget=_get_longitud, fset=_set_longitud)
    # area = property(fget=_get_area_)
















