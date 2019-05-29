# web-practice-backend
Repository for backend practice

## Notes

### Quickstart
source: http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application


#### App Initialization

```python
import flask from Flask
```

importing Flask class which will be WSGI applcation.

```python
app = Flask(__name__)
```

'\__name\__': if it is started as application
If it is imported as module, then '\__name\__' should be replaced with the module name.

```python
@app.route('/')
def func():
    ...
```

route() decorator: telling Flask what URL should trigger our function.

Note that it is better not to save the app file name as 'flask.py' because it might crash with the original Flask file.

To run the app.py with flaska, you should export FLASK_APP as environment variable:


```commandline
export FLASK_APP=app.py
```
 
if you want locally ran flask app to be open to external users, you can type like this in command:

```commandline
flask run --host=0.0.0.0
```

#### Development Mode
```commandline
export FLASK_ENV=development
```

Development Mode do the followings:

1. Activates the debugger
2. Activates the automatic reloader
3. Enabled the debug mode on the Flask App.

#### Router : Variable
```python
@app.route('/<converter:variable>')
```

available converter list:

1. string (default): accepts any string without slash(' / ')
2. int: positive int
3. float: positive floating point values
4. path: similar with string, but slash(' / ') is acceptable
5. uuid: uuid strings


#### Redirection Behavior: trailing slash?

1. /path
2. /path/

Above two paths redirects differently.

#### URL building

```python
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

/
/login
/login?next=/
/user/John%20Doe
```

*url_for(function name, param1=value, ...)*

if param is a part of url: pass it as path for the corresponding part

if param is not a part of url: pass it as query string parameter at the end of url

#### Methods

Operates based on RFC 2068.

*RFC2068: RFC doc which standardized HTTP 1.1 spec

#### PASS: static files
Don't get this part

#### partial pass: render_template
Don't get the 'package' part

Restart from this part

