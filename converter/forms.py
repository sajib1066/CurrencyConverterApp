from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
import requests

class InputDataForms(FlaskForm):
    url = 'https://api.exchangeratesapi.io/latest'
    response = requests.get(url)
    curr = response.json()['rates'].keys()
    curr = list(curr)
    choice = []
    for i in curr:
        tpl = (i, i)
        choice.append(tpl)

    date = DateField("Enter Date in This Format(yyyy-mm-dd) ", validators=[DataRequired()])
    base = SelectField('base', choices=choice, validators=[DataRequired()])
    currency = SelectField('currency', choices=choice, validators=[DataRequired()])
    quantity = FloatField(f'How Much Currency You Convert?', validators=[DataRequired()])
    submit = SubmitField('Calculate')