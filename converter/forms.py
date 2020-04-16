from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField
import requests

class InputDataForms(FlaskForm):
    date = DateField("Enter Date in this format(yyy-mm-dd): ")

    url = 'https://api.exchangeratesapi.io/latest'
    response = requests.get(url)
    curr = response.json()['rates'].keys()
    curr = list(curr)

    choice = []
    for i in curr:
        tpl = (i, i)
        choice.append(tpl)


    base = SelectField('base', choices=choice) # StringField("Enter Currency from Convert: (ex: USD)")
    currency = SelectField('currency', choices=choice) # StringField("Enter Currency to convert: (ex: JPY)")
    quantity = FloatField(f'How Much Currency you convert:')
    submit = SubmitField('Calculate')