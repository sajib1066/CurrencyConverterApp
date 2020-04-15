from flask import render_template, flash
import requests
from converter import app
from converter.forms import InputDataForms


@app.route('/', methods=['GET', 'POST'])
def home():
    forms = InputDataForms()
    if forms.validate_on_submit():
        date = forms.date.data
        base = forms.base.data
        currency = forms.currency.data
        quantity = forms.quantity.data
        
        base_url = 'https://api.exchangeratesapi.io/latest'
        url = base_url + '?base=' + base + '&symbols=' + currency
        response = requests.get(url)
        if (response.ok is False):
            flash(f'Error: {response.status_code}')
            flash(f"{response.json()['error']}")
        else:
            data = response.json()
            total = quantity*data['rates'][currency]
            flash(f"{quantity} {base} = {total} {currency} day of {date}")

    return render_template('home.html', form=forms)