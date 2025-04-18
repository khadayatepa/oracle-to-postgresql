import streamlit as st
from openai import OpenAI

# Page Configuration
st.set_page_config(page_title="Oracle to PostgreSQL Converter")
st.markdown("<h1 style='text-align: center; color: green;'>Developed Oracle to postgresql code conversion by Prashant K</h1>", unsafe_allow_html=True)

# Sidebar for API Key Input
st.sidebar.header("🔐 API Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Check if API Key is entered
if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to proceed.")
else:
    try:
        client = OpenAI(api_key=api_key)

        # Two-column layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Oracle PL/SQL Code")
            oracle_code = st.text_area("Paste your Oracle PL/SQL code here:", height=400)

        with col2:
            st.subheader("PostgreSQL Output")
            pgsql_output = st.empty()

        if st.button("Convert to PostgreSQL"):
            if not oracle_code.strip():
                st.warning("Please paste Oracle PL/SQL code to convert.")
            else:
                with st.spinner("Converting using OpenAI..."):
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are an expert in Oracle PL/SQL to PostgreSQL code migration."},
                                {"role": "user", "content": f"Convert the following Oracle PL/SQL code to PostgreSQL:\n\n{oracle_code}"}
                            ]
                        )
                        pgsql_code = response.choices[0].message.content
                        pgsql_output.text_area("PostgreSQL Code Output", pgsql_code, height=400)
                    except Exception as e:
                        st.error(f"Error during conversion: {e}")
    except Exception as auth_error:
        st.error(f"Authentication failed. Please check your API key.\nDetails: {auth_error}")
