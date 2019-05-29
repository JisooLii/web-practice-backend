from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/user/')
@app.route('/user/<user_id>')
def login_user(user_id=None):
    # return 'Hello, {}'.format(user_id)
    return render_template('index.html', name=user_id)

@app.route('/user/<user_id>/')
def login_user_resource(user_id):
    return 'This page is {}\'s file resources page'.format(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Directing to server...'
    else:
        return 'Welcome, Login Complete.'

"""
# I don't get this part
static_url = url_for('static', filename='styles/style.css')


@app.route(static_url)
def index_static():
    return 'Index Page with Static'
"""

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login_user', user_id='testuser123'))
    print(url_for('login_user', user_id='testuser123', password='1234'))