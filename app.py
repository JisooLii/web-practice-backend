from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/user/<user_id>')
def login_user(user_id):
    return 'Hello, {}'.format(user_id)


@app.route('/user/<user_id>/')
def login_user_resource(user_id):
    return 'This page is {}\'s file resources page'.format(user_id)


