# import flask modules
from flask import render_template, request, redirect, url_for, Flask, flash
from wtforms import Form, TextField, IntegerField, validators, SelectField, SubmitField

# import jinja2 environment
import jinja2

# import bootstrap
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    smoke = SelectField('Active Smoker (3+ / week)', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[validators.required()])
    number_covered = IntegerField('Number of Family Members Covered:', validators=[validators.required()])
    insured_amount = IntegerField('Insured Amount', default=500000, validators=[validators.required()])

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

# initialize extensions
bootstrap.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/insurance', methods=['POST', 'GET'])
def insurance():
    form = ReusableForm(request.form)

    print form.errors
    estimate = [20, 20, 20, 20]
    if request.method == 'POST':
        name = request.form['name']
        smoke = request.form['smoke']
        number_covered = request.form['number_covered']
        insured_amount = request.form['insured_amount']
        
        print name + smoke + number_covered + insured_amount
 
        if form.validate():
            pass
            estimate = [0,1,2,3]
        else:
            flash('Please fill in all form fields.')
 
    return render_template('insurance.html', form=form, estimate=estimate)

@app.route('/trends', methods=['POST', 'GET'])
def trends():
    return render_template('trends.html')

if __name__ == "__main__":
    app.run(debug=True)

