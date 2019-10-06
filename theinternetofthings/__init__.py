from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import random
from utils import cloudFunctions

import base64

import io

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def root():
    return redirect(url_for("about"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/snap")
def snap():
    return render_template("cameraAccess.html")

# testing this, will delete if fails
@app.route("/capture", methods=["POST"])
def capture():
    data = request.form["url"]
    encoded_data = data.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    filename = "img/tmp/" + str(random.randint(0,999999999999)) + ".png"
    f = open("static/" + filename, "wb")
    f.write(decoded_data)
    f.close()
    print(url_for('static', filename=filename))
    ret = cloudFunctions.getImageContents(url_for('static', filename=filename))
    print(ret)
    os.remove("static/" + filename)
    return str(ret)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", ssl_context='adhoc')
