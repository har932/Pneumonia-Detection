#Importing the required libraries
#from asyncore import file_dispatcher
from flask import Flask, redirect, url_for, request, render_template
import urllib.request
from flask import flash
from keras.models import load_model
import tensorflow as tf
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import os

pneumonia_model = load_model('F:/Pneumonia-Detection/Models/VGG16_model.h5')

UPLOAD_FOLDER = 'F:/Pneumonia-Detection/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/pneumonia')
def pneumonia():
    return render_template('pneumonia.html')

def model_predict(img_path, pneumonia_model):
    img = tf.keras.utils.load_img(img_path, target_size=(100, 100))
    # Preprocessing the image
    x = tf.keras.utils.img_to_array(img)/255.0
    x = x.reshape(1,100,100,3)
    preds = pneumonia_model.predict(x)
    return preds

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        file = request.files['file']
        if request.method == 'POST':
            f = request.files['file']
             # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
            basepath, 'F:/Pneumonia-Detection/static/uploads', secure_filename(f.filename))
            #file_path = secure_filename(f.filename)
            f.save(file_path)
        # Make prediction
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #f.save(filename)
            flash('Image successfully uploaded and displayed below')
            preds = model_predict(file_path,pneumonia_model)
            pred_class = preds
            if pred_class[0][0]>pred_class[0][1]:
                result=0
            else:
                result=1
            # pb.push_sms(pb.devices[0],str(phone), 'Hello {},\nYour COVID-19 test results are ready.\nRESULT: {}'.format(firstname,['POSITIVE','NEGATIVE'][pred]))
            return render_template('result.html', filename=filename, fn=firstname, ln=lastname, age=age, r=result, gender=gender)

        else:
            flash('Allowed image types are - png, jpg, jpeg')
            return redirect(request.url)

# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == '__main__':
    app.run(debug=True)

