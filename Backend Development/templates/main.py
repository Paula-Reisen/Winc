from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/")
def index(name="Index"):
    return render_template("index.html", title=name)

@app.route("/about")
def about(name="About"):
    return render_template("about.html", title=name)


@app.route('/home')
def home():
    return redirect(url_for('index'), 302)

@app.route('/navigate')
def navigate(name="Navigate"):
    return render_template("navigate.html", title=name)
