from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class FormularioEntrada(FlaskForm):
    algarismo = IntegerField('', validators=[DataRequired("")])
    submmit = SubmitField('Traduzir')

