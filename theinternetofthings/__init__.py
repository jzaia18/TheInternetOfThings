from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/")
def root():
    return redirect(url_for("about"))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
