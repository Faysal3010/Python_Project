from flask import Flask

app = Flask(__name__)

# with open("index.html", "r", encoding="utf-8") as html_file:
#     content = html_file.read()


def make_em(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


@app.route('/')
def index():
    return "h1>Root</h1>"
    # return content


@app.route("/home")
@make_em
def home():
    return '<h1>Home</h1>'


# @app.route("/user/<username>")
# def user(username):
#     return f'<h1>Hi, {username}</h1>'


# @app.route("/<username>/<int:age>")
# def say_hello(username, age):
#     return f'<h1 style="text-align: center;">Hello, {username} your age: {age}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
