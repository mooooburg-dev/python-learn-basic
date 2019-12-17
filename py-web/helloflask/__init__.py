from flask import Flask, g, Response, make_response

app = Flask(__name__)
app.debug = True # use only debug (debug mode)

@app.before_request
def before_request():
    print("before_request()")
    g.str = "한글"

@app.route("/res1")
def res1():
    custom_res = Response("Portfolio Response", 200, {'text':'111'})
    return make_response(custom_res)

@app.route("/gg")
def helloworld2():
    return "Hello Flask World " + getattr(g, "str", '111')

@app.route("/")
def helloworld():
    return "Hello Flask World"