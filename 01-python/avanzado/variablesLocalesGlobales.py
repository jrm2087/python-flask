# variables locales y globales

# globales
numero = 87
texto = 'José'


def funcion1():
    # variables local
    numero2 = 29
    saludos = 'Buenos días'
    print(numero2, saludos)
    print(locals())


# funcion1()
print(numero, texto)
print(globals())
print(globals()['__file__'])
