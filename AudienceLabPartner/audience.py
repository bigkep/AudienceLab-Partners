import streamlit as st
import math

# Set page title and favicon
st.set_page_config(page_title="Metrics Calculator", page_icon=":bar_chart:")

# Define function to calculate metrics
def calculate_metrics(your_plan, avg_plan_ref, ref_payout_percent, sales_conversion_rate, response_rate):
    payout = avg_plan_ref * (ref_payout_percent / 100)
    referrals_needed_to_be = your_plan / payout
    conversions_needed = referrals_needed_to_be / sales_conversion_rate
    touch_points_needed = math.ceil(conversions_needed / response_rate)
    
    return payout, referrals_needed_to_be, conversions_needed, touch_points_needed

# Define main function
def main():
    # Add title and header
    st.markdown("<h1 style='color:navy'>Metrics Calculator</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:navy'>This is the Calculated metrics for your AudienceLab Partners</h2>", unsafe_allow_html=True)
    
    # Add sidebar for input fields
    with st.sidebar:
        st.markdown("### Input Fields")
        your_plan = st.number_input("Plan", value=2500.00)
        avg_plan_ref = st.number_input("Avg Plan Ref", value=2500.00)
        ref_payout_percent = st.number_input("Ref Payout %", value=10.00)
        sales_conversion_rate = st.number_input("Sales Conversion Rate", value=0.40)
        response_rate = st.number_input("Response Rate", value=0.60)
    
    # Calculate metrics
    payout, referrals_needed_to_be, conversations_needed, touch_points_needed = calculate_metrics(your_plan, avg_plan_ref, ref_payout_percent, sales_conversion_rate, response_rate)
    
    # Display metrics
    st.markdown("<h2 style='color:navy'>Metrics</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:navy'>Payout: <strong>{payout:.2f}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:navy'>Referrals needed to be: <strong>{referrals_needed_to_be:.2f}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:navy'>Conversations Needed: <strong>{conversations_needed:.2f}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:navy'>Touch Points Needed: <strong>{touch_points_needed}</strong></p>", unsafe_allow_html=True)
    
    # Add success message
    st.success("Metrics calculated successfully!")
    
if __name__ == "__main__":
    # Set background color
    st.markdown("<style>body {background-color: lightSkyBlue;}</style>", unsafe_allow_html=True)
    
    main()
    