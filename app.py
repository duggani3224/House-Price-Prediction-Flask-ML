from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained objects
model = joblib.load('house_model.pkl')
scaler = joblib.load('scaler.pkl')
features = joblib.load('features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_df = pd.DataFrame([data])

        # Align columns
        final_input = input_df.reindex(columns=features, fill_value=0)

        # Scale & predict
        input_scaled = scaler.transform(final_input)
        log_prediction = model.predict(input_scaled)

        # Convert log price → actual price
        actual_price = np.expm1(log_prediction)[0]

        return jsonify({'predicted_price': f"${actual_price:,.2f}"})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
