import flask, os, os.path
from flask import *

app = flask.Flask(__name__)
app.secret_key = "114514"


def page4():
    return send_file("/index.html")


@app.route("/")
def nonepage():
    return flask.redirect("/index.html")


@app.route("/<path:page>")
def mainpage(page):
    if os.path.isdir(page):
        page = page
        page += "/index.html"
    try:
        return flask.send_file(page)
    except FileNotFoundError:
        return page4()


app.run(host="0.0.0.0", port=80)