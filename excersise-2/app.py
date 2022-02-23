import numbers
from flask import Flask,render_template,request



app=Flask(__name__)


@app.get("/")
def index():
    return render_template('index.html')



@app.post("/calculate")
def calculate():
    number=request.form.get("number")
    return_text=""
    try:
        if(number is None):
            return_text="No number provided"
        number=int(number)
        if number%2==0:
            return_text=f"{number} is a even number"
        if(number%2!=0):
            return_text=f"{number} is not a even number"
            
    except ValueError:
        return_text=f"{number} is not a integer!"

    return render_template("calculate.html",number=return_text)
