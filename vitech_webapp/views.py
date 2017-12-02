# import flask modules
from flask import render_template, request, redirect, url_for, Flask

# import jinja2 environment
import jinja2

# import bootstrap
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Flask(__name__)

# initialize extensions
bootstrap.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/insurance', methods=['POST', 'GET'])
def insurance():
    return render_template('insurance.html')

@app.route('/trends', methods=['POST', 'GET'])
def trends():
    return render_template('trends.html')

if __name__ == "__main__":
    app.run(debug=True)

