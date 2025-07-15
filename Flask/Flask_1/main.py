from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1> <h2>Welcome to my Flask app!</h2>'
@app.route("/home")
def home():
    return '<h1>This is the homepage</h1>'

@app.route("/about")
def about():
    return '<h1>This is the about page</h1>'

if __name__ =='__main__':
    app.run(debug=True)