from flask import Flask, render_template, url_for, request, redirect, flash, send_file, jsonify
from werkzeug.utils import secure_filename, send_from_directory
from os import path
from cancer_model import can
from form_data import ValuePredictor, ValuePredictor1
from pneumonia_model import pneumo
from malaria import malar


ALLOWED_EXTENSIONS = set(['tif', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['upload'] = 'upload'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
            if file.filename == '':
                print('no file selected')
                flash('No selected file')
                return redirect(request.url)
            else:
                full_name = path.join('upload', file.filename)
                secure_filename(file.filename)
                file.save(full_name)
                value = can(full_name)
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
            if file.filename == '':
                print('no file selected')
                flash('No selected file')
                return redirect(request.url)
            else:
                full_name = path.join('upload', file.filename)
                secure_filename(file.filename)
                file.save(full_name)
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
            if file.filename == '':
                print('no file selected')
                flash('No selected file')
                return redirect(request.url)
            else:
                full_name = path.join('upload', file.filename)
                secure_filename(file.filename)
                file.save(full_name)
                value = malar(full_name)
                print(value)
                return render_template('malaria.html', messages = value)
            
        return redirect(url_for('malaria'))
    else:
        return render_template('malaria.html')

@app.route('/pred_model', methods=["POST"])
def pred_model():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        # print("data",to_predict_list)
        result = ValuePredictor(to_predict_list, len(to_predict_list))
        if (len(to_predict_list) == 7):
            if(int(result) == 1):
                return render_template('heart.html', prediction_text="Sorry your chances of getting the disease. Please consult the doctor immediately")
            else:
                return render_template('heart.html', prediction_text="No need to fear. You have no dangerous symptoms of the disease")
        elif(len(to_predict_list)==8):
            if(int(result) == 1):
                return render_template('diabetes.html', prediction_text="Sorry your chances of getting the disease. Please consult the doctor immediately")
            else:
                return render_template('diabetes.html', prediction_text="No need to fear. You have no dangerous symptoms of the disease")
        elif (len(to_predict_list) == 9):
            if(int(result) == 1):
                return render_template('liver.html', prediction_text="Sorry your chances of getting the disease. Please consult the doctor immediately")
            else:
                return render_template('liver.html', prediction_text="No need to fear. You have no dangerous symptoms of the disease")
    return redirect(request.url)

@app.route('/liver_model', methods=["POST"])
def liver_model():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        result = ValuePredictor1(to_predict_list, len(to_predict_list))
        print(int(result))
        if (len(to_predict_list) == 9):
            if(int(result) == 1):
                return render_template('liver.html', prediction_text="Sorry your chances of getting the disease. Please consult the doctor immediately")
            else:
                return render_template('liver.html', prediction_text="No need to fear. You have no dangerous symptoms of the disease")
    return redirect(request.url)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='upload', filename=filename)

@app.route('/test-images', methods=['GET', 'POST'])
def test_images():
    path = 'upload/upload.zip'
    return send_file(path, as_attachment=True)

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
    # return request.environ.get('HTTP_X_REAL_IP', request.remote_addr) 
    # return request.remote_addr

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', debug=True)