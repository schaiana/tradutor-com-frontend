import tradutor
import re
import os

from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap

from forms import FormularioEntrada

app = Flask(__name__)

# CSRF Protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def inicio():
    form = FormularioEntrada()

    if form.validate_on_submit():
        algarismo = str(form.algarismo.data)
        if not tradutor.valida_algarismo(algarismo):
            return render_template('400.html', title='Bad request'), 400
        else:
            extenso = tradutor.obtem_extenso(int(algarismo))
            return render_template('index.html', title='Tradutor', form=form, res=extenso)
    return render_template('index.html', title='Tradutor', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Not found'), 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=(os.environ['PORT'] or 3000))
