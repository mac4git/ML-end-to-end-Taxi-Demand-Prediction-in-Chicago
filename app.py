import pickle
import numpy as np
import pandas as pd
import lightgbm as lgb

from flask import Flask, request, app, jsonify, url_for, render_template

# Initialize Flask app
app = Flask(__name__)

# Load the saved pickle file
model = pickle.load(open('lgbm_model.pkl','rb'))

# Path to the CSV file containing the remaining features
CSV_FILE_PATH = 'final_df.csv'
# Load the CSV data into a DataFrame
data_df = pd.read_csv(CSV_FILE_PATH)

@app.route('/')
def home():
    return render_template('home3.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Log the received JSON
        print("Received JSON:", request.json)

        # Get the 'features' dictionary from the request
        features = request.json.get('features')
        if features is None:
            return jsonify({"error": "Missing 'features' key in the request JSON"}), 400

        # Validate 'features' is a dictionary
        if not isinstance(features, dict):
            return jsonify({"error": "'features' must be a dictionary"}), 400

        # Log the extracted features
        print("Extracted features:", features)

        # Check for missing values
        if any(value is None for value in features.values()):
            return jsonify({"error": "All fields are required. Please fill out the form completely."}), 400

        # Convert features to a NumPy array
        new_data = np.array(list(features.values())).reshape(1, -1)

        # Make prediction
        output = model.predict(new_data)

        # Return the prediction
        return jsonify({"prediction": float(output[0])})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/predict_demand', methods=['POST'])
def predict_demand():
    try:
        fields = [
            'zone', 'year', 'month', 'date', 'hour', 
            'farePerMile', 'avgFlowSpeed_mph', 'weather_category', 
            'n_minus_1_hour_trips', 'n_minus_2_hour_trips', 'n_minus_3_hour_trips'
        ]

        # Extract all fields from the form
        form_data = {field: request.form.get(field) for field in fields}
        print("Received Form Data:", form_data)  # Debugging log

        # Check for missing or empty fields
        missing_fields = [field for field, value in form_data.items() if value is None or value.strip() == ""]
        if missing_fields:
            return render_template(
                'home3.html',
                error=f"Missing values for fields: {', '.join(missing_fields)}"
            )

        # Convert all fields to float
        features = [float(form_data[field]) for field in fields]

        # Use features for prediction (example)
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]

        return render_template('home3.html', prediction=round(prediction, 2))

    except Exception as e:
        return render_template('home3.html', error=f"Error: {str(e)}")



# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
