from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField

class Formulario1(Form):
	usuario = StringField('Nombre de usuario')
	correo = EmailField('Correo electronico')
	comentario = TextField('Comentario')