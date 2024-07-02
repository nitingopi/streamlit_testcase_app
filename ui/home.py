import streamlit as st
from services.jira_service import get_jira_ticket_response, create_jira_issues
from services.excel_service import export_to_excel
from utils.prompt_utils import generate_prompt
from strategies.base_strategy import LLMStrategy
import pandas as pd
import re
import json

def render_home_page(strategy:LLMStrategy):
    jira_id = st.text_input("Enter JIRA ID:")
    context = st.text_area("Enter additional context:")
    
    if st.button("Generate"):
        if jira_id:
            jira_response = get_jira_ticket_response(jira_id)
            prompt = generate_prompt(jira_response)
            # prompt = f"JIRA Description: {description}\nAdditional Context: {context}"
            response_orig = strategy.get_response(prompt)
            # Regular expression to find and remove trailing commas before closing brackets
            response = re.sub(r',(\s*[\]}])', r'\1', response_orig.text)
            # Parse the JSON string into a Python list
            test_cases_list = json.loads(response)
            # Create a DataFrame
            df = pd.DataFrame(test_cases_list)
            st.session_state.tests = df
            # Display the DataFrame in Streamlit
            # st.write("### Test Cases")
            # st.dataframe(df)
    
        else:
            st.error("Please enter a valid JIRA ID")

    if "tests" in st.session_state:
        st.write("### Test Cases")
        st.dataframe(st.session_state.tests)
        
        if st.button("Export to Excel"):
            file_name = export_to_excel(st.session_state.tests)
            st.success(f"Test cases exported to {file_name}")

        if st.button("Create test cases in JIRA"):
            create_jira_issues(st.session_state.tests)
            st.success("Test cases created in JIRA")
