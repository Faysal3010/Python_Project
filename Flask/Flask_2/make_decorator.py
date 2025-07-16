from flask import Flask

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

app=Flask(__name__)

@app.route('/')
@bold
@italic
def index():
    return "<h1>Root</h1>"

if __name__=="__main__":
    app.run(debug=True)

    
