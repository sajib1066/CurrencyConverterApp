from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField

class InputDataForms(FlaskForm):
    date = DateField("Enter Date in this format(yyy-mm-dd): ")
    base = StringField("Enter Currency from Convert: ")
    currency = StringField("Enter Currency to convert:")
    quantity = FloatField(f'How much {base} you caonvert:')
    submit = SubmitField('Calculate')