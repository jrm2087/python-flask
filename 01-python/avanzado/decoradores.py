# decoradores

def asteriscos(funcion):
    def poner_asteriscos():
        print('******************')
        funcion()
        print('******************')

    return poner_asteriscos()


@asteriscos
def imprimir():
    print('hola, buenos dias')


# asteriscos(imprimir)

imprimir()
