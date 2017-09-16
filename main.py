from flask import Flask 
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<nombre>')
def index(nombre='SALAME!'):
	return render_template('index.html', nombre=nombre)

@app.route('/sub1')
def sub1():
	var1 = 'sarasa'
	lista1 = ['a','b','c','d']
	return render_template('sub1.html', var1=var1, lista1=lista1)

if __name__=='__main__':
	app.run(debug=True)
