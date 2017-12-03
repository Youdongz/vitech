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

bar_graph_data = [1, 189, 206, 105, 121, 99, 145, 114, 119,
					169, 194, 5, 71, 4, 2, 93, 2, 43, 1, 73,
					27, 3, 40, 3, 4, 1, 4, 59, 66, 6, 1, 13,
					2, 20, 1]
@app.route('/trends', methods=['POST', 'GET'])
def trends():
    return render_template('trends.html', bar_graph=bar_graph_data)

if __name__ == "__main__":
    app.run(debug=True)

