from ejemplo7 import db, Persona

persona = Persona.query.get(1)
persona.color = 'Gris'
db.session.add(persona)
db.session.commit()

personas = Persona.query.all()
print('Todas las personas')
print(personas)
