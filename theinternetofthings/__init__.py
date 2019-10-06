from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
from utils import cloudFunctions

import numpy as np
import cv2
import re
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

# testing this, will delete if fails
@app.route('/capture', methods=["POST"])
def disp_pic():
    data = request.data
    encoded_data = data.split(',')[1]
    nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cloudFunctions.getImageContents("http://edge.rit.edu/edge/P15482/public/Photo Gallery/RIT_logo.jpg"))
    app.debug = True
    app.run(host="0.0.0.0")
