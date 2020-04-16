from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField

class InputDataForms(FlaskForm):
    date = DateField("Enter Date in this format(yyy-mm-dd): ")
    base = StringField("Enter Currency from Convert: (ex: USD)")
    currency = StringField("Enter Currency to convert: (ex: JPY)")
    quantity = FloatField(f'How Much Currency you convert:')
    submit = SubmitField('Calculate')