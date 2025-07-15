from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Root </h1>'


@app.route("/home")
def home():
    return '<h1>Home</h1>'


@app.route("/user/<username>")
def user(username):
    return f'<h1>Hi, {username}</h1>'


@app.route("/<username>")
def say_hello(username):
    return f'<h1>Hello, {username }</h1>'


if __name__ == '__main__':
    app.run(debug=True)
