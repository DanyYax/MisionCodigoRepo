from markupsafe import escape
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/cap/<s>/')
def cap(s):
    return f'<h1>{escape(s.capitalize())}</h1>'

@app.route('/add/<int:a>/<int:b>/')
def add(a, b):
    return f'<h1>Adding {a} and {b} is {a + b}</h1>'

@app.route('/login/<int:userid>')
def login_user(userid):
    users = ['Leonardo', 'Raphael', 'Donnie']
    try:
        return f'<h1>Welcome {users[userid]}</h1>'
    except IndexError:
        abort(404)

@app.route('/messages/')
def see_messages():
    # This data usually comes from APIs or a DB
    user = "Dany"
    tasks = [
        {"text": "Read a book", "status": "In Progress"},
        {"text": "Go to the Gym", "status": "In Progress"},
        {"text": "Like this Video", "status": "COMPLETE"},
        {"text": "Learn a new skill", "status": "In Progress"},
    ]
    return render_template("messages.html", user=user, tasks=tasks)