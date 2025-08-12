from flask import Flask, render_template
from datetime import date

app = Flask(__name__)
@app.route('/<string:name>')
def index(name):
    today = date.today()
    return render_template('index.html', name=name.title(), date=today)
if __name__ == '__main__':
    app.run(debug=True)