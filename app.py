#Importing the required libraries
from flask import Flask, redirect, url_for, request, render_template
from keras.models import load_model
import tensorflow as tf
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename
import os

# Define a flask app
app = Flask(__name__)

def model_predict(img_path, model):
    img = tf.keras.utils.load_img(img_path, target_size=(100, 100))
    # Preprocessing the image
    x = tf.keras.utils.img_to_array(img)/255.0
    x = x.reshape(1,100,100,3)
    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

cache = {}
@app.route('/modelSelection',methods=['POST'])
def select():
    f=request.form['models'];
    print(f)
    if f=='C':
        MODEL_PATH = 'F:\\Pneumonia-Detection\\Models\\CNN_model.h5'
        print('Loaded CNN Model')
    elif f=='V16':
        MODEL_PATH = 'F:\\Pneumonia-Detection\\Models\\VGG16_model.h5'
        print('Loaded VGG16 Model')
    elif f=='V19':
        MODEL_PATH = 'F:\\Pneumonia-Detection\\Models\\VGG19_model.h5'
        print('Loaded VGG19 Model')
    elif f=='R':
        MODEL_PATH = 'F:\\Pneumonia-Detection\\Models\\ResNet50_model.h5'
        print('Loaded ResNet Model')
        

    model= load_model(MODEL_PATH)
    #model._make_predict_function()
    cache['model'] = model

    return redirect('/')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'F:\\Pneumonia-Detection\\uploads', secure_filename(f.filename))
        f.save(file_path)
        print(cache)
        # Make prediction
        preds = model_predict(file_path,cache['model'])
        
        os.remove(file_path)#removes file from the server after prediction has been returned
        
        cache['confidence_0'] = preds[0][0]
        cache['confidence_1'] = preds[0][1]
        # Process your result for human
        pred_class = preds        
        if pred_class[0][0]>pred_class[0][1]:
            result="Person is safe"
        else:
            result="Person is affected with Pneumonia"
        print(result)
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)



