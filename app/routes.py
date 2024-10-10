from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    donnees = request.form.get('prenom')

    test = "ceci est un test "
    return render_template('index.html', title='Home', test = test, donnees = donnees)