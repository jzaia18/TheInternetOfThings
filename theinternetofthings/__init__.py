from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os
import random
from utils import cloudFunctions
from utils import mongoUtils
import base64

UPLOAD_FOLDER = "static/"
SERVER_ADDR = "http://theinternetofthings.vision"

#authentication wrapper
def require_login(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'uname' not in session:
            flash("Please log in to use The Internet of Things")
            return redirect(url_for("root"))
        else:
            return f(*args, **kwargs)
    return inner


app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def root():
    if "uname" in session:
        return redirect(url_for("about"))
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["POST"])
def login():
    if ("username" in request.form and "password" in request.form):
        if (mongoUtils.authenticate(request.form["username"], request.form["password"])):
            user = mongoUtils.get_user(request.form["username"])
            if (user != None):
                session["uname"] = user["username"]
            return redirect(url_for("about"))
        else:
            flash("Wrong username or password")
            return redirect(url_for("root"))
    else:
        return redirect(url_for("root"))


@app.route("/signup", methods=["POST"])
def signup():
    if ("username" in request.form and "password" in request.form):
        if (mongoUtils.create_user(request.form["username"], request.form["password"])):
            session["uname"] = mongoUtils.get_user(request.form["username"])["username"]
            return redirect(url_for("about"))
        else:
            flash("That username is already taken")
            return redirect(url_for("root"))
    else:
        return redirect(url_for("root"))


@app.route("/logout")
def logout():
    session.pop("uname")
    return redirect(url_for("root"))

@app.route("/favicon.ico")
def favicon():
    return url_for('static', filename="img/logo.png")

@app.route("/snap")
def snap():
    return render_template("cameraAccess.html")

@app.route("/tcg")
def tcg():
    return render_template("cardScan.html")

@app.route("/like/<mid>")
def like(mid):
    mongoUtils.like(mid)

@app.route("/dislike/<mid>", methods=["POST"])
def dislike(mid):
    mongoUtils.dislike(mid)

@app.route("/thing/<mid>", methods=["POST"])
def thing(mid):
    print(mid, "/m/" + mid)
    thing = mongoUtils.get_thing("/m/" + mid)
    return render_template("displayThing.html", data=thing)

@app.route("/capture", methods=["POST"])
def capture():
    data = request.form["url"]
    encoded_data = data.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    filename = "img/tmp/" + str(random.randint(0,999999999999)) + ".png"
    f = open(UPLOAD_FOLDER + filename, "wb")
    f.write(decoded_data)
    f.close()
    ret = cloudFunctions.getImageContents(SERVER_ADDR + url_for('static', filename=filename))
    forbidden = mongoUtils.get_stopwords()
    i = 0
    for dic in ret:
        if dic['name'] in forbidden:
            i += 1
        else:
            break

    if i >= len(ret):
        i = 0

    success = mongoUtils.create_thing(ret[i])

    if success:
        os.rename(UPLOAD_FOLDER + filename, UPLOAD_FOLDER + "img/things/" + ret[i]["mid"][3:] + ".png")
    else:
        os.remove(UPLOAD_FOLDER + filename)

    return ret[i]["mid"][3:]

@app.route("/cardcapture", methods=["POST"])
def cardCapture():
    data = request.form["url"]
    encoded_data = data.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    filename = "img/tmp/" + str(random.randint(0,999999999999)) + ".png"
    f = open(UPLOAD_FOLDER + filename, "wb")
    f.write(decoded_data)
    f.close()
    ret = cloudFunctions.getImageText(SERVER_ADDR + url_for('static', filename=filename))

    os.remove(UPLOAD_FOLDER + filename)

    return ret

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
