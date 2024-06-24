import streamlit as st
from strategies.openai_strategy import OpenAIStrategy
from strategies.gemini_strategy import GeminiStrategy
from strategies.ollama_strategy import OllamaStrategy
from ui.home import render_home_page

def main():
    st.sidebar.title("LLM Model Selector")
    llm_option = st.sidebar.selectbox("Choose an LLM API", ("OpenAI", "Gemini", "Ollama"))

    if llm_option == "OpenAI":
        strategy = OpenAIStrategy()
    elif llm_option == "Gemini":
        strategy = GeminiStrategy()
    else:
        strategy = OllamaStrategy()

    render_home_page(strategy)

if __name__ == "__main__":
    main()
