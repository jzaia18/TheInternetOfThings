from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import random
from utils import cloudFunctions
from utils import mongoUtils
import base64

UPLOAD_FOLDER = "static/"
SERVER_ADDR = "http://theinternetofthings.vision"

# print(SSL._CERTIFICATE_PATH_LOCATIONS)
# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('theinternetofthings.key')
# context.use_certificate_file('theinternetofthings.crt')

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

@app.route("/tcg")
def tcg():
    return render_template("cardScan.html")

@app.route("/like/<mid>")
def like(mid):
    mongoUtils.like(mid)

@app.route("/dislike/<mid>")
def dislike(mid):
    mongoUtils.dislike(mid)

@app.route("/thing/<mid>")
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
