from markupsafe import escape
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello Mision Codigo!</h1>'

@app.route('/about/')
def about():
    return '<h1>This is our about page</h1>'

@app.route('/cap/<s>/')
def cap(s):
    return f'<h1>{escape(s.capitalize())}</h1>'

@app.route('/add/<int:a>/<int:b>/')
def add(a, b):
    return f'<h1>Adding {a} and {b} is {a + b}</h1>'

@app.route('/login/<int:userid>/')
def login_user(userid):
    users = ['Leonardo', 'Raphael', 'Donnie']
    try:
        return f'<h1>Welcome {users[userid]}</h1>'
    except IndexError:
        abort(404)