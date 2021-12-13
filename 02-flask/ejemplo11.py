from werkzeug.security import generate_password_hash, check_password_hash

password = 'joser'

password_enc = generate_password_hash(password)
print(password_enc)

verificar = check_password_hash(password_enc, 'joser2')
print(verificar)

verificar = check_password_hash(password_enc, 'joser')
print(verificar)
