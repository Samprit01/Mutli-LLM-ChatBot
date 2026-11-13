import streamlit as st
from utility import openai_call, ollama_call, gemini_call

st.set_page_config(page_title="LLM Dashboard", layout="wide")

left_col, right_col = st.columns([3, 1])

with right_col:
    st.header("Settings")
    
    model_choice = st.radio(
        "Select your LLM:",
        ["OpenAI (GPT-4o)", "Ollama (Gemma4)", "Google Gemini"]
    )

with left_col:
    st.title("DASHBOARD FOR LLM CHOICE")
    
    question = st.text_area("Enter your question:")
    
    if st.button("Submit", type="primary"):
        if not question:
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating response..."):
                try:
                    if model_choice == "OpenAI (GPT-4o)":
                        answer, duration = openai_call(question)
                        
                    elif model_choice == "Ollama (Gemma4)":
                        answer, duration = ollama_call(question)
                        
                    elif model_choice == "Google Gemini":
                        answer, duration = gemini_call(question)
                    
                    st.markdown(answer)
                    st.caption(f"⏱️ **Response Time:** {duration:.2f} seconds")
                    
                except Exception as e:
                    st.error(f"Error: {e}")