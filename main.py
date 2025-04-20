import streamlit as st

st.title("Easy Finance: Credit Risk Modeling")

col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with col2:
    income = st.number_input("Income", min_value=0, step=1000)
with col3:
    loan_amount = st.number_input("Loan Amount", min_value=1000, step=1000)
with col4:
    loan_tenure = st.number_input("Loan Tenure (Months)", min_value=6, step=6)

col5, col6, col7, col8 = st.columns(4)
with col5:
    dpd = st.number_input("Days Past Due (DPD)", min_value=0, step=1)
with col6:
    credit_utilization = st.slider("Credit Utilization Ratio", 0.0, 1.0, 0.5)
with col7:
    residence_type = st.selectbox("Residence Type", ["Owned", "Rental", "Mortgage"])
with col8:
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])

col9, _, _, _ = st.columns(4)
with col9:
    loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])

if st.button("Submit"):
    st.write("## Submitted Details")
    st.json({
        "Age": age,
        "Income": income,
        "Loan Amount": loan_amount,
        "Loan Tenure (Months)": loan_tenure,
        "Days Past Due (DPD)": dpd,
        "Credit Utilization Ratio": credit_utilization,
        "Residence Type": residence_type,
        "Loan Purpose": loan_purpose,
        "Loan Type": loan_type
    })
