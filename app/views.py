from flask import Flask, render_template, jsonify, Response
import pandas as pd
from flask import request
from os.path import join, dirname, realpath
import os
from PIL import Image
from base64 import decodestring
import io
from io import BytesIO
import base64
from werkzeug.utils import secure_filename
from mednet import MedNet
from apps import predict
app = Flask(__name__, template_folder='templates')
@app.route("/")
def index():
        return render_template("index.html")
ALLOWED_EXTENTIONS= set(['png', 'jpg', 'jpeg'])
def allowed_files(filename):
        return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS

@app.route("/storImages", methods=['GET','POST'])
def storImages():
        dirnames = join(dirname(realpath(__file__)), 'static\\upload')
        UPLOAD_FOLDER = dirnames
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
        if 'file[]'not in request.files:
            resp = jsonify({'message': 'no file was uploaded'})
            resp.status_code = 400
            return resp
        files = request.files.getlist('file[]')
        errors = {}
        sucess = False
        for file in files:
            if file and allowed_files(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(file)
                succes = True
            else:
                errors[file.filename] = 'files is not allowed'
        if sucess and errors:
            errors['message'] = 'File(s) is uploaded ;)'
            resp = jsonify(errors)
            resp.status_code = 200
        return predict(file)
if __name__ == "__main__":
    app.run(debug=True)