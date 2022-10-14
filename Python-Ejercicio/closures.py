from distutils.command.install_egg_info import safe_name


def saluda_usuario(username):
    mensaje= 'hola ' + username

    def saludar():
        print(mensaje)

    return saludar


saludo = saluda_usuario('carlos')
saludo()
del(saluda_usuario)
saludo()