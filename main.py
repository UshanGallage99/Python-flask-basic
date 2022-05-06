from distutils.log import debug
from unittest import result
from urllib import response
from flask import Flask,request,render_template

app =Flask(__name__)

app_scope="TEST APP SCOPE"

@app.route("/")
def index():
    var =request.args["test"]
    print(type(var))
    request_scope = "TEST REQ SCOPE"
    print(request_scope)
    print("Hello world")
    return "Hello world"

@app.route("/calc")
def calc():
    number_one = request.args["number-1"]
    number_two = request.args["number-2"]

    result = int(number_one)+int(number_two)
    return str(result)

@app.route("/vol/<base>/<height>")
def vol(base,height):
    # base = request.args["base"]
    # height = request.args["height"]

    result = int(base)*int(height)
    response_data={
        "result":result
    }
    print(type(response_data))
    return str(result)

@app.route("/view")
def view():
    return "<h1>Hello World</h1>"

@app.route("/view_index")
def view_from_file():
    name = request.args("name")
    age = request.args("age")
    response_view=open("index.html").read()
    response_view=response_view.replace("{{name}}",name)
    response_view=response_view.replace("{{age}}",age)
    return response_view

@app.route("/view_index2",methods=["GET","POST"])
def view_from_render(): 
    print(request.method)
    name="Empty"
    age="Empty"
    if request.method == "POST":
        if "name" in request.form:
            name = request.form["name"]
        if "age" in request.form:
            age = request.form["age"]

    return render_template("index.html",name=name,age=age)



print(app_scope)

if __name__=="__main__":
    app.run(debug=True)