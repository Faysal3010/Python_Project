from flask import Flask, render_template
from datetime import date
import random

app=Flask(__name__)
@app.route('/')
def index():
    today=date.today()
    random_num=random.randint(1,10)
    return render_template("index.html",num=random_num,date=today)


if __name__=='__main__':
    app.run(debug=True)