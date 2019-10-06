from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import random
from time import sleep
from utils import cloudFunctions
from OpenSSL import SSL
import base64
import io

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

# testing this, will delete if fails
@app.route("/capture", methods=["POST"])
def capture():
    data = request.form["url"]
    encoded_data = data.split(',')[1]
    decoded_data = base64.b64decode(encoded_data)
    filename = "img/tmp/" + str(random.randint(0,999999999999)) + ".png"
    print(filename)
    print(UPLOAD_FOLDER + filename)
    f = open(UPLOAD_FOLDER + filename, "wb")
    f.write(decoded_data)
    f.close()
    print(SERVER_ADDR + url_for('static', filename=filename))
    ret = cloudFunctions.getImageContents(SERVER_ADDR + url_for('static', filename=filename))
    sleep(5)
    os.remove(UPLOAD_FOLDER + filename)
    return str(ret)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
