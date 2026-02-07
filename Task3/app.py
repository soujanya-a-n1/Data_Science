from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route('/')
def home():
    return '''
    <h2>House Price Prediction</h2>
    <form action="/predict" method="post">
        Area: <input type="number" name="area"><br><br>
        Bedrooms: <input type="number" name="bedrooms"><br><br>
        Bathrooms: <input type="number" name="bathrooms"><br><br>
        <input type="submit" value="Predict Price">
    </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])

    prediction = model.predict([[area, bedrooms, bathrooms]])

    return f"<h3>Predicted House Price: {prediction[0]:,.2f}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
