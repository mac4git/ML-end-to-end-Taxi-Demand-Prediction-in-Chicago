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

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract JSON data from the request
        data = request.get_json()
        print(data)  # Debugging: Ensure data is received correctly

        # Example: Extracting features
        features = data.get("features")  # Replace "features" with the actual key
        

        # Validate that features is a list of numbers
        if not isinstance(features, list):
            return jsonify({"error": "Invalid input format. 'features' must be a list of numbers."}), 400

        try:
            features = [float(f) for f in features]
        except ValueError:
            return jsonify({"error": "All features must be numbers."}), 400


        if features is None:
            return jsonify({"error": "No features provided"}), 400

        # Convert to NumPy array and reshape
        import numpy as np
        features = np.array(features).reshape(1, -1)  # Assuming it's a single sample
        print(features)  # Debugging: Check the reshaped array

        # Make a prediction
        prediction = model.predict(features)
        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
