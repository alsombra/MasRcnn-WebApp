from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np



# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer







from flask import Flask, request, redirect, url_for, flash, jsonify#
import numpy as np#
import pickle as p#
import json#








import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle






app = Flask(__name__)





@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')




@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))     # uploads image/video file will save here.
        f.save(file_path)





if __name__ == '__main__':
     modelfile = 'model.py'
     model = (open(modelfile, 'rb')) #
     app.run(debug=True) #app.run(debug=True)
