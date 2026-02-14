"""
Streamlit UI for Loan Default Prediction

Run with: streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
from predict import LoanDefaultPredictor

# Page configuration
st.set_page_config(
    page_title="Loan Default Prediction",
    page_icon="💰",
    layout="wide"
)

# Title
st.title("💰 Loan Default Prediction System")
st.markdown("---")

# Initialize predictor (cached to load only once)
@st.cache_resource
def load_predictor():
    """Load the prediction model"""
    try:
        return LoanDefaultPredictor()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("Please make sure you have run the notebook and saved the model first.")
        return None

predictor = load_predictor()

if predictor is None:
    st.stop()

# Sidebar with instructions
with st.sidebar:
    st.header("📋 Instructions")
    st.markdown("""
    Fill in the customer information below and click **Predict** to get the loan default risk assessment.
    
    ### Feature Codes:
    - **Checking Status**: A11 (<0), A12 (0-200), A13 (>=200), A14 (no account)
    - **Credit History**: A30 (all paid), A31 (paid delay), A32 (no credits), A33 (critical), A34 (other)
    - **Purpose**: A40 (car new), A41 (car used), A49 (other), etc.
    - **Savings**: A61 (<100), A62 (100-500), A63 (500-1000), A64 (>=1000), A65 (unknown)
    - **Employment**: A71 (unemployed), A72 (<1yr), A73 (1-4yr), A74 (4-7yr), A75 (>=7yr)
    - **Housing**: A151 (rent), A152 (own), A153 (free)
    - **Job**: A171 (unskilled), A172 (unskilled resident), A173 (skilled), A174 (management)
    - **Telephone**: A191 (yes), A192 (no)
    - **Foreign Worker**: A201 (yes), A202 (no)
    """)

# Main form
st.header("📝 Customer Information")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Information")
    checking_status = st.selectbox("Checking Status", ["A11", "A12", "A13", "A14"], index=1)
    duration = st.number_input("Loan Duration (months)", min_value=1, max_value=100, value=24)
    credit_history = st.selectbox("Credit History", ["A30", "A31", "A32", "A33", "A34"], index=2)
    purpose = st.selectbox("Loan Purpose", ["A40", "A41", "A42", "A43", "A44", "A45", "A46", "A48", "A49"], index=0)
    credit_amount = st.number_input("Credit Amount", min_value=0.0, value=5000.0, step=100.0)
    savings_status = st.selectbox("Savings Status", ["A61", "A62", "A63", "A64", "A65"], index=0)
    employment = st.selectbox("Employment", ["A71", "A72", "A73", "A74", "A75"], index=2)
    installment_commitment = st.number_input("Installment Commitment (%)", min_value=1, max_value=4, value=4)
    personal_status = st.selectbox("Personal Status", ["A91", "A92", "A93", "A94", "A95"], index=2)
    other_parties = st.selectbox("Other Parties", ["A101", "A102"], index=0)

with col2:
    st.subheader("Additional Information")
    residence_since = st.number_input("Years at Residence", min_value=1, max_value=4, value=2)
    property_magnitude = st.selectbox("Property Magnitude", ["A121", "A122", "A123", "A124"], index=0)
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    other_payment_plans = st.selectbox("Other Payment Plans", ["A141", "A142", "A143"], index=0)
    housing = st.selectbox("Housing", ["A151", "A152", "A153"], index=1)
    existing_credits = st.number_input("Existing Credits", min_value=0, max_value=4, value=1)
    job = st.selectbox("Job Type", ["A171", "A172", "A173", "A174"], index=2)
    num_dependents = st.number_input("Number of Dependents", min_value=0, max_value=2, value=0)
    own_telephone = st.selectbox("Own Telephone", ["A191", "A192"], index=0)
    foreign_worker = st.selectbox("Foreign Worker", ["A201", "A202"], index=0)

st.markdown("---")

# Prediction button
if st.button("🔮 Predict Loan Default Risk", type="primary", use_container_width=True):
    # Collect all inputs
    customer_data = {
        'checking_status': checking_status,
        'duration': int(duration),
        'credit_history': credit_history,
        'purpose': purpose,
        'credit_amount': float(credit_amount),
        'savings_status': savings_status,
        'employment': employment,
        'installment_commitment': int(installment_commitment),
        'personal_status': personal_status,
        'other_parties': other_parties,
        'residence_since': int(residence_since),
        'property_magnitude': property_magnitude,
        'age': int(age),
        'other_payment_plans': other_payment_plans,
        'housing': housing,
        'existing_credits': int(existing_credits),
        'job': job,
        'num_dependents': int(num_dependents),
        'own_telephone': own_telephone,
        'foreign_worker': foreign_worker
    }
    
    # Make prediction
    try:
        result = predictor.predict(customer_data)
        
        # Display results
        st.markdown("---")
        st.header("📊 Prediction Results")
        
        # Create columns for results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Prediction", result['prediction'])
            st.caption("0 = No Default, 1 = Default")
        
        with col2:
            st.metric("Default Probability", f"{result['probability']:.2%}")
        
        with col3:
            st.metric("Risk Level", result['risk_level'])
        
        # Recommendation
        st.markdown("---")
        if result['prediction'] == 1:
            st.error(f"⚠️ **Recommendation: {result['recommendation']}**")
            st.warning("This customer has a high risk of defaulting on the loan.")
        else:
            st.success(f"✅ **Recommendation: {result['recommendation']}**")
            st.info("This customer has a low risk of defaulting on the loan.")
        
        # Show input data
        with st.expander("📋 View Input Data"):
            st.json(customer_data)
    
    except Exception as e:
        st.error(f"Error making prediction: {e}")

# Footer
st.markdown("---")
st.markdown("**Note**: This is a machine learning model prediction. Always verify with additional risk assessment methods.")
