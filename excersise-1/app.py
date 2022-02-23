from datetime import datetime
from unicodedata import name
from flask import Flask,render_template,request
import datetime
import jinja2

app=Flask(__name__)


@app.get("/")
def index():
    time_data=datetime.datetime.now().strftime("%A, %B %d %Y %H:%M:%S")
    py_name = request.args.get(time_data)
    return render_template('index.html',time=time_data)
