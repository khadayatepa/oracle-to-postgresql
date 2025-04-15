import streamlit as st
import openai
import os

# Title
st.set_page_config(page_title="Oracle to PostgreSQL Converter")
st.markdown("<h1 style='text-align: center; color: green;'>Developed Oracle to postgresql code conversion by Prashant K</h1>", unsafe_allow_html=True)

# Get OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Oracle PL/SQL Code")
    oracle_code = st.text_area("Paste your Oracle code here:", height=400, key="oracle_code_input")

with col2:
    st.subheader("Converted PostgreSQL Code")
    pgsql_output = st.empty()

# Convert button
if st.button("Convert to PostgreSQL"):
    if not oracle_code.strip():
        st.warning("Please paste Oracle PL/SQL code.")
    else:
        try:
            with st.spinner("Converting..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert in PL/SQL to PostgreSQL code migration."},
                        {"role": "user", "content": f"Convert the following Oracle PL/SQL code to PostgreSQL:\n\n{oracle_code}"}
                    ]
                )
                pgsql_code = response['choices'][0]['message']['content']
                pgsql_output.text_area("PostgreSQL Code Output", pgsql_code, height=400)
        except Exception as e:
            st.error(f"Error during conversion: {e}")
