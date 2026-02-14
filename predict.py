"""
Loan Default Prediction Script

This script loads a trained model and makes predictions on new customer data.
Usage: python predict.py
"""

import pickle
import pandas as pd
import numpy as np
import os

class LoanDefaultPredictor:
    """Loan Default Prediction Model"""
    
    def __init__(self, model_dir='models'):
        """Load model and preprocessing objects"""
        self.model_dir = model_dir
        self.model = None
        self.scaler = None
        self.label_encoders = None
        self.metadata = None
        self._load_model()
    
    def _load_model(self):
        """Load all saved model artifacts"""
        try:
            # Load model
            with open(os.path.join(self.model_dir, 'model.pkl'), 'rb') as f:
                self.model = pickle.load(f)
            
            # Load scaler
            with open(os.path.join(self.model_dir, 'scaler.pkl'), 'rb') as f:
                self.scaler = pickle.load(f)
            
            # Load label encoders
            with open(os.path.join(self.model_dir, 'label_encoders.pkl'), 'rb') as f:
                self.label_encoders = pickle.load(f)
            
            # Load metadata
            with open(os.path.join(self.model_dir, 'metadata.pkl'), 'rb') as f:
                self.metadata = pickle.load(f)
            
            print("✓ Model and preprocessing objects loaded successfully!")
            
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Model files not found. Please run the notebook to train and save the model first. Error: {e}")
    
    def predict(self, customer_data):
        """
        Predict loan default for a customer
        
        Parameters:
        customer_data: dict with customer features
        
        Returns:
        dict: prediction (0 or 1), probability, and recommendation
        """
        # Convert to DataFrame
        customer_df = pd.DataFrame([customer_data])
        
        # Encode categorical variables
        categorical = self.metadata['categorical_features']
        for col in categorical:
            if col in customer_df.columns:
                if col in self.label_encoders:
                    customer_df[col] = self.label_encoders[col].transform(customer_df[col].astype(str))
        
        # Ensure all original columns are present
        feature_columns = self.metadata['feature_columns']
        original_cols = [col for col in feature_columns if col not in ['credit_per_month', 'age_group']]
        
        for col in original_cols:
            if col not in customer_df.columns:
                customer_df[col] = 0
        
        customer_df = customer_df[original_cols]
        
        # Feature engineering
        if 'credit_amount' in customer_df.columns and 'duration' in customer_df.columns:
            customer_df['credit_per_month'] = customer_df['credit_amount'] / (customer_df['duration'] + 1)
        
        if 'age' in customer_df.columns:
            customer_df['age_group'] = pd.cut(customer_df['age'], bins=[0, 30, 50, 100], labels=[0, 1, 2]).astype(float)
        
        # Ensure all engineered features are present
        for col in feature_columns:
            if col not in customer_df.columns:
                customer_df[col] = 0
        
        customer_df = customer_df[feature_columns]
        
        # Scale features
        customer_scaled = self.scaler.transform(customer_df)
        
        # Predict
        prediction = self.model.predict(customer_scaled)[0]
        probability = self.model.predict_proba(customer_scaled)[0][1]
        
        return {
            'prediction': int(prediction),
            'probability': float(probability),
            'risk_level': 'HIGH RISK' if prediction == 1 else 'LOW RISK',
            'recommendation': 'REJECT LOAN' if prediction == 1 else 'APPROVE LOAN'
        }


def main():
    """Example usage"""
    print("="*70)
    print("Loan Default Prediction Script")
    print("="*70)
    
    # Initialize predictor
    predictor = LoanDefaultPredictor()
    
    # Example customer data
    example_customer = {
        'checking_status': 'A11',
        'duration': 24,
        'credit_history': 'A32',
        'purpose': 'A40',
        'credit_amount': 5000,
        'savings_status': 'A61',
        'employment': 'A73',
        'installment_commitment': 4,
        'personal_status': 'A93',
        'other_parties': 'A101',
        'residence_since': 2,
        'property_magnitude': 'A121',
        'age': 35,
        'other_payment_plans': 'A141',
        'housing': 'A152',
        'existing_credits': 1,
        'job': 'A173',
        'num_dependents': 0,
        'own_telephone': 'A191',
        'foreign_worker': 'A201'
    }
    
    print("\n📥 Input Customer Data:")
    for key, value in example_customer.items():
        print(f"  {key:25s}: {value}")
    
    # Make prediction
    result = predictor.predict(example_customer)
    
    print("\n📤 Prediction Results:")
    print(f"  Prediction: {result['prediction']} ({result['risk_level']})")
    print(f"  Default Probability: {result['probability']:.2%}")
    print(f"  Recommendation: {result['recommendation']}")
    
    print("\n" + "="*70)
    print("Prediction completed successfully!")
    print("="*70)
    
    return result


if __name__ == "__main__":
    main()
