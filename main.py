from flask import Flask 
from flask import render_template
from flask import request

import forms
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/<nombre>', methods = ['GET', 'POST'])
def index(nombre='SALAME!'):
	listanombres = ['vos','dios','todos']
	formulario1 = forms.Formulario1(request.form)

	if request.method == 'POST':
		print formulario1.usuario.data
		print formulario1.correo.data
		print formulario1.comentario.data
		
	return render_template('index.html', nombre=nombre, milista=listanombres, formulario1=formulario1)



@app.route('/sub1')
def sub1():
	var1 = 'sarasa'
	lista1 = ['a','b','c','d']
	return render_template('sub1.html', var1=var1, lista1=lista1)

if __name__=='__main__':
	app.run(debug=True)
