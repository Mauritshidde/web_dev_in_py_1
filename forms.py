from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, email_validator, EqualTo

class AcountmakenForm(FlaskForm):
    username = StringField('username: ', validators=[DataRequired()])
    password = PasswordField('password: ', validators=[DataRequired()])
    submit = SubmitField('Maak acount')

class AddproductForm(FlaskForm):
    product = StringField('naam van het product: ', validators=[DataRequired()])
    product_soort = StringField('Wat voor soort product is het: ', validators=[DataRequired()])
    product_prijs = IntegerField('Prijs van het product: ', validators=[DataRequired()])
    submit = SubmitField('Add product ')
