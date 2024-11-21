import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, app, jsonify, url_for, render_template

# Initialize Flask app
app = Flask(__name__)

# Load the saved pickle file
model = pickle.load(open('lgbm_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_demand', methods=['POST'])
def predict_demand():
    try:
        # Extract form inputs
        features = [
            float(request.form.get('zone')),
            float(request.form.get('year')),
            float(request.form.get('month')),
            float(request.form.get('date')),
            float(request.form.get('hour')),
            float(request.form.get('farePerMile')),
            float(request.form.get('avgFlowSpeed_mph')),
            float(request.form.get('weather_category')),
            float(request.form.get('n_minus_1_hour_trips')),
            float(request.form.get('n_minus_2_hour_trips')),
            float(request.form.get('n_minus_3_hour_trips'))
        ]

        # Prepare feature array
        features_array = np.array([features])

        # Make prediction
        prediction = model.predict(features_array)[0]

        # Render template with prediction
        return render_template('home.html', prediction=round(prediction, 2))

    except Exception as e:
        # Render template with error
        return render_template('home.html', error=str(e))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
