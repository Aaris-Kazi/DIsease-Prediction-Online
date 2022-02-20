from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from tomlkit import value
from werkzeug.utils import secure_filename
import os
from cancer_model import can
from pneumonia_model import pneumo
from malaria import malar

ALLOWED_EXTENSIONS = set(['tif', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['upload'] = 'upload'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# @app.route('/', methods = ['POST', 'GET'])
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cancer')
def cancer():
    return render_template('cancer.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/kidney')
def kidney():
    return render_template('kidney.html')

@app.route('/liver')
def liver():
    return render_template('liver.html')

@app.route('/malaria')
def mala():
    return render_template('malaria.html')

@app.route('/pneumonia')
def pneu():
    return render_template('pneumonia.html')

@app.route('/cancer_model', methods = ['POST', 'GET'])
def cancer_model():
    if request.method == 'POST':
        if request.files:
            file = request.files["imagefile"]
            # print(file)
            if file.filename == '':
                print('no file selected')
                flash('No selected file')
                return redirect(request.url)
            else:
                full_name = os.path.join('upload', file.filename)
                file.save(full_name)
                # print(file.filename)
                value = can(file.filename)
                print(value)
                return render_template('cancer.html', messages = value)
            
        return redirect(url_for('cancer'))
    else:
        return render_template('cancer.html')

@app.route('/pneumonia_model', methods = ['POST', 'GET'])
def pneumonia_model():
    if request.method == 'POST':
        if request.files:
            file = request.files["imagefile"]
            # print(file)
            if file.filename == '':
                print('no file selected')
                flash('No selected file')
                return redirect(request.url)
            else:
                full_name = os.path.join('upload', file.filename)
                file.save(full_name)
                # print(file.filename)
                value = pneumo(full_name)
                print(value)
                return render_template('pneumonia.html', messages = value)
            
        return redirect(url_for('pneumonia'))
    else:
        return render_template('pneumonia.html')

@app.route('/malaria_model', methods = ['POST', 'GET'])
def malaria_model():
    if request.method == 'POST':
        if request.files:
            file = request.files["imagefile"]
            # print(file)
            if file.filename == '':
                print('no file selected')
                flash('No selected file')
                return redirect(request.url)
            else:
                full_name = os.path.join('upload', file.filename)
                file.save(full_name)
                # print(file.filename)
                # value = mala(full_name)
                value = malar(full_name)
                print(value)
                return render_template('malaria.html', messages = value)
            
        return redirect(url_for('malaria'))
    else:
        return render_template('malaria.html')


if __name__ == '__main__':
    app.run(debug=True)