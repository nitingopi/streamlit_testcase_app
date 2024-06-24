import streamlit as st
from services.jira_service import get_jira_ticket_description, create_jira_issues
from services.excel_service import export_to_excel

def render_home_page(strategy):
    jira_id = st.text_input("Enter JIRA ID:")
    context = st.text_area("Enter additional context:")
    
    if st.button("Generate"):
        if jira_id:
            description = get_jira_ticket_description(jira_id)
            prompt = f"JIRA Description: {description}\nAdditional Context: {context}"
            response = strategy.get_response(prompt)
            test_cases = [{"name": f"Test Case {i+1}", "description": tc} for i, tc in enumerate(response.split('\n'))]
            st.session_state.test_cases = test_cases
            st.write("Generated Test Cases:", test_cases)
        else:
            st.error("Please enter a valid JIRA ID")

    if "test_cases" in st.session_state:
        st.write("Generated Test Cases:")
        st.table(st.session_state.test_cases)
        
        if st.button("Export to Excel"):
            file_name = export_to_excel(st.session_state.test_cases)
            st.success(f"Test cases exported to {file_name}")

        if st.button("Generate test cases in JIRA"):
            create_jira_issues(st.session_state.test_cases)
            st.success("Test cases created in JIRA")
