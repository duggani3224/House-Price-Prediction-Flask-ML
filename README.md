# House-Price-Prediction-Flask-ML
House Price Prediction web application built using Flask, Machine Learning, and Tailwind CSS. Predicts property prices based on location, area, bedrooms, and other features using a trained regression model.

🏠 AI-Powered House Price Predictor
An end-to-end machine learning project that predicts residential property values using advanced regression techniques. This project features a robust ML pipeline and a modern, responsive web interface for instant valuations.

🚀 Features
Predictive Engine: Uses a Ridge Regression model trained on historical real estate data.

Feature Engineering: Implements advanced preprocessing including Box-Cox transformations, iterative imputation, and feature scaling.

Modern UI: A sleek, responsive dashboard built with Tailwind CSS and Font Awesome.

REST API: A Flask-based backend that serves model predictions in real-time.

🧠 Machine Learning Pipeline
The model was developed using a comprehensive data science workflow:

Data Preprocessing: Handled missing values using IterativeImputer with a Random Forest Regressor and addressed skewness in numerical features.

Feature Selection: Utilized Lasso Regression to identify and select the most impactful property features.

Model Selection: Evaluated multiple algorithms including Ridge, Lasso, ElasticNet, SVM, XGBoost, and CatBoost.

Final Model: A Ridge Regression model was selected for its balance of performance and generalization.

🛠️ Technical Stack
Frontend: HTML5, Tailwind CSS, JavaScript (Async/Fetch API).

Backend: Python, Flask.

Data Science: Scikit-learn, Pandas, NumPy, XGBoost, CatBoost.

Deployment Tools: Joblib for model serialization.

💻 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
Install dependencies:

Bash
pip install -r requirements.txt
Run the Flask application:

Bash
python app.py
Access the UI: Open http://127.0.0.1:5000 in your browser.

📊 Dataset Information
The project uses a comprehensive dataset containing various residential property attributes, including:

Property Characteristics: Zoning, Lot Area, Building Type, and Overall Quality.

Physical Dimensions: Square footage of different areas (Living Area, Basement, Garage).

Amenities: Fireplaces, Pool area, and Year Built/Remodeled.

📝 License
Distributed under the MIT License. See LICENSE for more information.
