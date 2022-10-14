# 7.1 Ejercicio 1
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y
# DNI. Construye los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. Validar los datos
# ● mostrar(): Muestra los datos de la persona.
# ● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.



class Persona:
    def __init__(self, nombre= "", edad = 0, dni = "") -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni =  dni
        self.set_dni(dni)
        self.set_edad(edad)
        self.set_nombre(nombre)

#getters: 
    def get_edad(self):
        return print(self.edad)

    def get_dni(self):
        return print(self.dni)

    def get_nombre(self):
        return print(self.nombre)
            
#setters 
    def set_nombre(self, nombre):
        self.nombre = nombre 

    def set_edad(self, edad):
        self.edad = edad
    
    def set_dni(self, dni):
        self.dni = dni

#validadción de edad 
    def val_edad(self):
        if self.edad < 0:
            print("edad incorrecta")
        elif self.edad < 18:
            print("es menor de edad")
        else:
            print("es mayor de edad")

#metdo para mostrsar a la persona 
    def get_persona(self):
        return print("nombre: {} edad: {} DNI: {}".format(self.nombre, self.edad, self.dni))

p = Persona()

p.set_edad(2)
p.get_edad()
p.get_persona()







        

