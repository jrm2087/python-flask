from flask_bcrypt import Bcrypt

generador = Bcrypt()

password = 'jrm2087'
password_enctriptada = generador.generate_password_hash(password)
print(password_enctriptada)

verificar = generador.check_password_hash(password_enctriptada, 'jrm20871')
print(verificar)

verificar = generador.check_password_hash(password_enctriptada, 'jrm2087')
print(verificar)
