import numpy as np
import pandas as pd
from flask_cors import  cross_origin
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@cross_origin()
@app.route('/')
def home():
    return render_template('index.html')
@cross_origin()
@app.route('/predict',methods=['POST'])
def predict():
    Pregnancies = float(request.form['Pregnancies'])
    Glucose = float(request.form['Glucose'])
    BloodPressure = float(request.form['BloodPressure'])
    SkinThickness = float(request.form['SkinThickness'])
    Insulin = float(request.form['Insulin'])
    BMI = float(request.form['BMI'])
    DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
    Age = float(request.form['Age'])

    filename = 'modelForPrediction.sav'
    loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
    scalar = pickle.load(open("sandardScalar.sav", 'rb'))
    # predictions using the loaded model file
    prediction = loaded_model.predict(scalar.transform(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]))
    if prediction ==[1]:
            prediction = "diabetes"

    else:
            prediction = "Normal"

    # showing the prediction results in a UI
    if  prediction =="diabetes":

        return render_template('diabetes.html', prediction=prediction)
    else:
        return render_template('Normal.html',prediction=prediction)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
	#app.run(debug=True)