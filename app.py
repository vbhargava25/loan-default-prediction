"""
FastAPI Application for Loan Default Prediction

Run with: uvicorn app:app --reload
API will be available at: http://localhost:8000
API docs at: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any
from predict import LoanDefaultPredictor
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Loan Default Prediction API",
    description="API for predicting loan default risk using machine learning",
    version="1.0.0"
)

# Initialize predictor (loads model once at startup)
predictor = LoanDefaultPredictor()


class CustomerData(BaseModel):
    """Customer data schema for prediction"""
    checking_status: str = Field(..., description="Checking account status (e.g., 'A11', 'A12')")
    duration: int = Field(..., description="Loan duration in months", ge=1, le=100)
    credit_history: str = Field(..., description="Credit history (e.g., 'A30', 'A32')")
    purpose: str = Field(..., description="Loan purpose (e.g., 'A40', 'A49')")
    credit_amount: float = Field(..., description="Credit amount", ge=0)
    savings_status: str = Field(..., description="Savings status (e.g., 'A61', 'A65')")
    employment: str = Field(..., description="Employment status (e.g., 'A71', 'A73')")
    installment_commitment: int = Field(..., description="Installment commitment percentage", ge=1, le=4)
    personal_status: str = Field(..., description="Personal status (e.g., 'A93', 'A94')")
    other_parties: str = Field(..., description="Other parties (e.g., 'A101')")
    residence_since: int = Field(..., description="Years at current residence", ge=1, le=4)
    property_magnitude: str = Field(..., description="Property magnitude (e.g., 'A121', 'A122')")
    age: int = Field(..., description="Age in years", ge=18, le=100)
    other_payment_plans: str = Field(..., description="Other payment plans (e.g., 'A141')")
    housing: str = Field(..., description="Housing status (e.g., 'A151', 'A152')")
    existing_credits: int = Field(..., description="Number of existing credits", ge=0, le=4)
    job: str = Field(..., description="Job type (e.g., 'A171', 'A173')")
    num_dependents: int = Field(..., description="Number of dependents", ge=0, le=2)
    own_telephone: str = Field(..., description="Own telephone (e.g., 'A191', 'A192')")
    foreign_worker: str = Field(..., description="Foreign worker (e.g., 'A201', 'A202')")
    
    class Config:
        schema_extra = {
            "example": {
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
            }
        }


class PredictionResponse(BaseModel):
    """Prediction response schema"""
    prediction: int = Field(..., description="Prediction: 0 = No Default, 1 = Default")
    probability: float = Field(..., description="Probability of default (0-1)")
    risk_level: str = Field(..., description="Risk level: LOW RISK or HIGH RISK")
    recommendation: str = Field(..., description="Recommendation: APPROVE LOAN or REJECT LOAN")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Loan Default Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "predict": "/predict",
            "docs": "/docs",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": predictor.model is not None
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict_loan_default(customer: CustomerData):
    """
    Predict loan default risk for a customer
    
    - **checking_status**: Checking account status
    - **duration**: Loan duration in months
    - **credit_history**: Credit history
    - **purpose**: Loan purpose
    - **credit_amount**: Credit amount
    - And other customer features...
    
    Returns prediction (0 or 1), probability, risk level, and recommendation
    """
    try:
        # Convert Pydantic model to dict
        customer_dict = customer.dict()
        
        # Make prediction
        result = predictor.predict(customer_dict)
        
        return PredictionResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.get("/model-info")
async def model_info():
    """Get information about the loaded model"""
    return {
        "model_name": predictor.metadata.get('model_name', 'Unknown'),
        "feature_count": len(predictor.metadata.get('feature_columns', [])),
        "categorical_features": len(predictor.metadata.get('categorical_features', [])),
        "numerical_features": len(predictor.metadata.get('numerical_features', []))
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
