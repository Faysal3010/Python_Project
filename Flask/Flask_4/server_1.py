from flask import Flask, render_template
from datetime import date
import requests


app = Flask(__name__)


@app.route('/guess/<string:name>')
def index(name):
    parameters = {"name": name}
    response_0 = requests.get("https://api.genderize.io", params=parameters)
    gender = response_0.json()['gender']
    response_1 = requests.get("https://api.agify.io", params=parameters)
    age = response_1.json()['age']
    today = date.today()
    return render_template("name_gender.html", date=today, name=name.title(), gender=gender, age=age)


if __name__ == '__main__':
    app.run(debug=True)
