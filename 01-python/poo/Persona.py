class Persona:
    texto = ''

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        self.texto = f'Hola, soy {self.nombre}'
        return self.texto


class Adulto(Persona):
    tarjeta = ''

    def __init__(self, nombre):
        Persona.__init__(self, nombre)

    def __str__(self):
        self.texto = f'Adutlo : nombre = {self.nombre}'
        return self.texto

    def saludar(self):
        self.texto = 'Hola, soy adulto'
        return self.texto

    def grabar_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta


####

persona1 = Persona('José')
print(type(persona1))
print(persona1.nombre)
texto = persona1.saludar()
print(texto)

adulto1 = Adulto('Darío')
print(type(adulto1))
print(adulto1.saludar())
adulto1.grabar_tarjeta('871029')
print(adulto1.tarjeta)
print(adulto1)
