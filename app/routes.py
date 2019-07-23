from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/doMath", methods = ["GET", "POST"])
def doMath():
    if request.method == "GET":
        return "Please fill out the form"
    else:
        data = dict(request.form)
        firstNum = data["firstNum"][0]
        secondNum = data["secondNum"][0]
        operation = data["operation"][0]
        answer=0
        if firstNum == "7" and secondNum == "5" and operation == "mod":
            return render_template("egg.html")
        elif operation == "plus" or operation=="add" or operation=="+":
            answer=float(firstNum)+float(secondNum)
        elif operation == "subtract" or operation=="sub" or operation=="-":
            answer=float(firstNum)-float(secondNum)
        elif operation == "multiply" or operation=="times" or operation=="mult" or operation=="x" or operation=="*":
            answer=float(firstNum)*float(secondNum)
        elif operation == "divide" or operation=="div" or operation=="/":
            answer=float(firstNum)/float(secondNum)
        elif operation == "mod" or operation=="modular" or operation=="%":
            answer=float(firstNum)%float(secondNum)
        
        if answer == 42.0:
            return render_template("life.html")
        # prfloat(answer)
        return render_template("answer.html", firstNum = firstNum, secondNum = secondNum, operation = operation, answer=answer)