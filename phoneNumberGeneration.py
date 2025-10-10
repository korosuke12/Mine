import streamlit as st
import pandas as pd
import random


def generate_phone_number(country_code, number_length, prefix):
    remaining_length = number_length - len(prefix)
    number = ''.join(random.choices('0123456789', k=remaining_length))
    return f"{country_code} {prefix}{number}"

st.title("📞 Phone Number Generator")
st.markdown("Generate fake phone numbers with custom options.")

st.sidebar.header("⚙️ Settings")

# User inputs
num_numbers = st.sidebar.slider("How many phone numbers to generate?", 1, 1000, 10)

country_code = st.sidebar.selectbox(
    "Select Country Code",
    options=["+1 (USA)", "+44 (UK)", "+91 (India)", "+61 (Australia)", "+81 (Japan)", "+49 (Germany)"],
)

code_map = {
    "+1 (USA)": "+1",
    "+44 (UK)": "+44",
    "+91 (India)": "+91",
    "+61 (Australia)": "+61",
    "+81 (Japan)": "+81",
    "+49 (Germany)": "+49"
}

prefix = st.sidebar.text_input("Phone number prefix (optional)", value="")
number_length = st.sidebar.slider("Total number length (excluding country code)", 6, 15, 10)


if st.sidebar.button("Generate Phone Numbers"):
    selected_code = code_map[country_code]

    
    numbers = [generate_phone_number(selected_code, number_length, prefix) for _ in range(num_numbers)]
    
    df = pd.DataFrame(numbers, columns=["Phone Number"])

    st.subheader("📋 Generated Phone Numbers")
    st.dataframe(df)

    # Download as CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name='phone_numbers.csv',
        mime='text/csv',
    )
else:
    st.info("👈 Use the sidebar to customize and generate phone numbers.")
