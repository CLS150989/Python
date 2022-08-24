class Persona:
    edad = 27
    nombre = "Victor"
    país = "Mex"


doctor = Persona
print("la edad es:  " , doctor.edad)
print("la edad es: ", getattr(doctor, 'edad' ))
print("el doctor tiene una edad?", hasattr(doctor,'edad'))
setattr(doctor, 'ahora se llama ', 'Héctor')
print(doctor.país)
delattr(Persona, 'país')


# delattr elimina un atributo 
# setattr : sirve para cambiar el valor de un atributo
# geattr: sirve para otorgar un atributo
# hasattr: comprueba si un objeto tiene determinado atributo
print(doctor.nombre)
 