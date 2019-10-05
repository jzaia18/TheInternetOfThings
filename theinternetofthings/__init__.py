from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from utils import cloudFunctions

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/")
def root():
    return redirect(url_for("about"))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    print(cloudFunctions.getImageContents("http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg"))
    app.debug = True
    app.run(host="0.0.0.0")
