# Loan Default Prediction - ML Project

Complete machine learning project for predicting loan default risk with deployment scripts.

## Project Structure

```
ML_PROJECT/
│
├── mlproject.ipynb          # Main Jupyter notebook with full ML pipeline
├── models/                  # Saved model artifacts (created after running notebook)
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   └── metadata.pkl
│
├── predict.py               # Standalone prediction script
├── app.py                   # FastAPI application
├── streamlit_app.py         # Streamlit UI
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the notebook:**
   - Open `mlproject.ipynb`
   - Run all cells to train the model
   - This will create the `models/` directory with saved artifacts

## Usage

### 1. Standalone Prediction Script

```bash
python predict.py
```

This will load the model and make a prediction on example data.

### 2. FastAPI Application

Start the API server:
```bash
uvicorn app:app --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

**Example API Request:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "checking_status": "A11",
    "duration": 24,
    "credit_history": "A32",
    "purpose": "A40",
    "credit_amount": 5000,
    "savings_status": "A61",
    "employment": "A73",
    "installment_commitment": 4,
    "personal_status": "A93",
    "other_parties": "A101",
    "residence_since": 2,
    "property_magnitude": "A121",
    "age": 35,
    "other_payment_plans": "A141",
    "housing": "A152",
    "existing_credits": 1,
    "job": "A173",
    "num_dependents": 0,
    "own_telephone": "A191",
    "foreign_worker": "A201"
  }'
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.25,
  "risk_level": "LOW RISK",
  "recommendation": "APPROVE LOAN"
}
```

### 3. Streamlit UI

Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

The UI will open in your browser at http://localhost:8501

## Features

- ✅ Complete ML pipeline (EDA, preprocessing, modeling, evaluation)
- ✅ Three models: Logistic Regression, Random Forest, Gradient Boosting
- ✅ Model selection and evaluation
- ✅ Standalone prediction script
- ✅ FastAPI REST API
- ✅ Streamlit web interface
- ✅ Production-ready code structure

## Model Performance

The best model (Random Forest) achieves:
- **Accuracy**: ~75%
- **F1-Score**: ~0.50
- **Precision**: ~64%
- **Recall**: ~42%

## Notes

- Make sure to run the notebook first to train and save the model
- All three deployment methods use the same saved model
- The model uses the German Credit Dataset from UCI
