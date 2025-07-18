import streamlit as st
from utils.llm import generate_docstring
from config.prompts import get_prompt

st.set_page_config(page_title="Docstring Generator", layout="wide")
st.title("LLM Python Docstring Generator")

left, right = st.columns(2)

with left:
    st.header("🔧 Original Code")
    input_code = st.text_area(
            "Paste your Python function here:",
            height=400,
            label_visibility="collapsed"
            )
    generate = st.button("Generate Docstring")

with right:
    st.header("📄 With Docstring")
    if generate and input_code.strip():
        prompt = get_prompt(input_code)
        print(prompt)
        with st.spinner("Generating docstring using phi3..."):
            output = generate_docstring(prompt)
        st.code(output, language="python")
    else:
        st.info("Docstring will appear here after generation.")
